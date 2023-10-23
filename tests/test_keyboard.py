import pytest
from src.keyboard import Keyboard, MixinKeyboard


@pytest.fixture
def keyboard():
    return Keyboard('WOW KB 142288', 6900, 3)


def test_language(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = 2


def test_change_lang(keyboard):
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
