CREATE DATABASE TERCEIRO;

CREATE TABLE operadoras(
    id INT NOT NULL,
    registro_ans INT NOT NULL,
    razao_social VARCHAR (150) NOT NULL,
    nome_fantasia VARCHAR (150) NOT NULL,
    modalidade VARCHAR (100) NOT NULL,
    endereco_logradouro VARCHAR (100),
    endereco_numero TINYINT,
    endereco_complemento VARCHAR (50),
    endereco_bairro VARCHAR (50),
    endereco_cidade VARCHAR (50),
    endereco_uf CHAR (2),
    endereco_cep INT(8),
    ddd INT(3),
    telefone int(9),
    fax INT(15),
    email VARCHAR(50),
    representante_nome VARCHAR(50),
    representante_cargo VARCHAR(50),
    data_registro_ans DATE,
    PRIMARY KEY (id)
);

CREATE TABLE despesas(
    id INT NOT NULL,
    data_despesa DATE,
    codigo_conta_contabil INT,
    descricao VARCHAR(200),
    valor_saldo_final DECIMAL(18,2),
    registro_ans_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (registro_ans_id) REFERENCES operadoras (registro_ans)
);