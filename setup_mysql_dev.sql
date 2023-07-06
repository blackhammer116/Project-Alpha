-- Script for creating a database in the server

CREATE DATABASE IF NOT EXISTS NOVA_DB;
USE NOVA_DB;
CREATE TABLE IF NOT EXISTS clients(client_id varchar(128) not null primary key, username varchar(128) not null, password varchar(128) not null,
		f_name varchar(128) not null,
		lname varchar(128) not null, m_name varchar(128) null, p_number varchar(128) not null,
		email varchar(128) not null, request varchar(20) null);
CREATE TABLE IF NOT EXISTS requests(request varchar(20) not null primary key, client_id varchar(128) null);
ALTER TABLE requests
ADD FOREIGN KEY (client_id) REFERENCES clients(client_id);
ALTER TABLE clients
ADD FOREIGN KEY (request) REFERENCES requests(request);
