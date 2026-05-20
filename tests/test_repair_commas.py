from jsonfix_ai.repair.commas import fix_commas, fix_trailing_commas
from tests.fixtures import (
    MISSING_COMMAS,
    MISSING_COMMAS_NESTED,
    MISSING_COMMAS_NESTED_EXPECTED,
    TRAILING_COMMAS,
    TRAILING_COMMAS_ARRAY,
    TRAILING_COMMAS_ARRAY_EXPECTED,
    TRAILING_COMMAS_EXPECTED,
)


def test_fix_missing_commas():
    result = fix_commas(MISSING_COMMAS)
    assert "," in result


def test_fix_missing_commas_nested():
    result = fix_commas(MISSING_COMMAS_NESTED)
    assert "," in result
    assert result == MISSING_COMMAS_NESTED_EXPECTED


def test_fix_trailing_commas():
    result = fix_commas(TRAILING_COMMAS)
    assert result == TRAILING_COMMAS_EXPECTED


def test_fix_trailing_commas_array():
    result = fix_commas(TRAILING_COMMAS_ARRAY)
    assert result == TRAILING_COMMAS_ARRAY_EXPECTED


def test_trailing_before_missing():
    result = fix_trailing_commas(TRAILING_COMMAS)
    assert "}," not in result


def test_passes_through_good_json():
    text = '{"a": 1, "b": 2}'
    assert fix_commas(text) == text
