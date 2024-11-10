CREATE DATABASE Uni1500;
USE Uni1500;

CREATE TABLE inseminacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fazenda VARCHAR(255),
    estado VARCHAR(2),
    municipio VARCHAR(255),
    numero_animal DECIMAL(10, 2),
    lote VARCHAR(50),
    raca VARCHAR(50),
    categoria VARCHAR(50),
    ecc DECIMAL(3, 2),
    ciclicidade DECIMAL(3, 2),
    protocolo VARCHAR(50),
    empresa VARCHAR(255),
    produto VARCHAR(255),
    dose VARCHAR(50),
    data_aplicacao DATE,
    diagnostico VARCHAR(255),
    cid VARCHAR(50),
    cid_lado VARCHAR(50),
    data_diagnostico DATE,
    ecg VARCHAR(255),
    dose_ecg VARCHAR(50),
    touro VARCHAR(50),
    raca_touro VARCHAR(50),
    empresa_touro VARCHAR(255),
    inseminador VARCHAR(255),
    numero_iatf VARCHAR(50),
    dg DECIMAL(3, 2),
    vazia VARCHAR(5),
    com_ou_sem_cl VARCHAR(50),
    perda VARCHAR(50)
);
select * from inseminacao;
