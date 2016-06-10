drop database SIS;
create database SIS;
use SIS;

CREATE TABLE Turno (
    turno VARCHAR(30) PRIMARY KEY
);
insert into turno values('Matutino');
insert into turno values('Vespertino');
insert into turno values('Noturno');

CREATE TABLE Professor (
    id_prof INT AUTO_INCREMENT PRIMARY KEY,
    matricula INT,
    nome_prof VARCHAR(40)
);
SELECT nome_prof FROM Professor;
SELECT matricula, nome_prof FROM Professor ORDER BY matricula;
delete from Professor where nome_prof = 'Rasta de Shambalá';
insert into Professor(matricula, nome_prof) values(123456, 'Rasta de Shambalá 1');
insert into Professor(matricula, nome_prof) values(1234567, 'Rasta de Shambalá 2');
insert into Professor(matricula, nome_prof) values(12345678, 'Rasta de Shambalá 3');
insert into Professor(matricula, nome_prof) values(123456789, 'Rasta de Shambalá 4');


CREATE TABLE Professor_Turno (
    id_professor INT,
    turno_turno VARCHAR(30),
    FOREIGN KEY (id_professor)
        REFERENCES Professor (id_prof)
);

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
insert into Horario values('13:00 - 14:00','Vespertino');
insert into Horario values('14:00 - 15:00','Vespertino');
insert into Horario values('15:00 - 16:00','Vespertino');
insert into Horario values('16:00 - 17:00','Vespertino');
insert into Horario values('18:00 - 19:00','Noturno');
insert into Horario values('19:00 - 20:00','Noturno');
insert into Horario values('20:00 - 21:00','Noturno');
insert into Horario values('21:00 - 22:00','Noturno');

CREATE TABLE Turma (
    nome_turma VARCHAR(10) PRIMARY KEY,
    turno VARCHAR(30),
    FOREIGN KEY (turno)
        REFERENCES Turno (turno)
);
insert into Turma values('TEC50419','Matutino');
insert into Turma values('TEC50420','Matutino');
insert into Turma values('TEC50421','Matutino');
insert into Turma values('TEC50411','Matutino');
insert into Turma values('TEC50412','Matutino');
insert into Turma values('TEC50413','Matutino');
insert into Turma values('TEC50414','Matutino');
insert into Turma values('TEC50415','Matutino');
SELECT nome_turma, turno FROM Turma ORDER BY nome_turma;

CREATE TABLE Coordenador (
    id_coor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    login VARCHAR(30),
    senha VARCHAR(30)
);
insert into Coordenador(nome, login, senha) values('Nome de teste', 'teste', '123');

CREATE TABLE Cronograma (
    id_professor INT,
    data_reserva DATE,
    horario VARCHAR(13),
    turma VARCHAR(30),
    id_coordenador INT,
    FOREIGN KEY (id_professor)
        REFERENCES professor (id_prof),
    FOREIGN KEY (horario)
        REFERENCES Horario (horario),
    FOREIGN KEY (turma)
        REFERENCES Turma (nome_turma),
    FOREIGN KEY (id_coordenador)
        REFERENCES Coordenador (id_coor)
);

insert into Cronograma values(1, '20160806', '07:30 - 08:30', 'TEC50419', 1);
insert into Cronograma values(2, '20160806', '08:30 - 09:30', 'TEC50419', 1);
insert into Cronograma values(3, '20160806', '09:30 - 10:30', 'TEC50419', 1);
insert into Cronograma values(4, '20160806', '10:30 - 11:30', 'TEC50419', 1);
