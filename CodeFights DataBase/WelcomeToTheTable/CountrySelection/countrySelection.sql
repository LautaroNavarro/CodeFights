#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE countriesSelection()
BEGIN
	SELECT name, continent, population FROM countries WHERE continent = 'Africa';
END