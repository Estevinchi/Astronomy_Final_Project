import pytest

from project import validate_city, validate_date

def test_validate_city_correct():
    assert validate_city("Barcelona") == True
    assert validate_city("Sant Vicenç dels Horts") == True
    assert validate_city("Scranton") == True

def test_validate_city_errors():
    with pytest.raises(ValueError):
        validate_city("abc123")
        validate_city("BarDrid")
        validate_city("Inlkin")

def test_validate_date_correct():
    assert validate_date("2022/12/01 20:00") == True
    assert validate_date("2025/02/13 03:30") == True
    assert validate_date("1990/03/30 2:01") == True
    

def test_validate_date_errors():
    with pytest.raises(ValueError):
        validate_date("2022 12 01 20:00")
        validate_date("abcd/ef/gh ij:kl")
        validate_date("2025-12-1 00:00")
        validate_date("2022/02/31 20:00")