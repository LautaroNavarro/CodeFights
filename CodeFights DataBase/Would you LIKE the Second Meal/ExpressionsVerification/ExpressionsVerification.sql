#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE expressionsVerification()
BEGIN
	SELECT * FROM expressions WHERE   IF(operation = "+", a + b,
                                      IF(operation = "-", a - b,
                                      IF(operation = "*", a * b, a / b)))  = c;
END