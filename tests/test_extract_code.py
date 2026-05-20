from jsonfix_llm.extract.extract_code import extract_code
from tests.fixtures import (
    EXTRACT_FENCED_JSON,
    EXTRACT_FENCED_PYTHON,
    EXTRACT_FENCED_PYTHON_EXPECTED,
    EXTRACT_INDENTED,
    EXTRACT_INLINE,
    EXTRACT_INLINE_EXPECTED,
    EXTRACT_MULTI_LANG,
    EXTRACT_XML_CODE,
    EXTRACT_XML_CODE_EXPECTED,
    EXTRACT_XML_PRE,
)


def test_extract_fenced_python():
    result = extract_code(EXTRACT_FENCED_PYTHON, language="python")
    assert result == EXTRACT_FENCED_PYTHON_EXPECTED


def test_extract_fenced_json():
    result = extract_code(EXTRACT_FENCED_JSON, language="json")
    assert "a" in result


def test_extract_any_language():
    result = extract_code(EXTRACT_FENCED_PYTHON)
    assert "def hello" in result


def test_extract_xml_code():
    result = extract_code(EXTRACT_XML_CODE)
    assert result == EXTRACT_XML_CODE_EXPECTED


def test_extract_xml_pre():
    result = extract_code(EXTRACT_XML_PRE)
    assert "function test" in result


def test_extract_indented():
    result = extract_code(EXTRACT_INDENTED)
    assert "def hello" in result


def test_extract_indented_multi_line():
    text = "    def hello():\n        pass"
    result = extract_code(text)
    assert "def hello" in result
    assert "pass" in result


def test_extract_xml_fallback_to_indented():
    text = "    x = 1"
    result = extract_code(text)
    assert "x = 1" in result


def test_extract_inline():
    result = extract_code(EXTRACT_INLINE)
    assert result == EXTRACT_INLINE_EXPECTED


def test_extract_all_blocks():
    result = extract_code(EXTRACT_MULTI_LANG, all=True)
    assert isinstance(result, list)
    assert len(result) == 2


def test_extract_first_block_default():
    result = extract_code(EXTRACT_MULTI_LANG)
    assert isinstance(result, str)
    assert "x = 1" in result


def test_no_code_found_returns_input():
    text = "Just plain text, no code."
    assert extract_code(text) == text
