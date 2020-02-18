from dotenv import load_dotenv
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)


class Config:
    CSRF_ENABLED = True
    SECRET_KEY = 'your-very-very-secret-key'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///flask_teste'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_ECHO = True


class Production(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'your-production-database-url')
