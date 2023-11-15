--  a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tvg.name
FROM tv_genres tvg
INNER JOIN tv_show_genres tsg
	ON tvg.id = tsg.genre_id
INNER JOIN tv_shows ts
	ON ts.id = tsg.show_id
	WHERE ts.title = "Dexter"
GROUP BY tvg.name
ORDER BY tvg.name;
