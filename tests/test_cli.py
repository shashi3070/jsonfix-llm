import json
import tempfile
from pathlib import Path

from typer.testing import CliRunner

from jsonfix_llm.cli.main import app

runner = CliRunner()


def test_cli_stdin_simple():
    result = runner.invoke(app, ["repair"], input="{'name': 'shashi'}")
    assert result.exit_code == 0
    parsed = json.loads(result.stdout)
    assert parsed["name"] == "shashi"


def test_cli_stdin_stats():
    result = runner.invoke(app, ["repair", "--stats"], input="{'name': 'shashi'}")
    assert result.exit_code == 0
    assert "Repaired" in result.stderr
    assert "Fixes applied" in result.stderr


def test_cli_stdin_no_repair():
    result = runner.invoke(app, ["repair"], input='{"a": 1}')
    assert result.exit_code == 0
    assert result.stdout.strip() == '{"a": 1}'


def test_cli_file_input():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write("{'b': 2}")
        f.flush()
        filepath = f.name
    try:
        result = runner.invoke(app, ["repair", filepath])
        assert result.exit_code == 0
        parsed = json.loads(result.stdout)
        assert parsed["b"] == 2
    finally:
        Path(filepath).unlink(missing_ok=True)


def test_cli_file_output():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write("{'c': 3}")
        f.flush()
        inpath = f.name
    outpath = str(Path(inpath).with_suffix(".fixed.json"))
    try:
        result = runner.invoke(app, ["repair", inpath, "-o", outpath])
        assert result.exit_code == 0
        assert Path(outpath).exists()
        with open(outpath, encoding="utf-8") as f:
            parsed = json.load(f)
            assert parsed["c"] == 3
    finally:
        Path(inpath).unlink(missing_ok=True)
        Path(outpath).unlink(missing_ok=True)


def test_cli_file_stats():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        f.write("{'d': 4}")
        f.flush()
        filepath = f.name
    try:
        result = runner.invoke(app, ["repair", filepath, "--stats"])
        assert result.exit_code == 0
        assert "Repaired" in result.stderr
    finally:
        Path(filepath).unlink(missing_ok=True)


def test_cli_extract_stdin():
    result = runner.invoke(app, ["extract"], input="```python\nx = 1\n```")
    assert result.exit_code == 0
    assert "x = 1" in result.stdout


def test_cli_extract_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("```python\ny = 2\n```")
        f.flush()
        filepath = f.name
    try:
        result = runner.invoke(app, ["extract", filepath, "--language", "python"])
        assert result.exit_code == 0
        assert "y = 2" in result.stdout
    finally:
        Path(filepath).unlink(missing_ok=True)


def test_cli_extract_output():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("```python\nz = 3\n```")
        f.flush()
        inpath = f.name
    outpath = str(Path(inpath).with_suffix(".extracted.py"))
    try:
        result = runner.invoke(app, ["extract", inpath, "-o", outpath])
        assert result.exit_code == 0
        assert Path(outpath).exists()
        with open(outpath, encoding="utf-8") as f:
            assert "z = 3" in f.read()
    finally:
        Path(inpath).unlink(missing_ok=True)
        Path(outpath).unlink(missing_ok=True)


def test_cli_extract_all():
    result = runner.invoke(app, ["extract", "--all"], input="```py\na=1\n```\n```py\nb=2\n```")
    assert result.exit_code == 0
    assert "a=1" in result.stdout
    assert "b=2" in result.stdout


def test_cli_extract_language_json():
    result = runner.invoke(app, ["extract", "--language", "json"],
                           input='```json\n{"e": 5}\n```')
    assert result.exit_code == 0
    assert '"e": 5' in result.stdout


def test_cli_default_routes_to_repair():
    result = runner.invoke(app, [], input="{'x': 1}")
    assert result.exit_code == 0
    parsed = json.loads(result.stdout)
    assert parsed["x"] == 1


def test_cli_stats_with_errors():
    result = runner.invoke(app, ["repair", "--stats"], input="not json at all")
    assert result.exit_code == 0
    assert "Repaired" in result.stderr


def test_cli_extract_file_output():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write("```python\nval=42\n```")
        f.flush()
        inpath = f.name
    outpath = str(Path(inpath).with_suffix(".extr.py"))
    try:
        result = runner.invoke(app, ["extract", inpath, "-o", outpath])
        assert result.exit_code == 0
        assert Path(outpath).exists()
        with open(outpath, encoding="utf-8") as f:
            assert "val=42" in f.read()
    finally:
        Path(inpath).unlink(missing_ok=True)
        Path(outpath).unlink(missing_ok=True)
