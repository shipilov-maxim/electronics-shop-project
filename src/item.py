import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл item.csv поврежден"


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
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self._name}"

    def __add__(self, other):
        """Функция сложения остатка у экземпляров класса Item и его наследников"""
        if isinstance(self, Item):
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

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Класс-метод, инициализирующий экземпляры
        класса Item данными из файла csv
        """
        cls.all = []
        try:
            path_csv = BASE_DIR/path
            with open(path_csv, encoding="windows-1251") as file:
                reader = csv.DictReader(file)
                try:
                    for row in reader:
                        cls(name=str(row['name']),
                            price=float(row['price']),
                            quantity=int(row['quantity']))
                except KeyError:
                    raise InstantiateCSVError

        except FileNotFoundError:
            print("Отсутствует файл items.csv")
        except InstantiateCSVError as m:
            print(m.message)

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
            # raise Exception("Длина наименования товара превышает 10 символов.")
