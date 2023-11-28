# app/config.py

import os

class Config:
     # Configuración común a todos los entornos
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_CONFIG = {
        'host': os.environ.get('DB_HOST'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'database': os.environ.get('DB_DATABASE'),
        'port': os.environ.get('DB_PORT')
    }

class ProductionConfig(Config):
    DEBUG = False
    # Configuración para producción

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()