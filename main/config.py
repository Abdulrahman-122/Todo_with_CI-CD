# unhash it for local running or github
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    model_config = SettingsConfigDict(env_file="main/.env", env_file_encoding="utf-8")


settings = Settings()

# this is for act
# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     DATABASE_URL: str
#     SECRET_KEY: str
#     ALGORITHM: str = "HS256"
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
#     model_config = SettingsConfigDict(
#         env_file="main/.secrets", env_file_encoding="utf-8"
#     )


# settings = Settings()
