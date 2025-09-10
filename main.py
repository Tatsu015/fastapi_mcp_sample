from fastapi import FastAPI, Header, HTTPException
from fastapi_mcp import FastApiMCP


app = FastAPI()


@app.get("/", operation_id="public_endpoint")
def public_endpoint():
    return {"message": "hello! this is public endpoint"}


@app.get("/private", operation_id="private_endpoint")
def private_endpoint(x_token: str = Header(None)):
    if x_token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "hello! this is private endpoint"}


mcp = FastApiMCP(
    app,
    headers=["authorization", "x-token"],  # add any header names you want forwarded
)

mcp.mount_http()
