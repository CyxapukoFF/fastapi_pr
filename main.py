from typing import Union
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def health():
    return {"status": "OK"}

