"""Database access of the example feature. Nothing but queries; no business logic."""

from sqlmodel import Session, col, select

from app.features.example.models import ExampleItem


def find_example_items(session: Session) -> list[ExampleItem]:
    statement = select(ExampleItem).order_by(col(ExampleItem.created_at))
    return list(session.exec(statement).all())


def insert_example_item(session: Session, entity: ExampleItem) -> ExampleItem:
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity
