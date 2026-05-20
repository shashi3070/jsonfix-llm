from jsonfix_llm.extract.extract_json import extract_json, extract_json_all
from tests.fixtures import (
    EXTRACT_JSON_ARRAY,
    EXTRACT_JSON_ARRAY_EXPECTED,
    EXTRACT_JSON_EMBEDDED,
    EXTRACT_JSON_EMBEDDED_EXPECTED,
    EXTRACT_JSON_MULTIPLE,
    EXTRACT_JSON_NESTED_BRACKETS,
    EXTRACT_JSON_NESTED_BRACKETS_EXPECTED,
    VALID_JSON,
    VALID_JSON_ARRAY,
    VALID_JSON_NESTED,
)


def test_extract_embedded_json():
    result = extract_json(EXTRACT_JSON_EMBEDDED)
    assert result == EXTRACT_JSON_EMBEDDED_EXPECTED


def test_extract_nested_brackets():
    result = extract_json(EXTRACT_JSON_NESTED_BRACKETS)
    assert result == EXTRACT_JSON_NESTED_BRACKETS_EXPECTED


def test_extract_array():
    result = extract_json(EXTRACT_JSON_ARRAY)
    assert result == EXTRACT_JSON_ARRAY_EXPECTED


def test_extract_first_json_block():
    result = extract_json(EXTRACT_JSON_MULTIPLE)
    assert result == '{"a": 1}'


def test_extract_all_json_blocks():
    result = extract_json_all(EXTRACT_JSON_MULTIPLE)
    assert len(result) == 2
    assert result[0] == '{"a": 1}'
    assert result[1] == '{"b": 2}'


def test_passes_through_plain_json():
    assert extract_json(VALID_JSON) == VALID_JSON
    assert extract_json(VALID_JSON_ARRAY) == VALID_JSON_ARRAY
    assert extract_json(VALID_JSON_NESTED) == VALID_JSON_NESTED


def test_no_json_found_returns_input():
    text = "Just plain text."
    assert extract_json(text) == text


def test_returns_empty_list_for_no_json():
    result = extract_json_all("No JSON here")
    assert result == []


def test_extract_all_escaped_quotes():
    text = r'{"a": "b\"c"} and {"d": "e\"f"}'
    result = extract_json_all(text)
    assert len(result) == 2
    assert '"a"' in result[0]
    assert '"d"' in result[1]


def test_extract_all_escaped_backslash():
    text = r'{"path": "c:\\dir"} and {"path2": "d:\\dir"}'
    result = extract_json_all(text)
    assert len(result) == 2


def test_extract_escaped_quotes():
    text = r'{"msg": "hello \"world\""}'
    result = extract_json(text)
    assert '"hello \\"world\\""' in result


def test_extract_escaped_backslash():
    text = r'{"path": "c:\\dir"}'
    result = extract_json(text)
    assert '"c:\\\\dir"' in result


def test_extract_all_arrays():
    result = extract_json_all("[1, 2, 3] and [4, 5]")
    assert len(result) == 2
    assert result[0] == "[1, 2, 3]"
    assert result[1] == "[4, 5]"


def test_extract_all_mixed():
    result = extract_json_all('{"a": 1} and [1, 2]')
    assert len(result) == 2
    assert result[0] == '{"a": 1}'
    assert result[1] == "[1, 2]"


def test_extract_array_from_text():
    result = extract_json("Here is [1, 2, 3]")
    assert result == "[1, 2, 3]"
