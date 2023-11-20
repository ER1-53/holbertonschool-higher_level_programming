-- 16-no_link.sql

SELECT score, name FROM second_table WHERE name IS NOT NULL GROUP BY name, score ORDER BY score DESC;
