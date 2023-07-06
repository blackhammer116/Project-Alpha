-- Script for creating a database in the server

CREATE DATABASE IF NOT EXISTS test;
USE test;
CREATE TABLE IF NOT EXISTS user(username varchar(128) not null, password varchar(128) not null);
