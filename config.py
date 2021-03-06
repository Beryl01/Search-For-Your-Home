import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_ENABLED = os.environ.get('CSRF_ENABLED')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    UPLOADED_PHOTOS_DEST ='app/static/images'
    
class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = os.environ.get('DEBUG')

class TestingConfig(Config):
    TESTING = True

config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig,
}
