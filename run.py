import os
from app import create_app

# Usar configuración de producción si está en Render
if os.environ.get('RENDER'):
    from config_production import ProductionConfig
    app = create_app(ProductionConfig)
else:
    app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
