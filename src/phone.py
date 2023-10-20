from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim >= 1:
            self._number_of_sim = number_of_sim
        else:
            print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
