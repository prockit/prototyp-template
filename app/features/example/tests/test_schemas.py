import pytest
from pydantic import ValidationError

from app.features.example.schemas import CreateExampleItemInput, field_error_keys


def test_input_is_trimmed() -> None:
    payload = CreateExampleItemInput(title="  Title  ", description="  Text  ")

    assert payload.title == "Title"
    assert payload.description == "Text"


def test_empty_and_too_long_values_map_to_i18n_keys() -> None:
    with pytest.raises(ValidationError) as raised:
        CreateExampleItemInput(title="", description="x" * 2001)

    assert field_error_keys(raised.value) == {
        "title": ["example.create.errors.titleRequired"],
        "description": ["example.create.errors.descriptionTooLong"],
    }
