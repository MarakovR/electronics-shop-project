import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return

    @property
    def name_prod(self):
        return self.__name

    @name_prod.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
            return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        with open("../src/items.csv", encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            Item.all = []
            for row in reader:
                Item(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(value):
        int_value = int(value[0])
        return int_value
