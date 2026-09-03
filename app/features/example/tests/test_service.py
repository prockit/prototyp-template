from sqlmodel import Session

from app.features.example.schemas import CreateExampleItemInput
from app.features.example.service import create_example_item, get_example_items


def test_get_example_items_returns_seeded_items_in_creation_order(session: Session) -> None:
    items = get_example_items(session)

    assert [item.id for item in items] == ["example-1", "example-2", "example-3"]


def test_create_example_item_assigns_id_and_created_at(session: Session) -> None:
    created = create_example_item(
        session, CreateExampleItemInput(title="New item", description="Something useful")
    )

    assert created.id
    assert created.created_at
    assert created.id in [item.id for item in get_example_items(session)]
