import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 15", 150_000, 9, 1)


def test_repr_and_str(phone):
    assert repr(phone) == "Phone('iPhone 15', 150000, 9, 1)"


def test_number_of_sim(phone):
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
