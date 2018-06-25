#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE mostExpensive()
BEGIN
	SELECT name FROM Products WHERE price * quantity = (SELECT MAX(price * quantity) FROM Products) ORDER BY name LIMIT 1;
END