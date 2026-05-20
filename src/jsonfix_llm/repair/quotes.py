def fix_single_quotes(text: str) -> str:
    result = []
    in_double = False
    in_single = False
    escape = False
    for char in text:
        if escape:
            result.append(char)
            escape = False
            continue
        if char == "\\":
            result.append(char)
            escape = True
            continue
        if char == '"' and not in_single:
            in_double = not in_double
            result.append(char)
        elif char == "'" and not in_double:
            in_single = not in_single
            result.append('"')
        else:
            result.append(char)
    return "".join(result)


def _find_identifier(text: str, start: int) -> tuple[int, int, str]:
    i = start
    while i < len(text) and text[i] in " \t\n\r":
        i += 1
    if i >= len(text) or not (text[i].isalpha() or text[i] == "_"):
        return start, start, ""
    ident_start = i
    while i < len(text) and (text[i].isalnum() or text[i] == "_"):
        i += 1
    ident = text[ident_start:i]
    j = i
    while j < len(text) and text[j] in " \t\n\r":
        j += 1
    if j < len(text) and text[j] == ":":
        return start, j + 1, ident
    return start, start, ""


def fix_unquoted_keys(text: str) -> str:
    result = []
    in_double = False
    in_single = False
    escape = False
    i = 0
    while i < len(text):
        ch = text[i]
        if escape:
            result.append(ch)
            escape = False
            i += 1
            continue
        if ch == "\\":
            result.append(ch)
            escape = True
            i += 1
            continue
        if ch == '"':
            in_double = not in_double
            result.append(ch)
            i += 1
            continue
        if ch == "'":
            in_single = not in_single
            result.append(ch)
            i += 1
            continue
        if in_double or in_single:
            result.append(ch)
            i += 1
            continue
        if ch in ("{", ","):
            result.append(ch)
            i += 1
            new_end, after_colon, ident = _find_identifier(text, i)
            if ident:
                result.append('"')
                result.append(ident)
                result.append('"')
                result.append(":")
                i = after_colon
            continue
        result.append(ch)
        i += 1
    return "".join(result)


def fix_quotes(text: str) -> str:
    text = fix_single_quotes(text)
    text = fix_unquoted_keys(text)
    return text
