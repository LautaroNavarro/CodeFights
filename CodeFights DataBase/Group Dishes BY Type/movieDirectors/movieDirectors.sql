#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE movieDirectors()
BEGIN
	SELECT DISTINCT director FROM moviesInfo WHERE year > 2000 AND oscars > 2 ORDER BY director;
END