DELIMITER //
CREATE PROCEDURE first_procedure1(IN id INT, IN name VARCHAR(100), IN age INT)
BEGIN
	INSERT INTO customers1
    VALUES
    (id, name, age);
END //

DELIMITER ;

CALL ecom.first_procedure(1, 'john', 21);
