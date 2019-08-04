from fastapi import FastAPI

from app.schema import User


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello world"}


@app.post("/age/", response_model=User)
def age_user(user: User):
    user.age += 1
    return user
