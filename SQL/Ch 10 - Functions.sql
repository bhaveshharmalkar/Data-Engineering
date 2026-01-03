DELIMITER //
CREATE FUNCTION suqare(x INT)
RETURNS INT
DETERMINISTIC
BEGIN
	return x*x;
END //

DELIMITER ;


SELECT
	unit_price,
    suqare(unit_price)
FROM
	dim_product;