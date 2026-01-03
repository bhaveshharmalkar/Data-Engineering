-- 1) Running Total / Running Sum
/*
1	1
2	3
3	7
4	15
*/

SELECT
	*,
    SUM(unit_price) OVER(ORDER BY launch_date) AS 'Running Total',
    SUM(unit_price) OVER(ORDER BY launch_date ROWS BETWEEN unbounded preceding AND current row) AS 'Running Total 1',
    SUM(unit_price) OVER(ORDER BY launch_date ROWS BETWEEN unbounded preceding AND unbounded following) AS 'Total',
    SUM(unit_price) OVER(PARTITION BY category ORDER BY launch_date ROWS BETWEEN unbounded preceding AND unbounded following) AS 'Partition Total'
FROM
	dim_product;
    
-- Rankings
SELECT
	unit_price,
    ROW_NUMBER() OVER(ORDER BY unit_price) AS 'row_number',
    RANK() OVER(ORDER BY unit_price) AS 'rank',
    DENSE_RANK() OVER(ORDER BY unit_price) AS 'dense_rank'
FROM
	dim_product;
    

SELECT
	unit_price,
    category,
    ROW_NUMBER() OVER(PARTITION BY category ORDER BY unit_price) AS 'row_number',
    RANK() OVER(PARTITION BY category ORDER BY unit_price) AS 'rank',
    DENSE_RANK() OVER(PARTITION BY category ORDER BY unit_price) AS 'dense_rank'
FROM
	dim_product;
