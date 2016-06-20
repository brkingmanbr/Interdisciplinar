drop database SIS;
create database SIS;
use SIS;

CREATE TABLE Turno (
    turno VARCHAR(30) PRIMARY KEY
);
insert into turno values('Matutino');
insert into turno values('Vespertino');
insert into turno values('Noturno');

CREATE TABLE Disciplina (
    nome VARCHAR(40) PRIMARY KEY
);
select * from Disciplina;
insert into Disciplina values('Disciplina de Teste');

CREATE TABLE Professor (
    id_prof INT AUTO_INCREMENT PRIMARY KEY,
    matricula INT,
    nome_prof VARCHAR(40),
    disciplina VARCHAR(40),
    carga_horaria INT,
    quantidade_dias INT,
    disponibilidade varchar(300),
    FOREIGN KEY (disciplina)
        REFERENCES Disciplina (nome_disc)
);
INSERT INTO Professor(matricula, nome_prof, disciplina, carga_horaria, quantidade_dias, detalhe) SELECT * FROM (SELECT 21312 ,'asdad','Disciplina de Teste', 20, 5) AS x WHERE NOT EXISTS (SELECT * FROM Professor WHERE  matricula = 21312 AND nome_prof = 'asdad' AND disciplina = 'Disciplina de Teste') LIMIT 1;
SELECT * FROM Coordenador ORDER BY id;
select * from turma;
SELECT 
    *
FROM
    professor
ORDER BY (nome_prof);
#Turma Disciplina CH Qtd.Dias Docente

SELECT id_prof FROM Professor WHERE nome_prof = 'Rasta de Shambalá 1';

SELECT nome_prof FROM Professor;
SELECT matricula, nome_prof FROM Professor ORDER BY matricula;
delete from Professor where nome_prof = 'Rasta de Shambalá';
insert into Professor(matricula, nome_prof, disciplina) values(123456, 'Rasta de Shambalá 1', 'Disciplina de Teste');
insert into Professor(matricula, nome_prof, disciplina) values(1234567, 'Rasta de Shambalá 2', 'Disciplina de Teste');
insert into Professor(matricula, nome_prof, disciplina) values(12345678, 'Rasta de Shambalá 3', 'Disciplina de Teste');
insert into Professor(matricula, nome_prof, disciplina) values(123456789, 'Rasta de Shambalá 4', 'Disciplina de Teste');
SELECT id_prof FROM Professor where nome_prof = 'Rasta de Shambalá 1';

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

SELECT horario FROM Horario ORDER BY (horario);

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
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(40),
    login VARCHAR(30),
    senha VARCHAR(30)
);

use SIS;
drop database SIS;
insert into Coordenador(nome, login, senha) values('coordenador', 'teste', '123');
SELECT * FROM Coordenador ORDER BY id;



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
use sis;
truncate Cronograma;
insert into Cronograma values(1, '20160609', '07:30 - 08:30', 'TEC50419', 1);
insert into Cronograma values(1, '20160609', '08:30 - 09:30', 'TEC50419', 1);
insert into Cronograma values(1, '20160609', '09:30 - 10:30', 'TEC50419', 1);
insert into Cronograma values(1, '20160609', '10:30 - 11:30', 'TEC50419', 1);

select id_professor from Cronograma where data_reserva = '20160609' and horario = '07:30 - 08:30';
SELECT nome_prof FROM Professor where id_prof = 1;
truncate Cronograma;
select count(*) from Cronograma;
INSERT INTO  Cronograma (id_professor, data_reserva, horario, turma) VALUES (1, '20160606', '07:30 - 08:30', 'TEC50419');
#DELETE FROM Cronograma WHERE id_professor = 1 AND data_reserva = '20160606' AND horario = '07:30 - 08:30', turma = 'TEC50419');
SELECT * FROM (SELECT 0, '%s','%ss', 0.0) AS x;
SELECT 0, '%s','%ss', 0.0;

select horario from Horario order by horario;

select * from Cronograma;
use sis;
INSERT INTO  Cronograma (id_professor, data_reserva, horario, turma) SELECT * FROM (SELECT 1, '20160606', '07:30 - 08:30', 'TEC50419') AS x WHERE NOT EXISTS (SELECT * FROM Cronograma WHERE id_professor = 1 AND data_reserva = '20160606'AND horario = '07:30 - 08:30' AND turma = 'TEC50419') LIMIT 1;
select * from Cronograma;
select * from turno;

INSERT INTO Cronograma(id_professor, data_reserva, horario, turma, id_coordenador)SELECT * FROM (SELECT 1, '20160606', '07:30 - 08:30', 'TESTE0001', 1) AS x WHERE NOT EXISTS (SELECT * FROM Cronograma	WHERE id_professor = 1 AND data_reserva = '20160606' AND horario = '07:30 - 08:30' AND turma = 'TESTE0001' AND id_coordenador = 1) LIMIT 1;