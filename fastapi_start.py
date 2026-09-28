from fastapi import FastAPI, Request
from mockData import products

app = FastAPI()

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
    return products

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