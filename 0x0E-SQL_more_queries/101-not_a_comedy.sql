-- a script that lists all shows without the genre Comedy in the database
SELECT DISTINCT ts.title
FROM tv_shows AS ts
LEFT OUTER JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT OUTER JOIN tv_genres tvg ON tsg.genre_id = tvg.id
WHERE ts.id NOT IN(
	SELECT tsg.show_id FROM tv_show_genres tsg
	LEFT OUTER JOIN tv_genres tvg ON tsg.genre_id = tvg.id
	WHERE tvg.name = "comedy"
)
ORDER BY ts.title;
