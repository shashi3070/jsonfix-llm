# Markdown fixtures
MARKDOWN_FENCED = """Here is your JSON:

```json
{
  "name": "shashi",
  "age": 25
}
```

Hope that helps!"""

MARKDOWN_FENCED_EXPECTED = """
{
  "name": "shashi",
  "age": 25
}

"""

MARKDOWN_NO_LANG = """```
{"name": "shashi"}
```"""

MARKDOWN_NO_LANG_EXPECTED = """{"name": "shashi"}"""

MARKDOWN_MULTIPLE = """First:
```json
{"a": 1}
```
Second:
```json
{"b": 2}
```"""

MARKDOWN_MULTIPLE_EXPECTED = """First:
{"a": 1}
Second:
{"b": 2}"""

# Comment fixtures
COMMENTS_LINE = """{
  // this is a comment
  "name": "shashi"
}"""

COMMENTS_LINE_EXPECTED = """{

  "name": "shashi"
}"""

COMMENTS_BLOCK = """{
  /* user info */
  "name": "shashi"
}"""

COMMENTS_BLOCK_EXPECTED = """{
  
  "name": "shashi"
}"""

COMMENTS_URL = """{
  "url": "http://example.com",
  "name": "shashi"
}"""

# Single quote fixtures
SINGLE_QUOTES_OBJECT = """{
  'name': 'shashi',
  'age': 25
}"""

SINGLE_QUOTES_OBJECT_EXPECTED = """{
  "name": "shashi",
  "age": 25
}"""

SINGLE_QUOTES_NESTED = """{
  'user': {
    'name': 'shashi',
    'active': True
  }
}"""

SINGLE_QUOTES_NESTED_EXPECTED = """{
  "user": {
    "name": "shashi",
    "active": True
  }
}"""

SINGLE_QUOTES_MIXED = """{
  "name": 'shashi',
  'age': "25"
}"""

SINGLE_QUOTES_APOSTROPHE = """{'name': "it's great"}"""

SINGLE_QUOTES_APOSTROPHE_EXPECTED = """{"name": "it's great"}"""

# Unquoted key fixtures
UNQUOTED_KEYS = """{
  name: "shashi",
  age: 25
}"""

UNQUOTED_KEYS_EXPECTED = """{
  "name": "shashi",
  "age": 25
}"""

UNQUOTED_KEYS_NESTED = """{
  user: {
    name: "shashi",
    active: true
  }
}"""

UNQUOTED_KEYS_NESTED_EXPECTED = """{
  "user": {
    "name": "shashi",
    "active": true
  }
}"""

UNQUOTED_KEYS_ARRAY = """[{
  name: "shashi"
}]"""

UNQUOTED_KEYS_ARRAY_EXPECTED = """[{
  "name": "shashi"
}]"""

# Python literal fixtures
PYTHON_LITERALS = """{
  "active": True,
  "data": None,
  "available": False,
  "value": undefined,
  "score": NaN
}"""

PYTHON_LITERALS_EXPECTED = """{
  "active": true,
  "data": null,
  "available": false,
  "value": null,
  "score": null
}"""

PYTHON_LITERALS_STRING = """{
  "message": "True story",
  "value": None
}"""

PYTHON_LITERALS_STRING_EXPECTED = """{
  "message": "True story",
  "value": null
}"""

# Comma fixtures
MISSING_COMMAS = """{
  "name": "shashi"
  "age": 25
}"""

MISSING_COMMAS_EXPECTED = """{
  "name": "shashi",
  "age": 25
}"""

MISSING_COMMAS_NESTED = """{
  "user": {
    "name": "shashi"
    "age": 25
  }
}"""

MISSING_COMMAS_NESTED_EXPECTED = """{
  "user": {
    "name": "shashi",
    "age": 25
  }
}"""

TRAILING_COMMAS = """{
  "name": "shashi",
  "age": 25,
}"""

TRAILING_COMMAS_EXPECTED = """{
  "name": "shashi",
  "age": 25}"""

TRAILING_COMMAS_ARRAY = """[1, 2, 3,]"""

TRAILING_COMMAS_ARRAY_EXPECTED = """[1, 2, 3]"""

# Bracket fixtures
UNCLOSED_BRACES = """{
  "name": "shashi\""""

UNCLOSED_BRACES_EXPECTED = """{
  "name": "shashi"}"""

UNCLOSED_BRACKETS = """[1, 2, 3"""

