class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def get_total(self, quantity) -> float:
        return self.price*quantity


class ShoppingCart:
    list = []

    def add(self, product, quantity: int = 1) -> None:
        self.list.append([product.name, quantity, product.price])

    def get_total(self) -> float:
        sum_1 = 0
        for i in self.list:
            sum_1 += i[1]*i[2]
        return sum_1
    
