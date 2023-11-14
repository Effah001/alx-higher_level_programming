-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (desc)
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY 2 DESC;
