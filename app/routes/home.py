from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    """Página principal del portafolio"""
    servicios = [
        {
            'titulo': 'Sistema Punto de Venta (POS)',
            'descripcion': 'Sistema completo de punto de venta con gestión de inventario, ventas y reportes en tiempo real.',
            'icono': 'shopping-cart',
            'url': '/pos',
            'demo': True
        },
        {
            'titulo': 'Encuestas de Satisfacción',
            'descripcion': 'Plataforma para capturar feedback de clientes con análisis de resultados y métricas de satisfacción.',
            'icono': 'clipboard-check',
            'url': '/encuesta',
            'demo': True
        },
        {
            'titulo': 'Panel Administrativo',
            'descripcion': 'Dashboard con reportes, gráficos y estadísticas para la toma de decisiones empresariales.',
            'icono': 'chart-bar',
            'url': '/admin',
            'demo': True
        },
        {
            'titulo': 'Sitios Web Personalizados',
            'descripcion': 'Desarrollo de sitios web corporativos, landing pages y portales empresariales a medida.',
            'icono': 'browser',
            'url': '#contacto',
            'demo': False
        }
    ]
    
    return render_template('home.html', servicios=servicios)

@home_bp.route('/contacto')
def contacto():
    """Página de contacto"""
    return render_template('contacto.html')