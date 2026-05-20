

def extract_json(text: str) -> str:
    brace_depth = 0
    bracket_depth = 0
    in_string = False
    escape = False
    json_start = -1
    json_end = -1

    for i, char in enumerate(text):
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue

        if char == "{":
            if brace_depth == 0 and bracket_depth == 0:
                json_start = i
            brace_depth += 1
        elif char == "}":
            brace_depth -= 1
            if brace_depth == 0 and bracket_depth == 0:
                json_end = i + 1
                break
        elif char == "[":
            if bracket_depth == 0 and brace_depth == 0:
                json_start = i
            bracket_depth += 1
        elif char == "]":
            bracket_depth -= 1
            if bracket_depth == 0 and brace_depth == 0:
                json_end = i + 1
                break

    if json_start >= 0 and json_end > json_start:
        return text[json_start:json_end]

    return text


def extract_json_all(text: str) -> list[str]:
    blocks = []
    in_string = False
    escape = False
    brace_depth = 0
    bracket_depth = 0
    start = -1

    for i, char in enumerate(text):
        if escape:
            escape = False
            continue
        if char == "\\":
            escape = True
            continue
        if char == '"':
            in_string = not in_string
            continue
        if in_string:
            continue

        if char == "{":
            if brace_depth == 0 and bracket_depth == 0:
                start = i
            brace_depth += 1
        elif char == "}":
            brace_depth -= 1
            if brace_depth == 0 and bracket_depth == 0 and start >= 0:
                blocks.append(text[start : i + 1])
                start = -1
        elif char == "[":
            if bracket_depth == 0 and brace_depth == 0:
                start = i
            bracket_depth += 1
        elif char == "]":
            bracket_depth -= 1
            if bracket_depth == 0 and brace_depth == 0 and start >= 0:
                blocks.append(text[start : i + 1])
                start = -1

    return blocks
