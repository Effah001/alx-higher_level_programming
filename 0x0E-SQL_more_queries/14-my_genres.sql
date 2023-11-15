--  a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tvg.name
FROM tv_genres AS tvg
INNER JOIN tv_shows_genres AS tsg
ON tvg.id = tsg.genre_id
INNER JOIN tv_shows ts
ON ts.id = tsg.show_id
WHERE ts.title = "DEXTER"
ORDER BY tvg.name;
