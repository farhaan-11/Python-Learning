from fastapi import FastAPI

app = FastAPI()

#  for server start uvicorn fastapi_start:app --reload and fastapi dev fastapi_start.py   

@app.get('/')
def home():
    return " Hii from server"


@app.get("/about")
def about():
    return " mai fast api server hu tum apna route bna skte ho "