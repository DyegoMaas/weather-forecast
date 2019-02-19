from abc import ABC


class Config(ABC):
    DEBUG = False
    TESTING = False
    OPEN_WEATHER_APP_ID = 'eb8b1a9405e659b2ffc78f0a520b1a46'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
