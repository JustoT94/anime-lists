import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration pulling core settings from the environment."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "fallback-secret-key")
    JWT_SECRET = os.environ.get("JWT_SECRET", "fallback-jwt-secret")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration using environment DATABASE_URL or falling back to local SQLite."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///dev.db")

class TestingConfig(Config):
    """Testing configuration for unit tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL", "sqlite:///test.db")

class ProductionConfig(Config):
    """Production configuration requiring a DATABASE_URL."""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}