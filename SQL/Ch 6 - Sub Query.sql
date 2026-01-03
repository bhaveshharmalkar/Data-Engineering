-- 1)
SELECT
	*
FROM
	dim_product
WHERE
	unit_price > (SELECT AVG(unit_price) FROM dim_product);
    
-- 2)
SELECT
	product_name
FROM
	(SELECT
	*
FROM
	dim_product
WHERE
	unit_price > (SELECT AVG(unit_price) FROM dim_product)) sb
WHERE 
	product_key = 1;