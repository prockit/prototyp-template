"""Translations. Same JSON structure as the productive template, so the files transfer 1:1."""

import json
import logging
from pathlib import Path
from typing import Any

from fastapi import Request

from app.core.config import settings

SUPPORTED_LANGUAGES: tuple[str, ...] = ("de", "en")

_LOCALES_DIR = Path(__file__).parent / "locales"
_translations: dict[str, dict[str, Any]] = {
    language: json.loads((_LOCALES_DIR / f"{language}.json").read_text(encoding="utf-8"))
    for language in SUPPORTED_LANGUAGES
}
_logger = logging.getLogger("prototype.i18n")


def get_language(request: Request) -> str:
    language = request.cookies.get("lang", settings.default_language)
    return language if language in SUPPORTED_LANGUAGES else settings.default_language


def translate(language: str, key: str, **values: object) -> str:
    """Resolve a dotted key such as `example.create.title`. A missing key renders the key itself."""
    node: Any = _translations.get(language, {})
    for part in key.split("."):
        if not isinstance(node, dict) or part not in node:
            _logger.warning("missing translation: language=%s key=%s", language, key)
            return key
        node = node[part]
    text = str(node)
    return text.format(**values) if values else text
