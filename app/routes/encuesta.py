from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import EncuestaModel

encuesta_bp = Blueprint('encuesta', __name__)

@encuesta_bp.route('/')
def index():
    """Página principal de encuesta"""
    return render_template('encuesta/index.html')

@encuesta_bp.route('/enviar', methods=['POST'])
def enviar():
    """Procesa y guarda la encuesta"""
    calificacion = request.form.get('calificacion', type=int)
    comentario = request.form.get('comentario', '')
    servicio = request.form.get('servicio', 'General')
    
    if not calificacion or calificacion < 1 or calificacion > 10:
        flash('Por favor selecciona una calificación válida', 'error')
        return redirect(url_for('encuesta.index'))
    
    # Guardar la encuesta
    resultado = EncuestaModel.create(calificacion, comentario, servicio)
    
    if resultado:
        return redirect(url_for('encuesta.gracias'))
    else:
        flash('Error al enviar la encuesta. Intenta nuevamente.', 'error')
        return redirect(url_for('encuesta.index'))

@encuesta_bp.route('/gracias')
def gracias():
    """Página de agradecimiento"""
    return render_template('encuesta/gracias.html')