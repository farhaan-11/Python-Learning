from database import db

products_collection = db["products"]


def create_product(product_data):
    result = products_collection.insert_one(product_data)
    return result.inserted_id



if __name__ == "__main__":
    test_product = {
        "name": "Test Mouse",
        "price": 499,
        "in_stock": True
    }
    new_id = create_product(test_product)

print("inserted id:", new_id)