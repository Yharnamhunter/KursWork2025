import pytest
from django.core.exceptions import ValidationError
from ..validators import MinimumLengthValidator, UppercaseValidator, SpecialCharacterValidator, NumericValidator

def test_minimum_length_validator():
    v = MinimumLengthValidator(min_length=5)
    with pytest.raises(ValidationError):
        v.validate('abc', None)
    v.validate('abcde', None)

def test_uppercase_validator():
    v = UppercaseValidator()
    with pytest.raises(ValidationError):
        v.validate('lowercase', None)
    v.validate('HasUpper', None)

def test_numeric_validator():
    v = NumericValidator()
    with pytest.raises(ValidationError) as exc:
        v.validate("NoDigitsHere", user=None)
    assert "одну цифру" in str(exc.value)
    v.validate("Contains1digit", user=None)
    assert "одну цифру" in v.get_help_text()

def test_special_character_validator():
    v = SpecialCharacterValidator()
    with pytest.raises(ValidationError) as exc:
        v.validate("Abc123", user=None)
    assert "специальный символ" in str(exc.value)
    help_text = v.get_help_text()
    assert "специальных символов" in help_text
    v.validate("Hello!", user=None)
