from database import db
from models import ProductCreate, ProductOut, ProductUpdate
from bson import ObjectId
from pymongo import ReturnDocument

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

# if __name__ == "__main__":
#     with open("products.json","r") as f:
#         data = json.load(f)                     # ye ek list hai (JSON array)
#         products_list = [ProductCreate(**item) for item in data]  # har dict ko ProductCreate me convert kiya
#         ids_list = create_many_products(products_list)

#         print("ids",ids_list)

#  get product all -----

def format_product(doc):
    doc["_id"] = str(doc["_id"])
    return doc

def get_all_products():
    cursor = products_collection.find()          # Cursor milta hai, data nahi
    data = [format_product(doc) for doc in cursor]  # cursor ko loop karke actual documents nikale
    return data


# if __name__ == "__main__":
#     all_products = get_all_products()
#     print("data", all_products)
#     print(f"data type : {type(all_products)}")


def get_single_product(product_id):
    if( ObjectId.is_valid(product_id)):
        data= products_collection.find_one({"_id": ObjectId(product_id)})
        if data is None:
          return None
        else:
         return format_product(data)    
    else:
        return {"message":"product id is invalid "}     


# if __name__ == "__main__":
#     one_product = get_single_product("6abbe0e74ac74ee4ed9c8d30")
#     print("one_product", one_product)
#     print(f"data type : {type(one_product)}")


def update_product(product_id,data_for_update:ProductUpdate):
    # print(f"before check data type : {type(data_for_update)}\n data:{data_for_update}")
    if not ObjectId.is_valid(product_id):
            return {"message":"product id Invalid"}
    update_data = data_for_update.model_dump(exclude_unset=True)
    
    # print(f"after check data type : {type(update_data)} \n data:{update_data}")

    if not update_data:
     return None
    

    after_update_data= products_collection.find_one_and_update(
        {"_id": ObjectId(product_id)},
       {"$set": update_data},
       return_document=ReturnDocument.AFTER
    )

    if after_update_data is None:
        return None
    else:
        return {"message":"data not found","data":format_product(after_update_data)}

ise_update_krna_hai = ProductUpdate(price=91001)

# if __name__ == "__main__":

#     one_product = update_product("6abbe0e74ac74ee4ed9c8d30",ise_update_krna_hai)
#     print("one_product", one_product)
#     print(f"data type : {type(one_product)}")   
# 
# 

#  delete method---

def delete_product(product_id):
     if not ObjectId.is_valid(product_id):
                 return {"message":"product id Invalid"}
     deleted_doc= products_collection.find_one_and_delete({"_id": ObjectId(product_id)})

     if deleted_doc is None:
         return {"message":"document not found"}
     else:
         return {"message":"documnet deleted","documnet":format_product(deleted_doc)}


if __name__ == "__main__":

    one_product = delete_product("6abbe0e74ac74ee4ed9c8d30")
    print("one_product", one_product)
    print(f"data type : {type(one_product)}")