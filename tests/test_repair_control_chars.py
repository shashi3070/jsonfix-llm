from jsonfix_ai.repair.control_chars import fix_control_chars
from tests.fixtures import (
    CONTROL_NEWLINES,
    CONTROL_TABS,
    CONTROL_TABS_EXPECTED,
)


def test_escape_newlines_in_string():
    result = fix_control_chars(CONTROL_NEWLINES)
    assert "\\n" in result


def test_escape_tabs_in_string():
    result = fix_control_chars(CONTROL_TABS)
    assert result == CONTROL_TABS_EXPECTED


def test_passes_through_clean():
    text = '{"a": 1}'
    assert fix_control_chars(text) == text


def test_escape_carriage_return():
    text = '{"text": "line1\rline2"}'
    result = fix_control_chars(text)
    assert "\\r" in result


def test_handles_escaped_backslash():
    text = '{"path": "c:\\dir"}'
    result = fix_control_chars(text)
    assert "c:" in result


def test_handles_escaped_quote():
    text = '{"msg": "hello \\"world\\""}'
    result = fix_control_chars(text)
    assert "world" in result
