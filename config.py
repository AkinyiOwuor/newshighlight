import os

class Config:
    '''
    General configuration parent class
    '''

    SOURCES_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SEARCH_API_BASE_URL = 'https://newsapi.org/v2/everything?language=en&q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    

class ProdConfig(Config):
    pass


class DevConfig(Config):

    ENV = 'production'
    DEBUG = True

config_option = {
'development':DevConfig,
'production':ProdConfig
}