DROP DATABASE ANS;

CREATE DATABASE ANS;

USE TERCEIRO;

CREATE TABLE operadoras(
    registro_ans INT,
    cnpj varchar(19),
    razao_social VARCHAR (150),
    nome_fantasia VARCHAR (150),
    modalidade VARCHAR (100),
    endereco_logradouro VARCHAR (100),
    endereco_numero VARCHAR (30),
    endereco_complemento VARCHAR (50),
    endereco_bairro VARCHAR (50),
    endereco_cidade VARCHAR (50),
    endereco_uf CHAR (2),
    endereco_cep INT(8),
    ddd VARCHAR(5),
    telefone VARCHAR(25),
    fax VARCHAR(20),
    email VARCHAR(50),
    representante_nome VARCHAR(50),
    representante_cargo VARCHAR(50),
    data_registro_ans DATE
);

CREATE TABLE despesas(
    data_despesa DATE,
    registro_ans_id INT,
    codigo_conta_contabil INT,
    descricao VARCHAR(300),
    valor_saldo_inicial DECIMAL(40, 2),
    valor_saldo_final DECIMAL(40, 2)
);

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/Relatorio_cadop.csv' INTO TABLE operadoras CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 3 ROWS (
    registro_ans,
    cnpj,
    razao_social,
    nome_fantasia,
    modalidade,
    endereco_logradouro,
    endereco_numero,
    endereco_complemento,
    endereco_bairro,
    endereco_cidade,
    endereco_uf,
    endereco_cep,
    ddd,
    telefone,
    fax,
    email,
    representante_nome,
    representante_cargo,
    @data_registro_ans
)
SET
    data_registro_ans = STR_TO_DATE(@data_registro_ans, '%d/%m/%Y');

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/1T2021.csv' INTO TABLE despesas CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data_despesa,
    registro_ans_id,
    codigo_conta_contabil,
    descricao,
    @valor_saldo_final
)
SET
    data_despesa = STR_TO_DATE(@data_despesa, '%d/%m/%Y'),
    valor_saldo_final = REPLACE(@valor_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/2T2021.csv' INTO TABLE despesas CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data_despesa,
    registro_ans_id,
    codigo_conta_contabil,
    descricao,
    @valor_saldo_final
)
SET
    data_despesa = STR_TO_DATE(@data_despesa, '%d/%m/%Y'),
    valor_saldo_final = REPLACE(@valor_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/3T2021.csv' INTO TABLE despesas CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data_despesa,
    registro_ans_id,
    codigo_conta_contabil,
    descricao,
    @valor_saldo_final
)
SET
    data_despesa = STR_TO_DATE(@data_despesa, '%d/%m/%Y'),
    valor_saldo_final = REPLACE(@valor_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/4T2021.csv' INTO TABLE despesas CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    data_despesa,
    registro_ans_id,
    codigo_conta_contabil,
    descricao,
    @valor_saldo_inicial,
    @valor_saldo_final
)
SET
    valor_saldo_inicial = REPLACE(@valor_saldo_inicial, ',', '.'),
    valor_saldo_final = REPLACE(@valor_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/1T2022.csv' INTO TABLE despesas CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    data_despesa,
    registro_ans_id,
    codigo_conta_contabil,
    descricao,
    @valor_saldo_inicial,
    @valor_saldo_final
)
SET
    valor_saldo_inicial = REPLACE(@valor_saldo_inicial, ',', '.'),
    valor_saldo_final = REPLACE(@valor_saldo_final, ',', '.');

LOAD DATA INFILE 'C:/Users/higor/Desktop/IC/Anexos_Teste 3/2T2022.csv' INTO TABLE despesas CHARACTER SET latin1 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS (
    @data_despesa,
    registro_ans_id,
    codigo_conta_contabil,
    descricao,
    @valor_saldo_inicial,
    @valor_saldo_final
)
SET
    data_despesa = STR_TO_DATE(@data_despesa, '%d/%m/%Y'),
    valor_saldo_inicial = REPLACE(@valor_saldo_inicial, ',', '.'),
    valor_saldo_final = REPLACE(@valor_saldo_final, ',', '.');