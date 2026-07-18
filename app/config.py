# reads .env, parses it, converts it to python objects,
# validates the values and makes them available to rest
# of the application.

# imports
from pydantic_settings import BaseSettings, SettingsConfigDict

#settings class
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding = "utf-8")

#global obj
settings = Settings()