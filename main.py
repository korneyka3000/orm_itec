from fastapi import FastAPI
from db_conn import connect_to_sqlite
app = FastAPI()



# connect_to_sqlite()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
