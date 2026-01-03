-- Transformatios

-- Numeric
SELECT
	*,
    ROUND(unit_price * 0.75, 2) AS discounted_price
FROM
	dim_product;
    
-- DATE
SELECT
	date,
    YEAR(date),
    MONTH(date),
    DAY(date),
    DAYNAME(date),
    ADDDATE(date, 2),
    SUBDATE(date, 2),
    DATEDIFF(DATE(utc_timestamp()), date) as total_days,
    DATE_FORMAT(date, '%W %M %e %Y') as converted
FROM
	dim_date;
    
-- Type Casting
SELECT
	CAST(customer_key AS char(100))
FROM
	dim_customer;
    
-- String functions
SELECT
    CONCAT(first_name, ' ', last_name) AS full_name,
    CONCAT_WS(' ', first_name, last_name, city) AS full_name,
    LENGTH(first_name) AS length_name,
    UPPER(first_name) AS uppercase,
    LOWER(first_name) AS lowercase,
    SUBSTRING(first_name, 1, 3) AS first_3,
    REPLACE(first_name, 'a', 'b') AS replace_a_b,
    LEFT(first_name, 3) AS left_3_char,
    RIGHT(first_name, 3) AS right_3_char,
    REVERSE(first_name) AS reverse_string,
    REPEAT(first_name, 2) AS repeat_name
FROM
	dim_customer;