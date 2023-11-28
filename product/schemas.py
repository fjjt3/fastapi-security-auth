from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: int

class DisplaySeller(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True

class DisplayProduct(BaseModel):
    name: str
    description: str
    seller: DisplaySeller
        
    class Config:
        from_attributes = True

class Seller(BaseModel):
    username: str
    email: str
    password: str

class Login(BaseModel):
    username: str
    password: str
