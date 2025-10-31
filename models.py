import mysql.connector
from mysql.connector import Error
from config import Config
from datetime import datetime

class Database:
    """Clase para manejar la conexión a la base de datos"""
    
    @staticmethod
    def get_connection():
        """Establece y retorna una conexión a la base de datos"""
        try:
            connection = mysql.connector.connect(**Config.DB_CONFIG)
            return connection
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None
    
    @staticmethod
    def execute_query(query, params=None, fetch=False):
        """Ejecuta una query y retorna los resultados si fetch=True"""
        connection = Database.get_connection()
        if connection is None:
            print("❌ No se pudo establecer conexión con la base de datos.")
            return [] if fetch else None
        
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            
            if fetch:
                result = cursor.fetchall()
                cursor.close()
                connection.close()
                return result
            else:
                connection.commit()
                last_id = cursor.lastrowid
                cursor.close()
                connection.close()
                return last_id
        except Error as e:
            print(f"Error en la query: {e}")
            return None


class ProductoModel:
    """Modelo para manejar productos del POS"""
    
    @staticmethod
    def get_all():
        """Obtiene todos los productos activos"""
        query = "SELECT * FROM productos WHERE activo = TRUE ORDER BY nombre"
        return Database.execute_query(query, fetch=True)
    
    @staticmethod
    def get_by_id(producto_id):
        """Obtiene un producto por su ID"""
        query = "SELECT * FROM productos WHERE id = %s AND activo = TRUE"
        result = Database.execute_query(query, (producto_id,), fetch=True)
        return result[0] if result else None
    
    @staticmethod
    def update_stock(producto_id, cantidad):
        """Actualiza el stock de un producto"""
        query = """
        UPDATE productos 
        SET stock = GREATEST(stock - %s, 0) 
        WHERE id = %s
        """
        return Database.execute_query(query, (cantidad, producto_id))


class VentaModel:
    """Modelo para manejar ventas del POS"""
    
    @staticmethod
    def create(total, metodo_pago='Efectivo'):
        """Crea una nueva venta"""
        query = "INSERT INTO ventas (total, metodo_pago) VALUES (%s, %s)"
        return Database.execute_query(query, (total, metodo_pago))
    
    @staticmethod
    def add_detalle(id_venta, id_producto, cantidad, subtotal):
        """Agrega el detalle de una venta"""
        query = """
            INSERT INTO detalle_ventas (id_venta, id_producto, cantidad, subtotal)
            VALUES (%s, %s, %s, %s)
        """
        return Database.execute_query(query, (id_venta, id_producto, cantidad, subtotal))
    
    @staticmethod
    def get_all():
        """Obtiene todas las ventas"""
        query = """
            SELECT v.*, COUNT(dv.id) as productos_vendidos
            FROM ventas v
            LEFT JOIN detalle_ventas dv ON v.id = dv.id_venta
            GROUP BY v.id
            ORDER BY v.fecha DESC
        """
        return Database.execute_query(query, fetch=True)
    
    @staticmethod
    def get_estadisticas():
        """Obtiene estadísticas de ventas"""
        query = """
            SELECT 
                COUNT(*) as total_ventas,
                SUM(total) as ingresos_totales,
                AVG(total) as promedio_venta,
                MAX(total) as venta_maxima,
                DATE(fecha) as fecha
            FROM ventas
            GROUP BY DATE(fecha)
            ORDER BY fecha DESC
            LIMIT 30
        """
        return Database.execute_query(query, fetch=True)


class EncuestaModel:
    """Modelo para manejar encuestas de satisfacción"""
    
    @staticmethod
    def create(calificacion, comentario, servicio_evaluado):
        """Crea una nueva encuesta"""
        query = """
            INSERT INTO encuestas (calificacion, comentario, servicio_evaluado)
            VALUES (%s, %s, %s)
        """
        return Database.execute_query(query, (calificacion, comentario, servicio_evaluado))
    
    @staticmethod
    def get_all():
        """Obtiene todas las encuestas"""
        query = "SELECT * FROM encuestas ORDER BY fecha DESC"
        return Database.execute_query(query, fetch=True)
    
    @staticmethod
    def get_estadisticas():
        """Obtiene estadísticas de las encuestas"""
        query = """
            SELECT 
                COUNT(*) as total_encuestas,
                AVG(calificacion) as promedio_calificacion,
                MAX(calificacion) as calificacion_maxima,
                MIN(calificacion) as calificacion_minima,
                servicio_evaluado,
                COUNT(*) as cantidad
            FROM encuestas
            GROUP BY servicio_evaluado
        """
        return Database.execute_query(query, fetch=True)


class UsuarioAdminModel:
    """Modelo para manejar usuarios administradores"""
    
    @staticmethod
    def authenticate(usuario, password):
        """Autentica un usuario administrador"""
        query = "SELECT * FROM usuarios_admin WHERE usuario = %s AND password = %s"
        result = Database.execute_query(query, (usuario, password), fetch=True)
        
        if result:
            # Actualizar último acceso
            update_query = "UPDATE usuarios_admin SET ultimo_acceso = NOW() WHERE id = %s"
            Database.execute_query(update_query, (result[0]['id'],))
            return result[0]
        return None
    
    @staticmethod
    def get_by_id(user_id):
        """Obtiene un usuario por su ID"""
        query = "SELECT * FROM usuarios_admin WHERE id = %s"
        result = Database.execute_query(query, (user_id,), fetch=True)
        return result[0] if result else None