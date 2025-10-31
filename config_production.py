import os
from config import Config

class ProductionConfig(Config):
    """Configuración para producción en Render"""
    DEBUG = False
    TESTING = False
    
    # Render proporciona estas variables de entorno automáticamente
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24).hex()
    
    # Configuración de base de datos para Render (MySQL)
    DB_CONFIG = {
        'host': os.environ.get('DB_HOST'),
        'user': os.environ.get('DB_USER'),
        'password': os.environ.get('DB_PASSWORD'),
        'database': os.environ.get('DB_NAME'),
        'port': int(os.environ.get('DB_PORT', 3306))
    }
