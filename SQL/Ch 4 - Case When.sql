select * from dim_product;

-- 1)
SELECT
	*,
	CASE
		WHEN unit_price <= 100 THEN 'Affordable'
        WHEN unit_price BETWEEN 100 AND 200 THEN 'Mid Range'
		ELSE 'Expensive'
	END AS 'Flag'
FROM
	dim_product;

-- 2)
SELECT
	*,
	CASE
		WHEN unit_price <= 100 AND Category = 'Clothing' THEN 'Affordable'
        WHEN unit_price <= 200 AND Category = 'Clothing' THEN 'Mid Range'
        WHEN unit_price > 200 AND Category = 'Clothing' THEN 'Expensive'
		ELSE CONCAT('Not For ',category)
	END AS 'Flag'
FROM
	dim_product;
    
-- 3)

SELECT
	*,
	CASE 
		WHEN MONTH(launch_date) IN (1, 2, 12) THEN 'Winter'
        WHEN MONTH(launch_date) IN (3, 4, 5) THEN 'Summer'
        WHEN MONTH(launch_date) IN (6, 7, 8) THEN 'Mansoon'
        ELSE 'Festive'
	END AS Season
	END AS Season
FROM
	dim_product;