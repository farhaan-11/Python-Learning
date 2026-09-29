from fastapi import FastAPI, Request
from mockData import products

import json
from pathlib import Path


from pydantic import BaseModel, Field, ValidationError, EmailStr

from typing import List,Dict, Optional, Annotated


app = FastAPI()

import json
from mockData import products

with open("products.json", "w") as f:
    json.dump(products, f, indent=2)

DATA_FILE = Path(__file__).parent / "products.json"
print("data file",DATA_FILE)

#  for server start uvicorn fastapi_start:app --reload and fastapi dev fastapi_start.py   

@app.get('/')
def home():
    return " Hii from server"


@app.get("/about")
def about():
    return " mai fast api server hu tum apna route bna skte ho "


@app.get('/products')
def product():
    # return products
    # big = []
    # for p in products:
    #  if p["price"] > 1200:
    #   big.append(p)
    # return [p for p in products if p["price"]>1200]    
    # return products
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# path params --

@app.get("/product/{product_id}")
def one_product(product_id : int):
    for single_product in products:
       if single_product.get("id") == product_id:
           return single_product
    return {"error":"product not found"}


#  query paramteres
@app.get("/product")
def one_product(name):
    for p in products:
        if(p.get("name")==name):
            return {"product found": p}

    
    return {"message":"product not found"}

# query parameter one more example

@app.get("/greet")
def greet_to_user(request:Request):
    request_body=dict(request.query_params)
    print("request",request_body["age"])
    # print("request type", type(request_body))
    return {"request":f"hii {request_body.get("name")} you are {request_body['age']} old!."}




# pahle file read krte hai 

with open("products.json", "r") as f:
    product_data=json.load(f)


class Product(BaseModel):

    id: int = 100
    name: Optional[str] = None
    category: Optional[str] = None
    brand: Optional[str] = None
    price: int = 399
    discount_percent: int = 15
    stock: int = 10
    in_stock: bool = True
    rating: float = 3.5
    tags: List[str]
    seller: Dict[str, str]
    # "seller": {
    #   "name": "FitZone",
    #   "city": "Pune"
    # }
  

# post request
@app.post("/products")
def insert_product(data:Product):
    payload_data=dict(data)

    print(type(payload_data))
    print(f"payload data {payload_data}")

    products.append(payload_data)

    with open("products.json","w") as f:
        json.dump(products, f, indent=2)

    return {"message ": " product created succesfully", "data":products}



@app.put("/products/{product_id}")
def update_products(data:Product, product_id: int):
    payload_data=dict(data)
    print(f"update product data : {payload_data}")
   
    print("product_id",product_id)
    for idx, p in enumerate(products):
        print("running")
        if(p["id"]==product_id):
            products[idx] = payload_data
    with open ("products.json","a") as f:
        json.dump(products, f, indent=2)        
    return {"message":" product updated", "updated data":products}


























# def write_products(products):
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(products, f, indent=2)


# def read_products():
#     with open(DATA_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)


# @app.post("/products", status_code=201)
# def add_product(body: dict):
#     products = read_products()
#     body.pop("id", None)
#     new_id = max((p["id"] for p in products), default=0) + 1
#     new_product = {"id": new_id, **body}
#     products.append(new_product)
#     write_products(products)
#     return {"message":"new product created ", "data":new_product}
