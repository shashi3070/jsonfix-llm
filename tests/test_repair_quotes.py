from jsonfix_llm.repair.quotes import fix_quotes
from tests.fixtures import (
    SINGLE_QUOTES_APOSTROPHE,
    SINGLE_QUOTES_APOSTROPHE_EXPECTED,
    SINGLE_QUOTES_MIXED,
    SINGLE_QUOTES_NESTED,
    SINGLE_QUOTES_OBJECT,
    UNQUOTED_KEYS,
    UNQUOTED_KEYS_ARRAY,
    UNQUOTED_KEYS_NESTED,
)


def test_fix_single_quotes():
    result = fix_quotes(SINGLE_QUOTES_OBJECT)
    assert "'" not in result


def test_fix_single_quotes_nested():
    result = fix_quotes(SINGLE_QUOTES_NESTED)
    assert "'" not in result


def test_fix_single_quotes_mixed():
    result = fix_quotes(SINGLE_QUOTES_MIXED)
    assert "'" not in result


def test_fix_single_quotes_apostrophe():
    result = fix_quotes(SINGLE_QUOTES_APOSTROPHE)
    assert result == SINGLE_QUOTES_APOSTROPHE_EXPECTED


def test_fix_unquoted_keys():
    result = fix_quotes(UNQUOTED_KEYS)
    assert '"name"' in result
    assert '"age"' in result


def test_fix_unquoted_keys_nested():
    result = fix_quotes(UNQUOTED_KEYS_NESTED)
    assert '"user"' in result
    assert '"name"' in result
    assert '"active"' in result


def test_fix_unquoted_keys_array():
    result = fix_quotes(UNQUOTED_KEYS_ARRAY)
    assert '"name"' in result


def test_passes_through_valid_json():
    text = '{"name": "shashi"}'
    assert fix_quotes(text) == text


def test_fix_quotes_escaped_backslash():
    text = "{\\'name\\': \\'shashi\\'}"
    result = fix_quotes(text)
    assert "name" in result or "'name'" in result


def test_fix_unquoted_keys_with_underscore():
    text = "{my_key: 'value'}"
    result = fix_quotes(text)
    assert '"my_key"' in result


def test_fix_no_identifier_after_brace():
    text = "{  : 'value'}"
    result = fix_quotes(text)
    assert result == '{  : "value"}'


def test_fix_unquoted_keys_escaped_in_string():
    text = '{"key\\": "value"}'
    result = fix_quotes(text)
    assert '"value"' in result


def test_fix_unquoted_keys_with_whitespace_before_colon():
    text = "{name   : 'shashi'}"
    result = fix_quotes(text)
    assert '"name"' in result
    assert '"shashi"' in result


def test_fix_unquoted_keys_without_colon_after_ident():
    text = "{foo bar}"
    result = fix_quotes(text)
    assert "foo" in result
    assert "bar" in result
