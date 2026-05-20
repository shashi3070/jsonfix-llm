from jsonfix_llm.repair.literals import fix_python_literals
from tests.fixtures import (
    PYTHON_LITERALS,
    PYTHON_LITERALS_EXPECTED,
    PYTHON_LITERALS_STRING,
    PYTHON_LITERALS_STRING_EXPECTED,
)


def test_fix_true():
    result = fix_python_literals('{"v": True}')
    assert "true" in result
    assert "True" not in result


def test_fix_false():
    result = fix_python_literals('{"v": False}')
    assert "false" in result
    assert "False" not in result


def test_fix_none():
    result = fix_python_literals('{"v": None}')
    assert "null" in result
    assert "None" not in result


def test_fix_undefined():
    result = fix_python_literals('{"v": undefined}')
    assert "null" in result


def test_fix_nan():
    result = fix_python_literals('{"v": NaN}')
    assert "null" in result


def test_fix_all_literals():
    result = fix_python_literals(PYTHON_LITERALS)
    assert result == PYTHON_LITERALS_EXPECTED


def test_preserves_true_in_string():
    result = fix_python_literals(PYTHON_LITERALS_STRING)
    assert result == PYTHON_LITERALS_STRING_EXPECTED


def test_passes_through_no_literals():
    text = '{"name": "shashi"}'
    assert fix_python_literals(text) == text


def test_handles_escaped_quotes():
    text = r'{"msg": "hello \"True\" world"}'
    result = fix_python_literals(text)
    assert "true" not in result
    assert "True" in result


def test_handles_backslash():
    text = r'{"path": "c:\\None"}'
    result = fix_python_literals(text)
    assert "null" not in result


def test_handles_escaped_backslash_before_literal():
    text = r'{"x": "\\True"}'
    result = fix_python_literals(text)
    assert "true" not in result
