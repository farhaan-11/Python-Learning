from fastapi import FastAPI,HTTPException,Query
from database import db
from bson import ObjectId
from pymongo import ReturnDocument, ASCENDING , DESCENDING
from typing import Annotated
import json

from models import ProductListResponse, ProductCreate, ProductOut, ProductUpdate, ProductOutQuery,ProductFilter


if db is None:
    raise RuntimeError("MongoDB se connection nahi hai, database.py check karo")

products_collection = db["products"]



app=FastAPI()


@app.get("/health")
def health():
    return {"message":'server is running'}


#  get all products----

@app.get('/products', response_model= list[ProductOut])
def get_products():
    data= products_collection.find()
    # print(f"data : {data}")
    # print(f"data type : {type(data)}")

    return  list(data)

#  get single products ---

@app.get('/products/{product_id}', response_model=ProductOut)
def get_single_product(product_id:str):

    if not  ObjectId.is_valid(product_id):
        # return {"message":"product id is not valid"}
        raise HTTPException(status_code=400, detail="product id invalid hai")

    # print(f"product id type  : {type(product_id)}")

    result = products_collection.find_one({"_id":ObjectId(product_id)})

    if result is None:
        # return {"message":"product not found"}
        raise HTTPException(status_code=404, detail="product nahi mila")

    return result

#  get document vased on query parameter

def build_mongo_query(filters: ProductFilter) -> dict:
    data = filters.model_dump(exclude_none=True, exclude={"sort_by_price"})

    print(f" data : {data}")

    min_price = data.pop("min_price", None)
    max_price = data.pop("max_price", None)

    if min_price is not None or max_price is not None:
        data["price"] = {}
        if min_price is not None:
            data["price"]["$gte"] = min_price
        if max_price is not None:
            data["price"]["$lte"] = max_price

    return data


@app.get('/query_products',response_model=ProductListResponse)
def get_products_by_query(filters: Annotated[ProductFilter, Query()]):
    # print(f"filters : {filters}")
    query = build_mongo_query(filters)
    cursor = products_collection.find(query)
    if filters.sort_by_price:
        direction = ASCENDING if filters.sort_by_price == 'asc' else DESCENDING
        cursor= cursor.sort("price", direction)
    products = list(cursor) 
    total = products_collection.count_documents(query)

    return {
        "message": "products found" if products else "products not found",
        "total": total,
        "data": products,
    }   


    return 
 
    # return {"message" : " api is working"}
