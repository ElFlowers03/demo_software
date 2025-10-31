from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models import UsuarioAdminModel, VentaModel, EncuestaModel
from functools import wraps

admin_bp = Blueprint('admin', __name__)

def login_required(f):
    """Decorador para proteger rutas que requieren autenticación"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión para acceder', 'warning')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/login')
def login():
    """Página de login"""
    if 'user_id' in session:
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/login.html')

@admin_bp.route('/login', methods=['POST'])
def login_post():
    """Procesa el login"""
    usuario = request.form.get('usuario')
    password = request.form.get('password')
    
    if not usuario or not password:
        flash('Usuario y contraseña son requeridos', 'error')
        return redirect(url_for('admin.login'))
    
    user = UsuarioAdminModel.authenticate(usuario, password)
    
    if user:
        session['user_id'] = user['id']
        session['usuario'] = user['usuario']
        session['nombre'] = user['nombre_completo']
        flash('Bienvenido al panel administrativo', 'success')
        return redirect(url_for('admin.dashboard'))
    else:
        flash('Usuario o contraseña incorrectos', 'error')
        return redirect(url_for('admin.login'))

@admin_bp.route('/logout')
def logout():
    """Cierra la sesión"""
    session.clear()
    flash('Has cerrado sesión exitosamente', 'info')
    return redirect(url_for('home.index'))

@admin_bp.route('/')
@login_required
def dashboard():
    """Dashboard principal del administrador"""
    # Obtener estadísticas de ventas
    estadisticas_ventas = VentaModel.get_estadisticas()
    ventas_recientes = VentaModel.get_all()[:5]  # Últimas 5 ventas
    
    # Obtener estadísticas de encuestas
    estadisticas_encuestas = EncuestaModel.get_estadisticas()
    encuestas_recientes = EncuestaModel.get_all()[:5]  # Últimas 5 encuestas
    
    return render_template(
        'admin/dashboard.html',
        estadisticas_ventas=estadisticas_ventas,
        ventas_recientes=ventas_recientes,
        estadisticas_encuestas=estadisticas_encuestas,
        encuestas_recientes=encuestas_recientes
    )

@admin_bp.route('/ventas')
@login_required
def ventas():
    """Página de reportes de ventas"""
    todas_ventas = VentaModel.get_all()
    estadisticas = VentaModel.get_estadisticas()
    return render_template('admin/ventas.html', ventas=todas_ventas, estadisticas=estadisticas)

@admin_bp.route('/encuestas')
@login_required
def encuestas():
    """Página de reportes de encuestas"""
    todas_encuestas = EncuestaModel.get_all()
    estadisticas = EncuestaModel.get_estadisticas()
    return render_template('admin/encuestas.html', encuestas=todas_encuestas, estadisticas=estadisticas)

@admin_bp.route('/api/estadisticas')
@login_required
def api_estadisticas():
    """API para obtener estadísticas en formato JSON"""
    ventas = VentaModel.get_estadisticas()
    encuestas = EncuestaModel.get_estadisticas()
    
    return jsonify({
        'ventas': ventas if ventas else [],
        'encuestas': encuestas if encuestas else []
    })