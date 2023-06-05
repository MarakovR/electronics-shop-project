"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

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
    item.name = 'СуперСмартфон'
    assert item.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
