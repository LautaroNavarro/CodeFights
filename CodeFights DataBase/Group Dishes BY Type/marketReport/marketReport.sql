#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE marketReport()
BEGIN
	SELECT IFNULL(country, 'Total:') as country, count(*) AS competitors FROM foreignCompetitors GROUP BY country WITH ROLLUP;
END