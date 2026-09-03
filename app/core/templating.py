"""Jinja2 rendering. Templates: `app/templates/` and `app/features/<feature>/templates/`."""

from datetime import UTC, datetime
from pathlib import Path

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.config import settings
from app.core.i18n import get_language, translate

APP_DIR = Path(__file__).resolve().parent.parent

_template_dirs = [APP_DIR / "templates", *sorted((APP_DIR / "features").glob("*/templates"))]
templates = Jinja2Templates(directory=[str(directory) for directory in _template_dirs])


def render(
    request: Request,
    name: str,
    context: dict[str, object] | None = None,
    status_code: int = 200,
) -> HTMLResponse:
    """Render a template with the standard context: `t`, `lang`, `app_name`, `year`."""
    language = get_language(request)

    def t(key: str, **values: object) -> str:
        return translate(language, key, **values)

    full_context: dict[str, object] = {
        "t": t,
        "lang": language,
        "app_name": settings.app_name,
        "year": datetime.now(UTC).year,
        **(context or {}),
    }
    return templates.TemplateResponse(request, name, full_context, status_code=status_code)
