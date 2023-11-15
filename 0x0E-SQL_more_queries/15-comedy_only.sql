-- a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT ts.title
FROM tv_genres tvg
INNER JOIN tv_show_genres AS tsg
ON tvg.id = tsg.genre_id
INNER JOIN tv_shows ts
ON ts.id = tsg.show_id
WHERE tvg.name = "comedy"
GROUP BY ts.title
ORDER BY ts.title;
