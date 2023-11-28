from fastapi import APIRouter, Depends, status, HTTPException
from ..import schemas, database, models
from ..database import get_db
from passlib.context import CryptContext
from sqlalchemy.orm import Session

router = APIRouter(tags=['Login'])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect username or password')
    # Verify the hashed password with the entered one
    if not pwd_context.verify(request.password, seller.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect password')
    # Gen JWT token
    
    return request