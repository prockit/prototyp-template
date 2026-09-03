"""Input validation and DTOs of the example feature (Zod schema + DTO in the productive template).

Validation messages are i18n keys, never display strings; the template resolves them with `t()`.
"""

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from app.features.example.models import ExampleItem


class CreateExampleItemInput(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=2000)


class ExampleItemDto(BaseModel):
    """Output shape of the feature. No table entity crosses the feature boundary."""

    id: str
    title: str
    description: str
    created_at: str  # ISO 8601


def to_example_item_dto(entity: ExampleItem) -> ExampleItemDto:
    return ExampleItemDto(
        id=entity.id,
        title=entity.title,
        description=entity.description,
        created_at=entity.created_at.isoformat(),
    )


def field_error_keys(error: ValidationError) -> dict[str, list[str]]:
    """Map Pydantic errors to keys like `example.create.errors.titleRequired`."""
    keys: dict[str, list[str]] = {}
    for item in error.errors():
        field = str(item["loc"][0]) if item["loc"] else "form"
        suffix = "TooLong" if item["type"] == "string_too_long" else "Required"
        keys.setdefault(field, []).append(f"example.create.errors.{field}{suffix}")
    return keys
