from datetime import datetime
from datetime import timedelta
from jose import jwt
from passlib.context import CryptContext
from main.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# make sure to use bcrypt algorith
# in case you used another one deprecated will add
# migeration correctly.
def hash_password(password: str):
    return pwd_context.hash(password)


def varify_password(plain_pass, hashed_password):
    return pwd_context.verify(plain_pass, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token
