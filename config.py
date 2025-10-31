import os

class Config:
    """Configuración base de la aplicación"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Configuración de la base de datos MySQL
    DB_CONFIG = {
        'host': os.environ.get('DB_HOST') or 'localhost',
        'user': os.environ.get('DB_USER') or 'root',
        'password': os.environ.get('DB_PASSWORD') or 'Ericko11$',
        'database': os.environ.get('DB_NAME') or 'demo_servicios_db',
        'port': int(os.environ.get('DB_PORT') or 3306)
    }
    
    # Configuración de la aplicación
    DEBUG = os.environ.get('FLASK_DEBUG') or True
    
    # Usuario admin por defecto (cambiar en producción)
    DEFAULT_ADMIN_USER = 'admin'
    DEFAULT_ADMIN_PASSWORD = 'admin123'