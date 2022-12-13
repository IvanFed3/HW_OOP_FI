class Product:
    def __init__(self, name: str, price: float, unit: float = 1) -> None:
        self.name = name
        self.price = price
        self.unit = unit

    def __repr__(self) -> str:
        return self.name

    def __float__(self) -> float:
        return self.price

    def __eq__(self, other) -> bool:
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False

    def __add__(self, other):
        if self.__eq__(other):
            self.unit += other.unit
            return self
        else:
            if not isinstance(other, Product):
                raise TypeError("unsupported operand type(s) for +")
            cart_new = ShoppingCart()
            cart_new.add_product(self)
            cart_new.add_product(other)
            return cart_new

    def get_total(self, quantity: float = None) -> float:
        if quantity is None:
            quantity = self.unit
        return round(self.price * quantity, 2)


class ShoppingCart:

    def __init__(self):
        self.products: list[Product] = []
        self.quantities: list[Product] = []

    def __repr__(self) -> str:
        return "Корзина"

    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return self.products == other.products
        return False

    def __float__(self) -> float:
        return self.get_total()

    def add_product(self, product, quantity: float = None) -> None:
        if quantity is None:
            quantity = product.unit
        if product in self.products:
            id_product = self.products.index(product)
            self.quantities[id_product] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def __add__(self, other):
        new_cart = ShoppingCart()
        new_cart.products = self.products[:]
        new_cart.quantities = self.quantities[:]
        if isinstance(other, ShoppingCart):
            for product_1 in other.products:
                if product_1 in new_cart.products:
                    for product, quantity in zip(other.products, other.quantities):
                        new_cart.add_product(product, quantity)
                else:
                    id_product_2 = other.products.index(product_1)
                    new_cart.products.append(other.products[id_product_2])
                    new_cart.quantities.append(other.quantities[id_product_2])
        else:
            new_cart.add_product(other)
        return new_cart

    def get_total(self) -> float:
        sum_cart = 0
        for product, quantity in zip(self.products, self.quantities):
            sum_cart += product.get_total(quantity)
        return round(sum_cart, 2)