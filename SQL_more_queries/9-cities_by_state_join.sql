-- 9-cities_by_state_join.sql

SELECT cities.id, cities.name, states.name FROM cities JOIN states
ON cities.state_id = states.id ORDER BY id ASC;
