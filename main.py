from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


app = FastAPI()


@app.get("/", operation_id="public_endpoint")
def public_endpoint():
    return {"message": "public endpoint"}


@app.get("/private", operation_id="private_endpoint")
def private_endpoint():
    print("aaa")
    return {"message": "private endpoinT"}


mcp = FastApiMCP(app)
mcp.mount()
