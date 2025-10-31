-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS demo_servicios_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE demo_servicios_db;

-- Tabla de productos para el POS
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT,
    stock INT DEFAULT 0,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de ventas
CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL,
    metodo_pago VARCHAR(50) DEFAULT 'Efectivo'
);

-- Tabla de detalle de ventas
CREATE TABLE IF NOT EXISTS detalle_ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES ventas(id) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES productos(id)
);

-- Tabla de encuestas de satisfacción
CREATE TABLE IF NOT EXISTS encuestas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    calificacion INT NOT NULL CHECK (calificacion BETWEEN 1 AND 10),
    comentario TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    servicio_evaluado VARCHAR(100)
);

-- Tabla de usuarios administradores
CREATE TABLE IF NOT EXISTS usuarios_admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    email VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_acceso TIMESTAMP NULL
);

-- Insertar datos de ejemplo para productos
INSERT INTO productos (nombre, precio, descripcion, stock) VALUES
('Laptop HP 15"', 12999.00, 'Laptop para uso profesional', 10),
('Mouse Inalámbrico', 299.00, 'Mouse ergonómico con batería recargable', 50),
('Teclado Mecánico', 899.00, 'Teclado RGB para gaming', 25),
('Monitor 24"', 3499.00, 'Monitor Full HD con puerto HDMI', 15),
('Webcam HD', 799.00, 'Cámara web 1080p con micrófono', 30),
('Audífonos Bluetooth', 599.00, 'Audífonos con cancelación de ruido', 40),
('Disco Duro Externo 1TB', 1299.00, 'Almacenamiento portátil USB 3.0', 20),
('Memoria USB 64GB', 199.00, 'Memoria flash de alta velocidad', 100);

-- Insertar usuario administrador por defecto (password: admin123)
-- Nota: En producción usar hashing apropiado con bcrypt o similar
INSERT INTO usuarios_admin (usuario, password, nombre_completo, email) VALUES
('admin', 'admin123', 'Administrador del Sistema', 'admin@ejemplo.com');

-- Insertar algunas encuestas de ejemplo
INSERT INTO encuestas (calificacion, comentario, servicio_evaluado) VALUES
(9, 'Excelente servicio, muy profesionales', 'Desarrollo Web'),
(10, 'Superó mis expectativas, entrega a tiempo', 'Sistema POS'),
(8, 'Buen trabajo, algunas mejoras necesarias', 'Consultoría'),
(9, 'Muy satisfecho con el resultado final', 'Desarrollo Web'),
(10, 'Definitivamente los recomendaré', 'Panel Administrativo');



-- Ventas simuladas para el panel de administrador
INSERT INTO ventas (fecha, total, metodo_pago) VALUES
('2025-10-01 10:15:00', 1798.00, 'Efectivo'),
('2025-10-02 14:30:00', 899.00, 'Tarjeta'),
('2025-10-03 17:45:00', 13498.00, 'Transferencia'),
('2025-10-05 11:20:00', 4198.00, 'Efectivo'),
('2025-10-06 09:55:00', 599.00, 'Tarjeta'),
('2025-10-07 18:10:00', 3798.00, 'Transferencia'),
('2025-10-09 12:40:00', 14498.00, 'Efectivo'),
('2025-10-11 15:00:00', 2298.00, 'Tarjeta'),
('2025-10-13 13:25:00', 5197.00, 'Efectivo'),
('2025-10-16 10:50:00', 2498.00, 'Transferencia'),
('2025-10-18 16:10:00', 13999.00, 'Tarjeta'),
('2025-10-21 19:30:00', 1798.00, 'Efectivo'),
('2025-10-23 12:15:00', 2998.00, 'Transferencia'),
('2025-10-25 17:05:00', 9498.00, 'Tarjeta'),
('2025-10-27 11:30:00', 1598.00, 'Efectivo');


-- Detalles de las ventas (productos vendidos)
INSERT INTO detalle_ventas (id_venta, id_producto, cantidad, subtotal) VALUES
(1, 2, 2, 598.00),
(1, 5, 1, 799.00),
(2, 3, 1, 899.00),
(3, 1, 1, 12999.00),
(3, 8, 1, 199.00),
(4, 4, 1, 3499.00),
(4, 6, 1, 599.00),
(5, 6, 1, 599.00),
(6, 7, 1, 1299.00),
(6, 2, 2, 598.00),
(7, 1, 1, 12999.00),
(7, 5, 1, 799.00),
(8, 3, 2, 1798.00),
(8, 8, 1, 199.00),
(9, 4, 1, 3499.00),
(9, 6, 1, 599.00),
(9, 8, 1, 199.00),
(10, 2, 2, 598.00),
(10, 5, 1, 799.00),
(11, 1, 1, 12999.00),
(12, 6, 2, 1198.00),
(13, 3, 1, 899.00),
(13, 7, 1, 1299.00),
(14, 4, 2, 6998.00),
(14, 2, 5, 1495.00),
(15, 5, 2, 1598.00);
