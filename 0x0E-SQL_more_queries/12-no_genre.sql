-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT s.tittle, tvg.genre_id
FROM tv_shows AS s LEFT JOIN tv_shows_genre AS tvg
ON s.id = tvg.show_id
WHERE tvg.genre_id is NULL
ORDER BY s.title, tvg.genre_id;
