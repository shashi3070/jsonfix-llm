# jsonfix-llm

Repair broken JSON from LLM outputs. Stop fighting malformed JSON.

## Install

```bash
pip install jsonfix-llm
```

## Quick Start

```python
from jsonfix_llm import repair_json

fixed = repair_json("""{
  'name': 'shashi'
  'age': 25
}""")
# {"name": "shashi", "age": 25}
```

## Features

- **Markdown fence stripping** — removes ` ```json ... ``` ` wrappers
- **Comment stripping** — removes `//` and `/* */` comments
- **Quote fixing** — single quotes → double quotes, unquoted keys → quoted
- **Literal fixing** — `True/False/None` → `true/false/null`
- **Comma fixing** — inserts missing commas, removes trailing commas
- **Value fixing** — fills missing values, fixes missing colons
- **Control char escaping** — escapes literal newlines/tabs in strings
- **Bracket auto-close** — appends missing `}` or `]`, handles truncation
- **Code extraction** — extracts code from fenced, indented, inline, and XML blocks
- **CLI tool** — quick repair from the terminal

## API

```python
from jsonfix_llm import repair_json, extract_code, extract_json

# Simple repair
fixed = repair_json(text)

# Rich result
result = repair_json(text, rich=True)
print(result.fixed)
print(result.was_repaired)
print(result.fixes)
print(result.error_count)
print(result.errors)

# Extract code (default: first Python block)
code = extract_code(text)
# language-specific: extract_code(text, language="python")
# all blocks: extract_code(text, language="json", all=True)

# Extract JSON blocks
json_block = extract_json(text)
json_blocks = extract_json(text, all=True)
```

## CLI

```bash
# Repair JSON file
jsonfix broken.json

# Read from stdin
echo '{"a":1' | jsonfix

# Write to file
jsonfix in.json -o fixed.json

# Show repair stats
jsonfix in.json --stats

# Extract code blocks
jsonfix extract file.md --language python
jsonfix extract file.md --language python -o output.py
jsonfix extract file.md --language json --all
```

## Development

```bash
pip install -e ".[dev]"
pytest tests/ -v
```
