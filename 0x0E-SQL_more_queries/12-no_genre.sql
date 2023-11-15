-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT ts.title, tvg.genre_id
FROM tv_shows AS ts LEFT JOIN tv_shows_genre AS tvg
ON ts.id = tvg.show_id
WHERE tvg.genre_id is NULL
ORDER BY ts.title, tvg.genre_id;
