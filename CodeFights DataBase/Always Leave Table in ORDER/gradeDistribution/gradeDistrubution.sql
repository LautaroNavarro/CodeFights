#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE gradeDistribution()
BEGIN
        SELECT Name,ID FROM Grades 
        WHERE Final > ( Midterm1 * 25 / 100 + Midterm2 * 25 / 100 + Final * 50 / 100) AND
                Final > (Midterm1 * 50 / 100 + Midterm2 * 50 / 100)
        ORDER BY LEFT (name,3) asc,ID asc;
END