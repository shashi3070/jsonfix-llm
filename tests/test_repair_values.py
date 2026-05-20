from jsonfix_ai.repair.values import fix_values
from tests.fixtures import (
    MISSING_COLONS,
    MISSING_COLONS_EXPECTED,
    MISSING_VALUES,
    MISSING_VALUES_EXPECTED,
)


def test_fix_missing_values():
    result = fix_values(MISSING_VALUES)
    assert result == MISSING_VALUES_EXPECTED


def test_fix_missing_colons():
    result = fix_values(MISSING_COLONS)
    assert result == MISSING_COLONS_EXPECTED


def test_passes_through_valid():
    text = '{"name": "shashi"}'
    assert fix_values(text) == text
