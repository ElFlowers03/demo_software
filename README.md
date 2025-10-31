# 🚀 Portafolio de Servicios - Demo Completo

Aplicación web completa que demuestra servicios de desarrollo de software, incluyendo Sistema POS, Encuestas de Satisfacción y Panel Administrativo.

## 📋 Características

- **Sistema de Punto de Venta (POS)**: Gestión completa de productos, ventas y carrito de compras
- **Encuestas de Satisfacción**: Sistema de recolección de feedback con escala de calificación
- **Panel Administrativo**: Dashboard con estadísticas, gráficos y reportes
- **Diseño Profesional**: Interfaz moderna, responsiva y limpia basada en Bootstrap 5
- **Base de Datos MySQL**: Almacenamiento persistente de datos
- **Arquitectura Modular**: Organizado con Blueprints de Flask

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3.8+ con Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Base de Datos**: MySQL 8.0+
- **Gráficos**: Chart.js
- **Iconos**: Font Awesome 6

## 📁 Estructura del Proyecto

```
proyecto/
│
├── app/
│   ├── __init__.py              # Inicialización de la app Flask
│   ├── routes/
│   │   ├── home.py             # Rutas de la página principal
│   │   ├── pos.py              # Rutas del sistema POS
│   │   ├── encuesta.py         # Rutas de encuestas
│   │   └── admin.py            # Rutas del panel admin
│   ├── static/
│   │   └── css/
│   │       └── style.css       # Estilos personalizados
│   └── templates/
│       ├── base.html           # Template base
│       ├── home.html           # Página principal
│       ├── pos/
│       │   └── index.html      # Sistema POS
│       ├── encuesta/
│       │   ├── index.html      # Formulario de encuesta
│       │   └── gracias.html    # Página de agradecimiento
│       └── admin/
│           ├── login.html      # Login administrativo
│           └── dashboard.html  # Dashboard principal
│
├── config.py                   # Configuración de la aplicación
├── models.py                   # Modelos de base de datos
├── database_setup.sql          # Script de creación de BD
├── run.py                      # Archivo principal para ejecutar
├── requirements.txt            # Dependencias de Python
└── README.md                   # Este archivo
```

## 🚀 Instalación y Configuración

### 1. Requisitos Previos

- Python 3.8 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)

### 2. Clonar o Descargar el Proyecto

```bash
# Si usas git
git clone <url-del-repositorio>
cd proyecto

# O simplemente descarga y descomprime los archivos
```

### 3. Crear Entorno Virtual (Recomendado)

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar MySQL

1. Inicia el servidor MySQL
2. Crea la base de datos e inserta los datos de prueba:

```bash
mysql -u root -p < database_setup.sql
```

O desde MySQL Workbench/phpMyAdmin, ejecuta el contenido del archivo `database_setup.sql`

### 6. Configurar Variables de Entorno (Opcional)

Crea un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=demo_servicios_db
DB_PORT=3306
SECRET_KEY=tu-clave-secreta-aqui
FLASK_DEBUG=True
```

Si no creas este archivo, se usarán los valores por defecto de `config.py`

### 7. Ejecutar la Aplicación

```bash
python run.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 🔐 Credenciales de Acceso

### Panel Administrativo
- **Usuario**: `admin`
- **Contraseña**: `admin123`

⚠️ **IMPORTANTE**: Cambia estas credenciales en producción

## 📱 Funcionalidades Principales

### 1. Página Principal (/)
- Presentación de servicios
- Navegación a las demos
- Información de contacto

### 2. Sistema POS (/pos)
- Visualización de productos
- Agregar productos al carrito
- Gestionar cantidades
- Procesar ventas
- Selección de método de pago

### 3. Encuestas (/encuesta)
- Formulario de satisfacción
- Escala de calificación 1-10
- Comentarios opcionales
- Página de agradecimiento

### 4. Panel Admin (/admin)
- Login seguro
- Dashboard con estadísticas
- Gráficos de ventas
- Gráficos de encuestas
- Historial de transacciones

## 🎨 Paleta de Colores

El diseño está basado en la siguiente paleta:
- **Primary**: #5D7D98
- **Primary Dark**: #4A6477
- **Primary Light**: #7A9AB3
- **Success**: #5FA582
- **Warning**: #E0A85F
- **Danger**: #D87D7D

## 🔧 Configuración Avanzada

### Cambiar Puerto de Ejecución

Edita `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Cambia 8080 por el puerto deseado
```

### Configurar Base de Datos Diferente

Edita `config.py` o usa variables de entorno en `.env`

### Deshabilitar Modo Debug

En producción, cambia en `config.py`:
```python
DEBUG = False
```

## 📊 Base de Datos

### Tablas Principales

1. **productos**: Catálogo de productos para el POS
2. **ventas**: Registro de ventas realizadas
3. **detalle_ventas**: Detalles de cada venta
4. **encuestas**: Respuestas de encuestas de satisfacción
5. **usuarios_admin**: Usuarios del panel administrativo

### Datos de Ejemplo

El script `database_setup.sql` incluye:
- 8 productos de ejemplo
- 1 usuario administrador
- 5 encuestas de muestra

## 🐛 Solución de Problemas

### Error de Conexión a MySQL

```
Error: Can't connect to MySQL server
```

**Solución**:
1. Verifica que MySQL esté ejecutándose
2. Confirma las credenciales en `config.py`
3. Asegúrate de que la base de datos exista

### Error de Módulo No Encontrado

```
ModuleNotFoundError: No module named 'flask'
```

**Solución**:
```bash
pip install -r requirements.txt
```

### Puerto Ya en Uso

```
OSError: [Errno 98] Address already in use
```

**Solución**: Cambia el puerto en `run.py` o detén el proceso que usa el puerto 5000

## 🚀 Despliegue en Producción

### Recomendaciones

1. **Usar un servidor WSGI**: Gunicorn o uWSGI
2. **Configurar HTTPS**: Con Let's Encrypt
3. **Usar variables de entorno**: Para credenciales sensibles
4. **Configurar respaldos**: De la base de datos
5. **Implementar logging**: Para monitoreo
6. **Cambiar SECRET_KEY**: Usa una clave segura y única

### Ejemplo con Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## 📝 Licencia

Este proyecto es una demostración y puede ser utilizado libremente para propósitos educativos y comerciales.

## 👥 Contacto

- **Email**: contacto@devsolutions.com
- **Teléfono**: +52 55 1234 5678

## 🎯 Próximas Mejoras

- [ ] Sistema de autenticación con JWT
- [ ] API REST completa
- [ ] Exportación de reportes a PDF
- [ ] Notificaciones en tiempo real
- [ ] Sistema de roles y permisos
- [ ] Integración con pasarelas de pago
- [ ] Dashboard más avanzado con más métricas

---

**Desarrollado con ❤️ por DevSolutions**