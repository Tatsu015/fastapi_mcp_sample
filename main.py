from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


app = FastAPI()


@app.get("/", operation_id="public_endpoint")
def public_endpoint():
    return {"message": "hello! this is public endpoint"}


@app.get("/private", operation_id="private_endpoint")
def private_endpoint():
    print("aaa")
    return {"message": "hello! this is private endpoint"}


mcp = FastApiMCP(app)
mcp.mount()
