-- a script that lists all shows
SELECT s.title, tvg.genre_id
FROM tv_shows AS s
INNER JOIN tv_shows_genres AS tvg ON s.id = tvg.show_id
ORDER BY s.title, tvg.genre_id;
