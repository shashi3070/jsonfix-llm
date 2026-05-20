from jsonfix_ai.repair.comments import strip_comments
from tests.fixtures import (
    COMMENTS_BLOCK,
    COMMENTS_BLOCK_EXPECTED,
    COMMENTS_LINE,
    COMMENTS_LINE_EXPECTED,
    COMMENTS_URL,
)


def test_strip_line_comment():
    result = strip_comments(COMMENTS_LINE)
    assert "//" not in result
    assert result == COMMENTS_LINE_EXPECTED


def test_strip_block_comment():
    result = strip_comments(COMMENTS_BLOCK)
    assert "/*" not in result
    assert result == COMMENTS_BLOCK_EXPECTED


def test_preserves_url():
    result = strip_comments(COMMENTS_URL)
    assert "http://example.com" in result


def test_passes_through_no_comments():
    text = '{"name": "shashi"}'
    assert strip_comments(text) == text


def test_preserves_escaped_quotes():
    text = r'{"url": "http://example.com"}'
    assert strip_comments(text) == text


def test_preserves_single_quotes():
    text = r"{'key': 'value'}"
    result = strip_comments(text)
    assert "'key'" in result


def test_preserves_url_with_slashes():
    text = r'{"url": "https://example.com/path"}'
    assert strip_comments(text) == text


def test_strip_comment_inside_escaped_string():
    text = '{"url": "http://example.com"} // not a comment'
    result = strip_comments(text)
    assert "// not a comment" not in result


def test_strip_comment_inside_single_quoted_string():
    text = "{'url': 'http://example.com//path'}"
    result = strip_comments(text)
    assert "'url'" in result
    assert "'http://example.com//path'" in result or '"http://example.com//path"' in result


def test_strip_block_comment_outside_string():
    text = '{"msg": "hello"} /* real comment */ {"other": "world"}'
    result = strip_comments(text)
    assert "/* real comment */" not in result


def test_escape_before_comment():
    text = r'{"path": "c:\dir"} // trailing comment'
    result = strip_comments(text)
    assert "// trailing comment" not in result
    assert "c:" in result
