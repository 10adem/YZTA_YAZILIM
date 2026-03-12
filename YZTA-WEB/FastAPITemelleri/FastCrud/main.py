from fastapi import FastAPI

app = FastAPI()

#endpoint

@app.get("/")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello_world():
    return {"message": "hello sayfası Hello World"}

#JSON