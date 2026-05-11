from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    ALLOWED_GROUP_ID: int
    CHECK_INTERVAL_HOURS: int = 6
    STEAM_COUNTRY_CODE: str = "UZ"
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()