import os

class Config:
    '''
    General configuration parent class
    '''
    #NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey=18511174a077429aaaeaee76c5574ee9'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}