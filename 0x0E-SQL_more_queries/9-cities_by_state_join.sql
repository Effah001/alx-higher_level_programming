-- a script that lists all cities contained in the database
SELECT cities.id, cities.name. state.name
FROM cities JOIN state
ON cities.state_id = state.id
ORDER BY cities.id;
