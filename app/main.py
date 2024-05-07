from fastapi import FastAPI 
from app.api.v1.user import router

app = FastAPI()

@app.get("/")
def red_root():
    return {"Status": "OK"}

app.include_router(router)