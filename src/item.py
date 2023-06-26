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
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if self.__class__.__name__ == 'Item' or 'Phone' and other.__class__.__name__ == 'Item' or 'Phone':
            return self.quantity + other.quantity

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
        else:
            raise ValueError("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open("../src/items.csv", encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                Item.all = []
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        Item(row["name"], row['price'], row['quantity'])
                    else:
                        raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            print('Отсутствует файл item.csv')

    def string_to_number(self):
        int_value = int(self[0])
        return int_value


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

    def __str__(self):
        return self.message
