from flask import Blueprint, render_template, request, jsonify
from models import ProductoModel, VentaModel

pos_bp = Blueprint('pos', __name__)

@pos_bp.route('/')
def index():
    """Página principal del POS"""
    productos = ProductoModel.get_all()
    return render_template('pos/index.html', productos=productos)

@pos_bp.route('/api/productos')
def get_productos():
    """API para obtener todos los productos"""
    productos = ProductoModel.get_all()
    return jsonify(productos if productos else [])

@pos_bp.route('/api/producto/<int:producto_id>')
def get_producto(producto_id):
    """API para obtener un producto específico"""
    producto = ProductoModel.get_by_id(producto_id)
    if producto:
        return jsonify(producto)
    return jsonify({'error': 'Producto no encontrado'}), 404

@pos_bp.route('/api/venta', methods=['POST'])
def crear_venta():
    """API para crear una nueva venta"""
    data = request.get_json()
    
    if not data or 'items' not in data or 'total' not in data:
        return jsonify({'error': 'Datos incompletos'}), 400
    
    # Crear la venta
    metodo_pago = data.get('metodo_pago', 'Efectivo')
    id_venta = VentaModel.create(data['total'], metodo_pago)
    
    if not id_venta:
        return jsonify({'error': 'Error al crear la venta'}), 500
    
    # Agregar detalles de la venta
    for item in data['items']:
        VentaModel.add_detalle(
            id_venta,
            item['id'],
            item['cantidad'],
            item['subtotal']
        )
        
        # Actualizar stock
        ProductoModel.update_stock(item['id'], item['cantidad'])
    
    return jsonify({
        'success': True,
        'id_venta': id_venta,
        'mensaje': 'Venta registrada exitosamente'
    })

@pos_bp.route('/ventas')
def historial_ventas():
    """Página de historial de ventas"""
    ventas = VentaModel.get_all()
    return render_template('pos/ventas.html', ventas=ventas)