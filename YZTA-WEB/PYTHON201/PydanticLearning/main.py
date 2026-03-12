class Product:

    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == "__main__":
    ornek_product = Product("Ornek", 100, True)
    ornek_product2 = Product("Ornek", 100, 20)
    print(ornek_product.in_stock)
    print(ornek_product2.in_stock)

    external_data = {
        "name": "Laptop",
        "price": "999.99",
        "in_stock": "True",
    }

    product = Product(
        name = external_data.get("name"),
        price = external_data.get("price"),
        in_stock = external_data.get("in_stock")
    )

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))