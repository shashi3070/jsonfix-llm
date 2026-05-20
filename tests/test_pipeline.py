import json

from jsonfix_llm import repair_json
from jsonfix_llm.models import RepairResult
from tests.fixtures import (
    BOM_TEXT,
    COMPLEX_LLM_OUTPUT,
    COMPLEX_OPENAI,
    COMPLEX_TRUNCATED,
    COMPLEX_WRONG_BRACKET,
    SINGLE_QUOTES_OBJECT,
    VALID_JSON,
)


def test_repair_complex_llm_output():
    result = repair_json(COMPLEX_LLM_OUTPUT)
    parsed = json.loads(result)
    assert parsed["name"] == "shashi"
    assert parsed["age"] == 25
    assert parsed["active"] is True
    assert parsed["tags"] == ["dev", "ops"]


def test_repair_openai_style():
    result = repair_json(COMPLEX_OPENAI)
    parsed = json.loads(result)
    assert parsed["name"] == "Shashi"
    assert parsed["preferred_name"] is None
    assert parsed["role"] == "engineer"
    assert parsed["settings"]["notifications"] is True
    assert parsed["settings"]["theme"] == "dark"


def test_repair_truncated():
    result = repair_json(COMPLEX_TRUNCATED)
    parsed = json.loads(result)
    assert parsed["name"] == "shashi"


def test_repair_wrong_bracket():
    result = repair_json(COMPLEX_WRONG_BRACKET)
    parsed = json.loads(result)
    assert parsed["name"] == "shashi"


def test_repair_bom():
    result = repair_json(BOM_TEXT)
    parsed = json.loads(result)
    assert parsed["name"] == "shashi"


def test_rich_result():
    result = repair_json(SINGLE_QUOTES_OBJECT, rich=True)
    assert isinstance(result, RepairResult)
    assert result.was_repaired is True
    assert "quotes_fixed" in result.fixes


def test_rich_result_no_repair():
    result = repair_json(VALID_JSON, rich=True)
    assert isinstance(result, RepairResult)
    assert result.was_repaired is False
    assert result.fixes == []


def test_passes_through_valid_jsons():
    for text in [VALID_JSON, '{"a": 1, "b": 2}', '[1, 2, 3]', '{"nested": {"deep": true}}']:
        result = repair_json(text)
        assert json.loads(result) is not None


def test_simple_returns_string():
    result = repair_json(SINGLE_QUOTES_OBJECT)
    assert isinstance(result, str)


def test_repair_missing_values():
    text = '{"name": , "age": 25}'
    result = repair_json(text, rich=True)
    assert "values_fixed" in result.fixes
    assert "null" in result.fixed


def test_repair_control_chars():
    text = '{"text": "line1\nline2"}'
    result = repair_json(text, rich=True)
    assert "control_chars_escaped" in result.fixes
    assert "\\n" in result.fixed


def test_repair_missing_colons():
    text = '{"name" "shashi", "age": 25}'
    result = repair_json(text, rich=True)
    assert '"name":' in result.fixed
