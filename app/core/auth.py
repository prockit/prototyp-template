"""Fake login for prototypes: pick a sample person, no password (the real app uses Entra ID).

The session cookie (signed, HttpOnly) carries `user_id`, `user_name` and `role`, mirroring the JWT
session of the productive template. `UserRole` is the single source of truth for roles.
"""

from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlmodel import Field, Session, SQLModel, col, select

from app.core.db import get_session
from app.core.templating import render

UserRole = Literal["ADMIN", "USER"]
USER_ROLES: tuple[UserRole, ...] = ("ADMIN", "USER")


class User(SQLModel, table=True):
    id: str = Field(primary_key=True)
    email: str = Field(unique=True, index=True)
    first_name: str
    last_name: str
    role: str = Field(default="USER")

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


def get_current_user(
    request: Request, session: Annotated[Session, Depends(get_session)]
) -> User | None:
    """FastAPI dependency: the signed-in user, or None."""
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    return session.get(User, user_id)


router = APIRouter(prefix="/auth")


@router.get("/signin")
def signin_page(
    request: Request, session: Annotated[Session, Depends(get_session)]
) -> HTMLResponse:
    users = session.exec(select(User).order_by(col(User.last_name))).all()
    return render(request, "auth/signin.html", {"users": users})


@router.post("/signin")
def signin(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    user_id: Annotated[str, Form()],
) -> RedirectResponse:
    user = session.get(User, user_id)
    if user is None:
        return RedirectResponse(url="/auth/signin", status_code=303)
    request.session.update({"user_id": user.id, "user_name": user.full_name, "role": user.role})
    return RedirectResponse(url="/", status_code=303)


@router.post("/signout")
def signout(request: Request) -> RedirectResponse:
    request.session.clear()
    return RedirectResponse(url="/auth/signin", status_code=303)
