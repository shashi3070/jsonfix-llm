import json

from jsonfix_llm.repair.brackets import auto_close_brackets
from tests.fixtures import (
    EMPTY_ARRAY,
    EMPTY_OBJECT,
    UNCLOSED_BRACES,
    UNCLOSED_BRACES_EXPECTED,
    UNCLOSED_BRACKETS,
    UNCLOSED_BRACKETS_EXPECTED,
    UNCLOSED_NESTED,
    UNCLOSED_NESTED_EXPECTED,
)


def test_close_unclosed_brace():
    result = auto_close_brackets(UNCLOSED_BRACES)
    assert result == UNCLOSED_BRACES_EXPECTED


def test_close_unclosed_bracket():
    result = auto_close_brackets(UNCLOSED_BRACKETS)
    assert result == UNCLOSED_BRACKETS_EXPECTED


def test_close_nested():
    result = auto_close_brackets(UNCLOSED_NESTED)
    assert result == UNCLOSED_NESTED_EXPECTED


def test_passes_through_empty_object():
    assert auto_close_brackets(EMPTY_OBJECT) == EMPTY_OBJECT


def test_passes_through_empty_array():
    assert auto_close_brackets(EMPTY_ARRAY) == EMPTY_ARRAY


def test_passes_through_valid_json():
    text = '{"a": 1}'
    assert auto_close_brackets(text) == text


def test_result_is_valid_json():
    result = auto_close_brackets(UNCLOSED_BRACES)
    parsed = json.loads(result)
    assert parsed["name"] == "shashi"


def test_ignores_brackets_inside_escaped_strings():
    text = '{"msg": "hello {world}"}'
    result = auto_close_brackets(text)
    parsed = json.loads(result)
    assert parsed["msg"] == "hello {world}"


def test_ignores_backslash_before_brace():
    text = '{"x": "\\\\{"}'
    result = auto_close_brackets(text)
    assert "{ }" in result or '"\\\\{"' in result
