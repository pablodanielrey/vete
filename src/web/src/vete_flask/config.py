
from vete_models import config

class Config(config.Config):
    
    def __init__(self):
        self.version = '0.0.1'
        self.dbhost = '0.0.0.0'
        self.dbport = 5432
        self.dbpassword = 'vete'
        self.dbuser = 'vete'
        self.dbname = 'vete'


def configure(binder):
    _config = Config()
    binder.bind(config.Config, _config)
    binder.bind(Config, _config)

