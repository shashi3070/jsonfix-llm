def auto_close_brackets(text: str) -> str:
    in_string = False
    escape = False
    stack = []

    for char in text:
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
            stack.append("}")
        elif char == "[":
            stack.append("]")
        elif char == "}":
            if stack and stack[-1] == "}":
                stack.pop()
        elif char == "]":
            if stack and stack[-1] == "]":
                stack.pop()

    while stack:
        text += stack.pop()

    return text
