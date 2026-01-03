CREATE DATABASE sales;

CREATE TABLE sales.store
(
	store_id INT,
    store_name VARCHAR(200)
);

INSERT INTO sales.store VALUES
(1, 'XYZ'),
(2, 'ABC');


-- With constraints
CREATE TABLE sales.store_new
(
	store_id INT UNIQUE,
    store_name VARCHAR(200) NOT NULL
);

INSERT INTO sales.store_new VALUES
(1, 'XYZ'),
(2, 'ABC');

INSERT INTO sales.store_new VALUES
(3, 'WSA');

TRUNCATE TABLE sales.store;

DROP DATABASE sales;

DROP TABLE sales.store;

-- Add column
ALTER TABLE sales.store
ADD COLUMN store_city VARCHAR(200);

-- Rename column
ALTER TABLE sales.store
RENAME COLUMN store_city TO store_location;