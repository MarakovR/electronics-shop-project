"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os
from src.item import Item, InstantiateCSVError
import pytest
from src.phone import Phone

test_item = Item("ПК", 50000, 3)


def test_calculate_total_price():
    assert test_item.calculate_total_price() == 150000


def test_apply_discount():
    test_item.apply_discount()
    assert test_item.price == 50000
    Item.pay_rate = 0.2
    test_item.apply_discount()
    assert test_item.price == 10000


def test_name():
    item = Item('Смартфон', 10000, 5)
    assert item.name == 'Смартфон'
    with pytest.raises(ValueError):
        item.name = 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_and_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add_class():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        os.remove("../src/items.csv")
        open("../src/items.csv", encoding='windows-1251')

    with pytest.raises(Exception):
        InstantiateCSVError({'name': 'Смартфон', 'price': '100', 'quantity': None})
