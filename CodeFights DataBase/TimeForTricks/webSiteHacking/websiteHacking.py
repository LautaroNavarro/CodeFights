#By Lautaro Navarro

CREATE PROCEDURE websiteHacking()
    SELECT id,login,name
    FROM users
    WHERE type='user'
    OR 1 = 1
    ORDER BY id