class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def __float__(self) -> float:
        return self.price

    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def __add__(self, other):
        cart_new = ShoppingCart()
        if self.__eq__(other):
            pass
        else:
            cart_new.add_product(self)
            cart_new.add_product(other)
        return cart_new

    def get_total(self, quantity) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:

    def __init__(self):
        self.list_product = []
        self.list_quantity = []

    def __repr__(self) -> str:
        return "Корзина"

    def __float__(self) -> float:
        return self.get_total()

    def add_product(self, product_name, quantity: float = 1) -> None:
        if len(self.list_product) == 0:
            self.list_product.append(product_name)
            self.list_quantity.append(quantity)
        else:
            for i in range(len(self.list_product)):
                if product_name.__eq__(self.list_product[i]):
                    self.list_quantity[i] += quantity
                    break
                elif i != len(self.list_product) - 1:
                    continue
                else:
                    self.list_product.append(product_name)
                    self.list_quantity.append(quantity)
                    break

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.list_product = self.list_product[:]
        new_cart.list_quantity = self.list_quantity[:]
        for i in range(len(new_cart.list_product)):
            for j in range(len(other.list_product)):
                if other.list_product[j].__eq__(new_cart.list_product[i]):
                    new_cart.list_quantity[i] += other.list_quantity[j]
                    break
                elif j != len(new_cart.list_product) - 1:
                    continue
                else:
                    new_cart.list_product.append(other.list_product[j])
                    new_cart.list_quantity.append(other.list_quantity[j])
                    break
        return new_cart

    def get_total(self) -> float:
        sum_cart = 0
        for product, quantity in zip(self.list_product, self.list_quantity):
            sum_cart += product.get_total(quantity)
        return round(sum_cart, 2)
