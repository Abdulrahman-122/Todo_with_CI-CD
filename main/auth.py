from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import session
from main.database import get_db
from main.models import User
from main.schemas import UserCreate, UserResponse, UserLogin, Token
from main.security import hash_password, varify_password, create_access_token

router1 = APIRouter(prefix="/auth", tags=["Authentication"])


@router1.post("/register", response_model=UserResponse, status_code=201)
def register_user(user: UserCreate, db: session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Oops user already exists")
    hashed_password = hash_password(user.password)
    new_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router1.post("/login", response_model=Token)
def login(credential: UserLogin, db: session = Depends(get_db)):
    user = db.query(User).filter(User.email == credential.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password!!")

    if not varify_password(credential.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password!!")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
