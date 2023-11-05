-- Crear la base de datos
CREATE DATABASE NodoTemperatura;

-- Usar la base de datos
USE NodoTemperatura;

-- Crear la tabla para las lecturas de temperatura
CREATE TABLE LecturasTemperatura (
    lectura_id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_hora TIMESTAMP NOT NULL,
    temperatura DECIMAL(5, 2) NOT NULL
);

-- Crear la tabla para las acciones del actuador
CREATE TABLE AccionesActuador (
    accion_id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_hora TIMESTAMP NOT NULL,
    temperatura DECIMAL(5, 2) NOT NULL,
    accion_realizada VARCHAR(255) NOT NULL
);