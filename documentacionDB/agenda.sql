CREATE DATABASE agenda;

CREATE TABLE agenda(
	idAgenda NUMERIC(2,0) NOT NULL,
	anio CHAR(4) NOT NULL,

	CONSTRAINT pkAgenda
	PRIMARY KEY (idAgenda)
);

CREATE TABLE prioridad(
	idPrioridad NUMERIC(2,0) NOT NULL,
	nombre VARCHAR(5) NOT NULL,

	CONSTRAINT pkPrioridad
	PRIMARY KEY (idPrioridad),

	CONSTRAINT uqPrioridadNombre
	UNIQUE (nombre)
);

CREATE TABLE categoria(
	idCategoria NUMERIC(2,0) NOT NULL,
	nombre VARCHAR(8) NOT NULL,

	CONSTRAINT pkCategoria
	PRIMARY KEY (idCategoria),

	CONSTRAINT uqCategoriaNombre
	UNIQUE (nombre)
);

CREATE TABLE escuela(
	idCategoria NUMERIC (2,0) NOT NULL,
	materia VARCHAR(255) NOT NULL,

	CONSTRAINT fkEscuelaCategoria
	FOREIGN KEY (idCategoria)
	REFERENCES categoria(idCategoria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE trabajo(
	idCategoria NUMERIC (2,0) NOT NULL,
	supervisor VARCHAR(255) NOT NULL,

	CONSTRAINT fkTrabajoCategoria
	FOREIGN KEY (idCategoria)
	REFERENCES categoria(idCategoria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE casa(
	idCategoria NUMERIC (2,0) NOT NULL,
	lugar VARCHAR(255) NOT NULL,

	CONSTRAINT fkCasaCategoria
	FOREIGN KEY (idCategoria)
	REFERENCES categoria(idCategoria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

CREATE TABLE tarea(
	idTarea SERIAL,
	descripcion VARCHAR(255) NOT NULL,
	fechaEntrega DATE NOT NULL,
	horaEntrega TIME NOT NULL,
	completada CHAR(1) NOT NULL,
	idPrioridad NUMERIC(2,0) NOT NULL,
	idCategoria NUMERIC(2,0) NOT NULL,
	idAgenda NUMERIC(2,0) NOT NULL,

	CONSTRAINT pkTarea
	PRIMARY KEY (idTarea),

	CONSTRAINT fkTareaPrioridad
	FOREIGN KEY (idPrioridad)
	REFERENCES prioridad(idPrioridad)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT fkTareaCategoria
	FOREIGN KEY (idCategoria)
	REFERENCES categoria(idCategoria)
	ON DELETE RESTRICT
	ON UPDATE CASCADE,

	CONSTRAINT fkTareaAgenda
	FOREIGN KEY (idAgenda)
	REFERENCES agenda(idAgenda)
	ON DELETE RESTRICT
	ON UPDATE CASCADE
);

INSERT INTO prioridad VALUES (1, 'Alta'), (2, 'Media'), (3, 'Baja');
INSERT INTO categoria VALUES (1, 'Escuela'), (2, 'Trabajo'), (3, 'Casa');
INSERT INTO agenda VALUES (1, '2025');

SELECT * FROM tarea;
SELECT * FROM agenda;
SELECT * FROM prioridad;
SELECT * FROM categoria;
SELECT * FROM escuela;
SELECT * FROM casa;
SELECT * FROM trabajo;

