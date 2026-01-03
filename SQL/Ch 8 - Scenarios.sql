-- Scenario 1 (Finding the Nth value)

SELECT
	*
FROM
	(SELECT *, ROW_NUMBER() OVER(ORDER BY unit_price DESC) AS ranking FROM dim_product) sub
WHERE
	ranking <= 5;

-- OR 

WITH ctes AS (
SELECT
	*,
    ROW_NUMBER() OVER(ORDER BY unit_price DESC) AS ranking
FROM
	dim_product
)
SELECT
	*
FROM
	ctes
WHERE ranking <= 5;


-- Scenario 2 (Finding the Top 3 value from every category)
WITH ctes AS (
SELECT
	*,
    ROW_NUMBER() OVER(PARTITION BY category ORDER BY unit_price DESC) AS ranking
FROM
	dim_product
)
SELECT
	*
FROM
	ctes
WHERE ranking = 3;


-- Scenario 3 (Removing Duplicates)
WITH ctes AS(
SELECT
	*,
    ROW_NUMBER() OVER(PARTITION BY id) AS check_dups
FROM
	customers
)
SELECT
	id, name, email
FROM
	ctes
WHERE
	check_dups = 1;
    

-- Scenario 4 (LAG and LEAD)
SELECT
	*,
    LAG(temp, 1, 'NA') OVER(ORDER BY Day) AS prev_day,
    LEAD(temp, 1, 'NA') OVER(ORDER BY Day) AS next_day,
    LAG(temp, 2, 'NA') OVER(ORDER BY Day) AS prev_2day
FROM
	weather;