import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    AUTHOR: str
    
    ROOT_PATH: Path = Path(__file__).parent.parent
    
    PG_DB: str
    PG_HOST: str
    PG_PORT: int
    PG_USER: str
    PG_PASSWORD: str
    
    model_config = SettingsConfigDict(
            env_file = ROOT_PATH /'.env', 
            env_file_encoding = 'utf-8'
        )

settings = Settings()