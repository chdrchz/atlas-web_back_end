-- Queries for country and fans
-- and order by fan numbers in desc order
SELECT 
    origin,
    SUM(fans) AS nb_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    nb_fans DESC;