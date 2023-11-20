-- 17 for display all name & score is not only one
SELECT score, name
FROM second_table
WHERE name IN (
    SELECT name
    FROM second_table
    GROUP BY name
    HAVING COUNT(*) > 1
)
OR score IN (
    SELECT score
    FROM second_table
    GROUP BY score
    HAVING COUNT(*) > 1
) ORDER BY score DESC;