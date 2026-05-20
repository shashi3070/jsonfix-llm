import re


def fix_missing_values(text: str) -> str:
    text = re.sub(r'(")\s*:\s*,', r"\1: null,", text)
    text = re.sub(r'(")\s*:\s*\}', r"\1: null}", text)
    return text


def fix_missing_colons(text: str) -> str:
    text = re.sub(r'(")\s+("(?=[^:]*:))', r"\1: \2", text)
    return text


def fix_values(text: str) -> str:
    text = fix_missing_colons(text)
    text = fix_missing_values(text)
    return text
