from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


app = FastAPI()


@app.get("/")
def public_endpoint():
    return {"message": "public endpoint"}


@app.get("/private")
def private_endpoint():
    print("aaa")
    return {"message": "private endpoinT"}


mcp = FastApiMCP(app)
mcp.mount()
