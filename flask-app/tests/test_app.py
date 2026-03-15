import pytest
from app import main_conversion_function

def test_kg_to_grams():
    assert pytest.approx(main_conversion_function(1, 'kg', 'grams'), rel=0.01) == 1000

def test_grams_to_kg():
    assert pytest.approx(main_conversion_function(1000, 'grams', 'kg'), rel=1e-5) == 1

def test_kg_to_pounds():
    assert pytest.approx(main_conversion_function(1, 'kg', 'pounds'), rel=0.01) == 2.20462

def test_pounds_to_kg():
    assert pytest.approx(main_conversion_function(2.20462, 'pounds', 'kg'), rel=1e-5) == 1

def test_grams_to_pounds():
    assert pytest.approx(main_conversion_function(1000, 'grams', 'pounds'), rel=1e-5) == 2.20462


