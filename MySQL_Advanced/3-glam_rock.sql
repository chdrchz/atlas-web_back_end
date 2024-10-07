-- Queries for style as band name
-- and order by longevity
SELECT
    band_name,
    SUM(COALESCE(split, YEAR(CURDATE())) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
GROUP BY
    band_name
ORDER BY
    lifespan DESC;