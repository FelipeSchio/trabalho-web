create database mercadinho;
use mercadinho;

create table if not exists Funcionario (
	id integer auto_increment not null,
    nome varchar(25) not null,
    email varchar(25) not null,
	telefone varchar(25) not null,
	senha varchar(25) not null,
	tipo varchar(25) not null,
	data_cadastro date not null,
	data_atualizacao date not null,
    primary key (id)
);

create table if not exists Fornecedor (
	id integer auto_increment not null,
    nome varchar(25) not null,
    email varchar(25) not null,
    telefone varchar(25) not null,
    primary key (id)
);

create table if not exists Produto (
	id integer auto_increment not null,
    nome varchar(25) not null,
    preco_unitario double not null,
    quantidade double not null,
    unidade varchar(2) not null,
    fornecedor integer not null,
    primary key (id),
    foreign key (fornecedor) references fornecedor (id)
);

create table if not exists Venda (
	id integer auto_increment not null,
    produto integer not null,
    funcionario integer not null,
    quantidade integer not null,
    valor_total double not null,
    primary key (id),
    foreign key (produto) references produto (id),
    foreign key (funcionario) references funcionario (id)
);