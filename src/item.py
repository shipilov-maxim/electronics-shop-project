import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


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
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self._name}"

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

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, инициализирующий экземпляры
        класса Item данными из файла csv
        """
        path_csv = BASE_DIR / path
        cls.all = []
        with open(path_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'],
                    row['price'],
                    row['quantity'])

    @staticmethod
    def string_to_number(string):
        if '.' in string:
            dot = string.find('.')
            return int(string[:dot])
        else:
            return int(string)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self._name = name
        else:
            self._name = name[:10]
            print('Exception: Длина наименования товара превышает 10 символов.')
