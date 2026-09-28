from fastapi import FastAPI

app = FastAPI()

#  for server start uvicorn fastapi_start:app --reload

@app.get("/health")
def health():
    return {"status": "server start ho gya ab check kro"}