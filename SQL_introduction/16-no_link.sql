-- 16-no_link.sql methode KK SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;

SELECT score, name FROM second_table WHERE name IS NOT NULL GROUP BY name, score ORDER BY score DESC;
