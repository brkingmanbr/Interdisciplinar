drop database SIS;
create database SIS;
use SIS;

CREATE TABLE Professor (
    matricula INT PRIMARY KEY,
    nome_prof VARCHAR(40)
);
CREATE TABLE Turno (
    turno VARCHAR(30) PRIMARY KEY
);
insert into turno values('Matutino');
insert into turno values('Vespertino');
insert into turno values('Noturno');

CREATE TABLE Horario (
    horario VARCHAR(13) PRIMARY KEY,
    turno VARCHAR(30),
    FOREIGN KEY (turno)
        REFERENCES Turno (turno)
);
insert into Horario values('07:30 - 08:30','Matutino');
insert into Horario values('08:30 - 09:30','Matutino');
insert into Horario values('09:30 - 10:30','Matutino');
insert into Horario values('10:30 - 11:30','Matutino');

CREATE TABLE Turma (
    nome_turma VARCHAR(10) PRIMARY KEY,
    turno VARCHAR(30),
    FOREIGN KEY (turno)
        REFERENCES Turno (turno)
);
CREATE TABLE Coordenador(
    id_coor VARCHAR(30) PRIMARY KEY,
    nome VARCHAR(40),
    login VARCHAR(30),
    senha VARCHAR(30)
);
CREATE TABLE Cronograma (
    mat_professor INT,
    data_reserva DATE,
    horario VARCHAR(13),
    id_coordenador VARCHAR(13),
    FOREIGN KEY (mat_professor)
        REFERENCES professor (matricula),
    FOREIGN KEY (id_coordenador)
        REFERENCES Coordenador (id_coor)
);ba