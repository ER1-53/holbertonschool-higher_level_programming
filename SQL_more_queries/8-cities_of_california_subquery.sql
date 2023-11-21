-- 8-cities_of_california_subquery.sql

SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name='california') ORDER BY id ASC;
