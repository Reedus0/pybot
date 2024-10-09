CREATE DATABASE bot;

\c bot

CREATE TABLE email (
    id SERIAL PRIMARY KEY,
    email varchar(255) NOT NULL
);

CREATE TABLE phone (
    id SERIAL PRIMARY KEY,
    phone varchar(255) NOT NULL
);

CREATE USER db_user WITH ENCRYPTED PASSWORD 'pass';

GRANT INSERT, SELECT ON email,phone TO db_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO db_user;

CREATE USER db_repl_user WITH REPLICATION ENCRYPTED PASSWORD 'pass';
SELECT pg_create_physical_replication_slot('replication_slot');
