# app/config.py

import os

class Config:
     # Configuración común a todos los entornos
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_FOLDER = 'C:\\Users\\ezequ\\Desktop\\Coding\\CodoACodo\\Committt\\app\\assets\\img'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
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
        'host': 'sql10.freemysqlhosting.net',
        'user': 'sql10668517',
        'password': 'z8eerYDapW',
        'database': 'sql10668517',
        'port': int(3306)
    }
    # Configuración para producción

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()