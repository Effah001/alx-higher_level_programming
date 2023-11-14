-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (desc)
SELECT city, AVG(value) as avg_tmp FROM temperatures GROUP BY city ORDER BY avg_tmp DESC;
