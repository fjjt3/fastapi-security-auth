from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List
from uuid import UUID
from datetime import date, datetime, time, timedelta

class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_time: datetime
    repeat_time: time
    excecute_after: timedelta

class Profile (BaseModel):
    name: str
    email: str
    age: int

class Image(BaseModel):
    url:HttpUrl
    name:str

class Product(BaseModel):
    name: str
    price: int = Field(title="Price of the item", description="price of item added")
    discount: int
    discounted_price: float 
    tags:Set[str] = [] 
    image: List[Image]

    class Config:
        json_schema_extra = {
            "example": {
            "name":"Phone",
            "price":100,
            "discount":10,
            "discounted_price":0,
            "tags":["electronics", "computers"],
            "image":[
                {"url":"https://www.example.com/image.jpg}",
                    "name": "phone image"},
                {"url":"https://www.example.com/image1.jpg}",
                    "name": "monitor image"}
                ]
        }
    }

class Offer(BaseModel):
    name: str
    description: str
    price: int
    products: List[Product]


class User(BaseModel):
    name: str
    email: str

app = FastAPI()

@app.post('/login')
def login(username: str = Form(...), password:str = Form(...)):
    return{"username": username}

@app.post('/addevent')
def addevent(event: Event):
    return event

@app.post('/addofeer')
def addofer(offer: Offer):
    return{offer}

@app.post('/purchase')
def purchase(user:User, product:Product):
    return {"user": user ,"product": product}


@app.post("/addproduct/{product_id}")
def add_product(product:Product, product_id:int, category:str):
    product.discounted_price = (product.price * product.discount)/100
    return {"product_id": product_id ,"product": product, 'category': category}


@app.post('/adduser')
def add_user(profile:Profile):
    return profile