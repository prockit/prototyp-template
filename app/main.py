"""FastAPI application: middleware, routers and the two global routes `/` and `/lang/{code}`."""

from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.core import auth, outbox
from app.core.config import settings
from app.core.db import create_all
from app.core.i18n import SUPPORTED_LANGUAGES
from app.core.logger import configure_logging, logger
from app.core.templating import APP_DIR, render
from app.features.example.routes import router as example_router

# Paths reachable without the fake login (mirrors the public routes of the productive proxy).
PUBLIC_PATH_PREFIXES = ("/auth/", "/static/", "/design/", "/lang/")


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    configure_logging()
    create_all()
    logger.info("prototype started: app_name=%s", settings.app_name)
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.mount("/static", StaticFiles(directory=APP_DIR / "static"), name="static")
app.mount("/design", StaticFiles(directory=APP_DIR / "design" / "project"), name="design")


@app.middleware("http")
async def auth_guard(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    is_public = request.url.path.startswith(PUBLIC_PATH_PREFIXES)
    if settings.auth_required and not is_public and "user_id" not in request.session:
        return RedirectResponse(url="/auth/signin", status_code=303)
    return await call_next(request)


# Added after the guard so it wraps it: the guard can read `request.session`.
app.add_middleware(SessionMiddleware, secret_key=settings.session_secret, same_site="lax")

app.include_router(auth.router)
app.include_router(outbox.router)
app.include_router(example_router)


@app.get("/")
def home(request: Request) -> HTMLResponse:
    return render(request, "home.html")


@app.get("/lang/{code}")
def set_language(code: str, request: Request) -> RedirectResponse:
    response = RedirectResponse(url=request.headers.get("referer") or "/", status_code=303)
    if code in SUPPORTED_LANGUAGES:
        response.set_cookie("lang", code, max_age=365 * 24 * 3600, samesite="lax")
    return response
