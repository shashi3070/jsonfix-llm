import re


def _extract_fenced(text: str, language: str | None) -> list[str]:
    if language:
        lang_pattern = re.escape(language)
        pattern = rf"```{lang_pattern}\s*\n(.*?)\n```"
    else:
        pattern = r"```\w*\s*\n(.*?)\n```"
    return re.findall(pattern, text, re.DOTALL)


def _extract_xml(text: str, tag: str) -> list[str]:
    pattern = rf"<{tag}>(.*?)</{tag}>"
    return re.findall(pattern, text, re.DOTALL)


def _extract_indented(text: str) -> list[str]:
    blocks = []
    current: list[str] = []
    for line in text.split("\n"):
        if line.startswith("    ") or line.startswith("\t"):
            current.append(line.lstrip())
        elif current:
            blocks.append("\n".join(current))
            current = []
    if current:
        blocks.append("\n".join(current))
    return blocks


def _extract_inline(text: str) -> list[str]:
    return re.findall(r"`([^`]+)`", text)


def extract_code(text: str, language: str | None = None, all: bool = False) -> str | list[str]:
    blocks = _extract_fenced(text, language)
    if not blocks:
        blocks = _extract_xml(text, "code")
    if not blocks:
        blocks = _extract_xml(text, "pre")
    if not blocks:
        blocks = _extract_indented(text)
    if not blocks:
        blocks = _extract_inline(text)
    if all:
        return blocks
    return blocks[0] if blocks else text
