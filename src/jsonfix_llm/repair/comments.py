import re


def _is_inside_string(line: str, pos: int) -> bool:
    in_double = False
    in_single = False
    escape = False
    for i in range(pos):
        ch = line[i]
        if escape:
            escape = False
            continue
        if ch == "\\":
            escape = True
            continue
        if ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "'" and not in_double:
            in_single = not in_single
    return in_double or in_single


def strip_line_comments(text: str) -> str:
    lines = text.split("\n")
    result = []
    for line in lines:
        comment_pos = -1
        i = 0
        while i < len(line):
            if line[i] == "/" and i + 1 < len(line) and line[i + 1] == "/":
                if not _is_inside_string(line, i):
                    comment_pos = i
                    break
                i += 2
            else:
                i += 1
        if comment_pos >= 0:
            line = line[:comment_pos].rstrip()
        result.append(line)
    return "\n".join(result)


def strip_block_comments(text: str) -> str:
    return re.sub(r"/\*[\s\S]*?\*/", "", text)


def strip_comments(text: str) -> str:
    text = strip_block_comments(text)
    text = strip_line_comments(text)
    return text
