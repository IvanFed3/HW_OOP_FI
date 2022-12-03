class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return self.name

    def get_total(self, quantity) -> float:
        return round(self.price * quantity, 2)


class ShoppingCart:
    list_shopping_cart_product = []
    list_shopping_cart_quantity = []

    def add(self, product_name, quantity: int = 1) -> None:
        self.list_shopping_cart_product.append(product_name)
        self.list_shopping_cart_quantity.append(quantity)
        print(self.list_shopping_cart_product)

    def get_total(self) -> float:
        sum_shopping_cart = 0
        for i in range(len(self.list_shopping_cart_product)):
            sum_shopping_cart += self.list_shopping_cart_product[i].get_total(self.list_shopping_cart_quantity[i])
        print(sum_shopping_cart)
        return round(sum_shopping_cart, 2)
