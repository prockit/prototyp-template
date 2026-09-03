"""Routes of the example feature. GET renders pages; POST validates, calls the service, redirects.

GET  /example   list page with the create form   (page.tsx in the productive template)
POST /example   create                           (Server Action in the productive template)
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import ValidationError
from sqlmodel import Session

from app.core.db import get_session
from app.core.logger import logger
from app.core.templating import render
from app.features.example.schemas import CreateExampleItemInput, field_error_keys
from app.features.example.service import create_example_item, get_example_items

router = APIRouter(prefix="/example")


@router.get("")
def list_page(request: Request, session: Annotated[Session, Depends(get_session)]) -> HTMLResponse:
    return render(
        request,
        "example/list.html",
        {"items": get_example_items(session), "form": {}, "field_errors": {}},
    )


@router.post("")
def create(
    request: Request,
    session: Annotated[Session, Depends(get_session)],
    title: Annotated[str, Form()] = "",
    description: Annotated[str, Form()] = "",
) -> Response:
    submitted = {"title": title, "description": description}
    try:
        payload = CreateExampleItemInput(**submitted)
    except ValidationError as error:
        return render(
            request,
            "example/list.html",
            {
                "items": get_example_items(session),
                "form": submitted,
                "field_errors": field_error_keys(error),
            },
            status_code=400,
        )

    try:
        create_example_item(session, payload)
    except Exception:
        # Internals never reach the UI; details go to the structured log only.
        logger.exception("failed to create example item")
        return render(
            request,
            "example/list.html",
            {
                "items": get_example_items(session),
                "form": submitted,
                "field_errors": {},
                "error": "example.create.errors.unexpected",
            },
            status_code=500,
        )

    return RedirectResponse(url="/example", status_code=303)
