--  a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT g.name
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
WHERE g.id NOT IN (
	SELECT sg.genre_id
	FROM tv_show_genres sg INNER JOIN tv_shows s ON s.id = sg.show_id
	WHERE s.title = "Dexter"
)
ORDER BY g.name;
