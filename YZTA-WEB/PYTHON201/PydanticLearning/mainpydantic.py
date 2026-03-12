from pydantic import BaseModel

class ProductPydantic(BaseModel):
    name: str
    price: float
    in_stock: bool

if __name__ == "__main__":
    #ornek_product = ProductPydantic("Ornek", 100, True)
    #ornek_product2 = ProductPydantic("Ornek", 100, 20)
    #print(ornek_product.in_stock)
    #print(ornek_product2.in_stock)

    external_data = {
        "name": "Laptop",
        "price": "999.99",
        "in_stock": "True",
    }

    product = ProductPydantic(
        name = external_data.get("name"),
        price = external_data.get("price"),
        in_stock = external_data.get("in_stock")
    )

    print(type(product.name))
    print(type(product.price))
    print(type(product.in_stock))