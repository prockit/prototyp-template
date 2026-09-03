"""Synthetic sample data. Idempotent: rows that already exist (by id) are left untouched.

Never seed real persons, customers or production data.
"""

from datetime import UTC, datetime

from sqlmodel import Session

from app.core.auth import User
from app.core.db import create_all, engine
from app.features.example.models import ExampleItem


def demo_users() -> list[User]:
    return [
        User(
            id="user-admin",
            email="alex.admin@example.com",
            first_name="Alex",
            last_name="Admin",
            role="ADMIN",
        ),
        User(
            id="user-standard",
            email="mia.muster@example.com",
            first_name="Mia",
            last_name="Muster",
            role="USER",
        ),
    ]


def demo_example_items() -> list[ExampleItem]:
    return [
        ExampleItem(
            id="example-1",
            title="First example item",
            description="Shows how a list entry looks.",
            created_at=datetime(2026, 1, 5, 9, 0, tzinfo=UTC),
        ),
        ExampleItem(
            id="example-2",
            title="Second example item",
            description="Entries are ordered by creation time.",
            created_at=datetime(2026, 1, 6, 10, 30, tzinfo=UTC),
        ),
        ExampleItem(
            id="example-3",
            title="Third example item",
            description="Replace this feature with the first real one.",
            created_at=datetime(2026, 1, 7, 14, 15, tzinfo=UTC),
        ),
    ]


def seed(session: Session) -> None:
    for entity in [*demo_users(), *demo_example_items()]:
        if session.get(type(entity), entity.id) is None:
            session.add(entity)
    session.commit()


def main() -> None:
    create_all()
    with Session(engine) as session:
        seed(session)


if __name__ == "__main__":
    main()
