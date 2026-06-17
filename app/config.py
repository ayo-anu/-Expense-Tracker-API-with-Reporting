from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

    TOKEN_ISSUER:str
    TOKEN_AUDIENCE:str
    
    APP_ENV:str


    class Config:
        env_file = ".env"

        
settings = Settings()
