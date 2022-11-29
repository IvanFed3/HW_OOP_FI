class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self) -> None:
        print(f'{self.name} {self.price*self.quantity}')


class ShoppingCart:
    list = []
    def add(self, name, price, quantity) -> None:
        self.list.append([name, price, quantity])

    def get_total (self) -> None:
        sum_1 = 0
        for i in self.list:
            sum_1 += i[1]*i[2]
        print(sum_1)