import os

class Settings:
    PROJECT_NAME: str = "Smart Vision"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///../smart_vision.db")  # Example for SQLite

settings = Settings()
