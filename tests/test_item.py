"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def path():
    return f'src/items.csv'


Item.pay_rate = 0.8


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 8000.0


def test_instantiate_from_csv(path):
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 5


def test_name():
    a = Item('abcdefghiklmn', 1, 1)
    a.name = 'abcdefg'
    assert a.name == 'abcdefg'
    a.name = 'abcdefghiklm'
    assert a.name == 'abcdefghik'
    with pytest.raises(AttributeError):
        item.name == "Смартфон"


def test_string_to_number():
    assert Item.string_to_number('123') == 123
    assert Item.string_to_number('123.9') == 123


def test_repr_and_str():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"
    assert str(item) == 'Смартфон'
