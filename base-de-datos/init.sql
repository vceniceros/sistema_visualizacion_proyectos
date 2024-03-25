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
);


