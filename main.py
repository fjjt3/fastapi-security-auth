from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return 'Hallo Welt'

# id here is a path parameter
@app.get("/property/{id}")
def property(id: int):
    return {f' This is a property page for property {id}'}

@app.get('/profile/{username}')
def profile(username: str):
    return {f'This is a profile page for use: {username}'}

@app.get('/movies')
def movies():
    return {'movie list':{'movie 1','movie 2','movie 3'}}
