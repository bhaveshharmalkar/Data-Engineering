
WITH cte_table1 AS(
SELECT
	*,
    ROW_NUMBER() OVER(ORDER BY unit_price DESC) AS ranking
FROM
	dim_product
WHERE
	unit_price > (SELECT AVG(unit_price) FROM dim_product)
), cte_table2 AS(
SELECT
	*
FROM
	cte_table1
WHERE ranking <= 5
)
SELECT
	*
FROM
	cte_table2
WHERE
	category = 'Electronics';