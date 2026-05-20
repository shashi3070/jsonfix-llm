from jsonfix_ai.repair.markdown import strip_markdown_fences
from tests.fixtures import (
    MARKDOWN_FENCED,
    MARKDOWN_MULTIPLE,
    MARKDOWN_NO_LANG,
    MARKDOWN_NO_LANG_EXPECTED,
)


def test_strips_language_tagged_fence():
    result = strip_markdown_fences(MARKDOWN_FENCED)
    assert "```json" not in result
    assert "```" not in result


def test_strips_fence_without_language():
    result = strip_markdown_fences(MARKDOWN_NO_LANG)
    assert result.strip() == MARKDOWN_NO_LANG_EXPECTED.strip()


def test_handles_multiple_fences():
    result = strip_markdown_fences(MARKDOWN_MULTIPLE)
    assert "```" not in result
    assert '{"a": 1}' in result
    assert '{"b": 2}' in result


def test_passes_through_plain_text():
    text = '{"name": "shashi"}'
    assert strip_markdown_fences(text) == text
