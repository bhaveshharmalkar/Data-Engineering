-- SELECT
SELECT 
    *
FROM
    dim_customer;

-- WHERE 1
SELECT
	*
FROM
	dim_customer
WHERE
	gender = 'F';
    
-- WHERE 2
SELECT
	*
FROM
	dim_customer
WHERE
	(gender = 'F') AND (country = 'France' OR join_date > '2022-01-01');
    
-- Like
-- 1
SELECT
	*
FROM
	dim_customer
WHERE 
	first_name LIKE 'T%'; -- Start with T
    
-- 2
SELECT
	*
FROM
	dim_customer
WHERE 
	first_name LIKE 'T%y'; -- Start with T and and with y
    
-- 3
SELECT
	*
FROM
	dim_customer
WHERE 
	first_name LIKE 'T__f%y'; -- Start with T and end with y but after 2 charater from T want f.
    
-- Order By
SELECT
	*
FROM
	dim_product
ORDER BY
	unit_price DESC;

-- Group by
SELECT
	category,
    AVG(unit_price) AS avg_price
FROM
	dim_product
GROUP BY
	category
HAVING
	avg_price > 500;


-- UPDATE
select * from market.cust_dimen;

UPDATE market.cust_dimen
SET Customer_Name = 'Sam Bahadur'
WHERE Cust_id = 'Cust_1';

DELETE FROM market.cust_dimen
WHERE Cust_id = 'Cust_1';
    
    
    
    
    
    
    
    
    
    
    
    
    