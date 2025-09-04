# 1. Conteo diario
daily_crimes_query = """
SELECT report_dat::date AS day, COUNT(*) AS crimes
FROM raw_crimes_clean
GROUP BY day
ORDER BY day;
"""

# 2. Mapa (sample de 1000)
map_sample_query = """
SELECT latitude, longitude
FROM raw_crimes_clean
WHERE latitude IS NOT NULL
LIMIT 1000;
"""

# 3. Top 10 wards
wards_query = """
SELECT ward, COUNT(*) AS total_crimes
FROM raw_crimes_clean
GROUP BY ward
ORDER BY total_crimes DESC
LIMIT 10;
"""

# 4. Delitos más comunes
offense_query = """
SELECT offense, COUNT(*) AS total
FROM raw_crimes_clean
GROUP BY offense
ORDER BY total DESC
LIMIT 10;
"""

# 5. Distribución por turno
shift_query = """
SELECT shift, COUNT(*) AS total
FROM raw_crimes_clean
GROUP BY shift
ORDER BY total DESC;
"""