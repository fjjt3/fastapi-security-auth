from fastapi import FastAPI
from .import models
from .database import engine
from .routers import product, seller, login

app = FastAPI(
    title="Products API",
    description="Get details of products",
    terms_of_service="http://www.google.com",
    contact ={"Developer_name":"Fran Jimenez"},
    # docs_url="/documentation"
)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)

models.Base.metadata.create_all(engine)



