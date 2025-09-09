from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def public_endpoint():
    return {"message": "public endpoint"}


@app.get("/private")
def private_endpoint():
    print("aaa")
    return {"message": "private endpoint"}
