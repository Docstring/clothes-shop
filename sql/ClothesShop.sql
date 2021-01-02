CREATE DATABASE clothes_shop;

\c clothes_shop

CREATE TYPE colours AS ENUM ('blue', 'green', 'red', 'yellow');
CREATE TYPE sexes AS ENUM ('male', 'female');
CREATE TYPE sizes AS ENUM ('small', 'medium', 'large');

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE clothes_stock(
    id UUID NOT NULL DEFAULT uuid_generate_v4(),
    clothes_name TEXT NOT NULL,
    price NUMERIC NOT NULL,
    cost NUMERIC NOT NULL,
    colour colours NOT NULL,
    sex sexes NOT NULL,
    clothes_size sizes NOT NULL,
    stock_level int NOT NULL
);

INSERT INTO clothes_stock (clothes_name, price, cost, colour, sex, clothes_size, stock_level)
VALUES ('Red T-Shirt', 1.99, 0.99, 'red', 'male', 'small', 100);
