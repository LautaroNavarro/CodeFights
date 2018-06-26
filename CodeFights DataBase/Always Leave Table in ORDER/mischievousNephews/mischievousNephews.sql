#By Lautaro Navarro

/*Please add ; after each select statement*/
CREATE PROCEDURE mischievousNephews()
BEGIN
	SELECT WEEKDAY(mischief_date) AS weekday,
           mischief_date,
           author,
           title 
    FROM mischief 
    ORDER BY weekday ASC,
    (CASE 
        WHEN author LIKE 'H%' THEN 1
        WHEN author LIKE 'D%' THEN 2
        ELSE 3 
        END ),
    mischief_date,
    title;
END