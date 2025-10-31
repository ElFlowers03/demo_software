from flask import Flask
from config import Config

def create_app(config_class=Config):
    """Factory para crear la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Registrar blueprints
    from app.routes.home import home_bp
    from app.routes.pos import pos_bp
    from app.routes.encuesta import encuesta_bp
    from app.routes.admin import admin_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(pos_bp, url_prefix='/pos')
    app.register_blueprint(encuesta_bp, url_prefix='/encuesta')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    return app