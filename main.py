from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return 'Hallo Welt'

@app.get('/user/{username}')
def profile(username: str):
    return {f'This is a profile page for use: {username}'}

@app.get('/products')
def products(id=1, price=0):
    return {f'Product with an id: {id} and price {price}'}

@app.get('/profile/{userid}/comments')
def profile(userid:int, commentid:int):
    return {f'Profile page for user id{userid} and comment with {commentid}'}