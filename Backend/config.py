class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:fuguator1@localhost/paw_rescue'
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:fuguator1@localhost/paw_rescue'
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}