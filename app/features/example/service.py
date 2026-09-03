"""Business logic of the example feature. Knows no FastAPI and no Jinja."""

import uuid
from datetime import UTC, datetime

from sqlmodel import Session

from app.features.example.models import ExampleItem
from app.features.example.repository import find_example_items, insert_example_item
from app.features.example.schemas import (
    CreateExampleItemInput,
    ExampleItemDto,
    to_example_item_dto,
)


def get_example_items(session: Session) -> list[ExampleItemDto]:
    return [to_example_item_dto(entity) for entity in find_example_items(session)]


def create_example_item(session: Session, payload: CreateExampleItemInput) -> ExampleItemDto:
    entity = ExampleItem(
        id=str(uuid.uuid4()),
        title=payload.title,
        description=payload.description,
        created_at=datetime.now(UTC),
    )
    return to_example_item_dto(insert_example_item(session, entity))
