#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE newsSubscribers()
BEGIN
	SELECT DISTINCT subscriber FROM full_year WHERE newspaper LIKE '%Daily%'
    UNION
    SELECT DISTINCT subscriber FROM half_year WHERE newspaper LIKE '%Daily%' ORDER BY subscriber;
END