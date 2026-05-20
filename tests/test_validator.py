import json

from jsonfix_llm.validators.validator import validate_json


def test_validates_correct_json():
    is_valid, errors = validate_json('{"name": "shashi"}')
    assert is_valid is True
    assert errors == []


def test_validates_array():
    is_valid, errors = validate_json("[1, 2, 3]")
    assert is_valid is True
    assert errors == []


def test_reports_error_for_invalid_json():
    is_valid, errors = validate_json("{invalid}")
    assert is_valid is False
    assert len(errors) > 0
    assert "line" in errors[0]


def test_reports_error_for_truncated():
    is_valid, errors = validate_json('{"name": "shashi')
    assert is_valid is False
    assert len(errors) > 0


def test_reports_error_for_empty():
    is_valid, errors = validate_json("")
    assert is_valid is False
    assert len(errors) > 0