UNCLOSED_BRACKETS_EXPECTED = """[1, 2, 3]"""

UNCLOSED_NESTED = """{
  "items": [1, 2, 3
}"""

UNCLOSED_NESTED_EXPECTED = """{
  "items": [1, 2, 3
}]}"""

EMPTY_OBJECT = """{}"""

EMPTY_ARRAY = """[]"""

# Missing value fixtures
MISSING_VALUES = """{
  "name": ,
  "age": 25
}"""

MISSING_VALUES_EXPECTED = """{
  "name": null,
  "age": 25
}"""

MISSING_COLONS = """{
  "name" "shashi",
  "age": 25
}"""

MISSING_COLONS_EXPECTED = """{
  "name": "shashi",
  "age": 25
}"""

# Control char fixtures
CONTROL_NEWLINES = """{
  "text": "line1
line2"
}"""

CONTROL_TABS = """{
  "text": "col1\tcol2"
}"""

CONTROL_TABS_EXPECTED = """{
  "text": "col1\\tcol2"
}"""

# BOM fixture
BOM_TEXT = '\ufeff{"name": "shashi"}'
BOM_TEXT_EXPECTED = '{"name": "shashi"}'

# Complex multi-error fixtures
COMPLEX_LLM_OUTPUT = """Here's the JSON you asked for:

```json
{
  'name': 'shashi'
  'age': 25
  'active': True
  'tags': ['dev', 'ops']
}
"""

COMPLEX_LLM_OUTPUT_EXPECTED = """{
  "name": "shashi",
  "age": 25,
  "active": true,
  "tags": ["dev", "ops"]
}"""

COMPLEX_OPENAI = """{
  // user profile
  'name': 'Shashi'
  'preferred_name': None
  'role': 'engineer'
  'settings': {
    'notifications': True
    'theme': 'dark'
  }
}"""

COMPLEX_OPENAI_EXPECTED = """{
  "name": "Shashi",
  "preferred_name": null,
  "role": "engineer",
  "settings": {
    "notifications": true,
    "theme": "dark"
  }
}"""

COMPLEX_TRUNCATED = """{
  "name": "shashi\""""

COMPLEX_TRUNCATED_EXPECTED = """{
  "name": "shashi"
}"""

COMPLEX_WRONG_BRACKET = '''{"name": "shashi"'''

COMPLEX_WRONG_BRACKET_EXPECTED = '{"name": "shashi"}'

# Extract code fixtures
EXTRACT_FENCED_PYTHON = """Here's a function:
```python
def hello():
    print("hello")
```
"""

EXTRACT_FENCED_PYTHON_EXPECTED = """def hello():
    print("hello")"""

EXTRACT_FENCED_JSON = """```json
{"a": 1}
```"""

EXTRACT_MULTI_LANG = """Python:
```python
x = 1
```
JS:
```javascript
let x = 1;
```
"""

EXTRACT_XML_CODE = """<code>print("hello")</code>"""

EXTRACT_XML_PRE = """<pre>function test() {}</pre>"""

EXTRACT_INDENTED = """Some text:
    def hello():
        pass
More text."""

EXTRACT_INLINE = "Use the `print()` function."

EXTRACT_XML_CODE_EXPECTED = """print("hello")"""

EXTRACT_INLINE_EXPECTED = "print()"

# Valid JSON that should pass through
VALID_JSON = '{"name": "shashi", "age": 25}'
VALID_JSON_ARRAY = '[1, 2, 3]'
VALID_JSON_NESTED = '{"user": {"name": "shashi"}, "tags": ["a", "b"]}'

# Extract JSON fixtures
EXTRACT_JSON_EMBEDDED = """Here is your result:
{"name": "shashi", "age": 25}
Let me know if you need anything else."""

EXTRACT_JSON_EMBEDDED_EXPECTED = '{"name": "shashi", "age": 25}'

EXTRACT_JSON_MULTIPLE = """First: {"a": 1}
Second: {"b": 2}"""

EXTRACT_JSON_NESTED_BRACKETS = """Result: {"data": {"items": [1, 2, {"key": "val"}]}}"""

EXTRACT_JSON_NESTED_BRACKETS_EXPECTED = '{"data": {"items": [1, 2, {"key": "val"}]}}'

EXTRACT_JSON_ARRAY = """Array: [1, 2, 3]"""

EXTRACT_JSON_ARRAY_EXPECTED = "[1, 2, 3]"
