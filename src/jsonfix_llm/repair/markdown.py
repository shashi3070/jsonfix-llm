def strip_markdown_fences(text: str) -> str:
    lines = text.split("\n")
    result = []
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        result.append(line)
    return "\n".join(result)
