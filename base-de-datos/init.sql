CREATE TABLE IF NOT EXISTS proyectos (
    id_proyectos INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    descripcion TEXT,
    latitud FLOAT,
    longitud FLOAT,
    tipo_inmueble VARCHAR(100),
    tipo_contrato VARCHAR(100),
    precio FLOAT,
    ancho INT,
    largo INT
INSERT INTO proyectos (nombre, imagen, descripcion, latitud, longitud, tipo_inmueble, tipo_contrato, precio, ancho, largo)
VALUES
    ('Casa cerca de Palermo', 'imagen_1.jpg', 'Amplia casa de estilo en zona residencial.', -34.5845, -58.4321, 'Casa', 'Venta', 850000, 20, 15),
    ('Dpto en Recoleta', 'imagen_2.jpg', 'Departamento moderno en edificio de lujo.', -34.5958, -58.3926, 'Dpto', 'Alquiler', 2000, 10, 10),
    ('Casa en Belgrano', 'imagen_3.jpg', 'Hermosa casa con jardín y piscina.', -34.5632, -58.4538, 'Casa', 'Venta', 1200000, 25, 20),
    ('Dpto con vista al río', 'imagen_4.jpg', 'Apartamento con excelente vista al río.', -34.5421, -58.3874, 'Dpto', 'Venta', 450000, 15, 12),
    ('Casa en Núñez', 'imagen_5.jpg', 'Acogedora casa familiar con amplio patio.', -34.5497, -58.4635, 'Casa', 'Alquiler', 3000, 18, 16),
    ('Dpto en Puerto Madero', 'imagen_6.jpg', 'Lujoso departamento en la zona más exclusiva de la ciudad.', -34.6098, -58.3623, 'Dpto', 'Venta', 1500000, 30, 25),
    ('Casa con jardín en Caballito', 'imagen_7.jpg', 'Casa luminosa con jardín en barrio tranquilo.', -34.6181, -58.4427, 'Casa', 'Venta', 780000, 22, 18),
    ('Dpto en Palermo Soho', 'imagen_8.jpg', 'Moderno departamento cerca de tiendas y restaurantes.', -34.5895, -58.4240, 'Dpto', 'Alquiler', 2500, 12, 10),
    ('Casa en Villa Urquiza', 'imagen_9.jpg', 'Espaciosa casa con excelente ubicación.', -34.5682, -58.4887, 'Casa', 'Venta', 550000, 21, 17),
    ('Dpto en San Telmo', 'imagen_10.jpg', 'Apartamento remodelado en barrio histórico.', -34.6209, -58.3736, 'Dpto', 'Alquiler', 1800, 14, 12);


