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
    DB_CONFIG = {
        'host': 'db4free.net',
        'user': 'codocursosg23',
        'password': 'codocursosg23',
        'database': 'codocursosg23',
        'port': 3306
    }
    # Configuración para producción

def get_config():
    env = os.environ.get('MODE', 'development')
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()