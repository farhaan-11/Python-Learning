from database import db
from models import ProductCreate

import json

if db is None:
    raise RuntimeError("MongoDB se connection nahi hai, database.py check karo")

products_collection = db["products"]


def create_product(product: ProductCreate):
    product_dict = product.model_dump()
    result = products_collection.insert_one(product_dict)
    return str(result.inserted_id)



# if __name__ == "__main__":
#     test_product = ProductCreate(
#         name="Test Keyboard",
#         price=499,
#         tags=["electronics", "input"],
#         seller={"name": "TechHub", "city": "Hyderabad"}
#     )
#     new_id = create_product(test_product)

# print("inserted id:", new_id)


# insert many ---
def create_many_products(products: list[ProductCreate]):
    product_dicts = [p.model_dump() for p in products]
    result = products_collection.insert_many(product_dicts)
    return [str(pid) for pid in result.inserted_ids]

if __name__ == "__main__":
    with open("products.json","r") as f:
        data = json.load(f)                     # ye ek list hai (JSON array)
        products_list = [ProductCreate(**item) for item in data]  # har dict ko ProductCreate me convert kiya
        ids_list = create_many_products(products_list)

        print("ids",ids_list)