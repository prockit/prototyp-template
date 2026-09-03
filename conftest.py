"""Shared test fixtures. Tests use a fresh in-memory SQLite database, never data/."""

import os

os.environ["DATABASE_URL"] = "sqlite://"
os.environ["AUTH_REQUIRED"] = "true"
os.environ["SESSION_SECRET"] = "test-secret"
os.environ["DEFAULT_LANGUAGE"] = "de"

from collections.abc import Iterator  # noqa: E402

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from sqlmodel import Session  # noqa: E402

from app.core.db import engine, reset  # noqa: E402
from app.main import app  # noqa: E402
from app.seed import seed  # noqa: E402


@pytest.fixture
def session() -> Iterator[Session]:
    """A freshly reset and seeded database session."""
    reset()
    with Session(engine) as db_session:
        seed(db_session)
        yield db_session


@pytest.fixture
def client(session: Session) -> Iterator[TestClient]:
    """Anonymous HTTP client against the app, sharing the in-memory database of `session`."""
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def signed_in_client(client: TestClient) -> TestClient:
    """HTTP client signed in as the seeded admin user via the fake login."""
    client.post("/auth/signin", data={"user_id": "user-admin"}, follow_redirects=False)
    return client
