import pytest

from project import validate_city

def test_validate_city_correct():
    assert validate_city("Barcelona") == True
    assert validate_city("Sant Vicenç dels Horts") == True
    assert validate_city("Scranton") == True

def test_validate_city_errors():
    with pytest.raises(ValueError):
        validate_city("abc123")
        validate_city("BarDrid")
        validate_city("Inlkin")
