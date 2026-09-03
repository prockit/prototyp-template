"""Database engine and session. SQLite only, no migrations: `reset()` recreates everything."""

import importlib
import pkgutil
from collections.abc import Iterator
from pathlib import Path

from sqlalchemy import Engine
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

_IN_MEMORY_URLS = ("sqlite://", "sqlite:///:memory:")


def _build_engine(url: str) -> Engine:
    if url in _IN_MEMORY_URLS:
        # One shared connection so the whole app (and the tests) see the same in-memory database.
        return create_engine(url, connect_args={"check_same_thread": False}, poolclass=StaticPool)
    if url.startswith("sqlite:///"):
        Path(url.removeprefix("sqlite:///")).parent.mkdir(parents=True, exist_ok=True)
    return create_engine(url, connect_args={"check_same_thread": False})


engine: Engine = _build_engine(settings.database_url)


def get_session() -> Iterator[Session]:
    """FastAPI dependency: one session per request."""
    with Session(engine) as session:
        yield session


def import_all_models() -> None:
    """Import every module that defines tables so `SQLModel.metadata` knows all of them.

    Core tables live in `app.core.auth` and `app.core.outbox`; every feature slice under
    `app/features/<feature>/models.py` is discovered automatically.
    """
    import app.core.auth  # noqa: F401
    import app.core.outbox  # noqa: F401
    import app.features as features

    for module_info in pkgutil.iter_modules(features.__path__):
        if not module_info.ispkg:
            continue
        module_name = f"app.features.{module_info.name}.models"
        try:
            importlib.import_module(module_name)
        except ModuleNotFoundError as error:
            if error.name != module_name:
                raise


def create_all() -> None:
    import_all_models()
    SQLModel.metadata.create_all(engine)


def reset() -> None:
    """Drop and recreate all tables. The caller seeds afterwards."""
    import_all_models()
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
