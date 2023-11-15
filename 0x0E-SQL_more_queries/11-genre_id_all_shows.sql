--  a script that lists all shows contained in the database
SELECT s.title, tvg.genre_id
FROM tv_shows AS s LEFT OUTER JOIN tv_show_genres AS tvg
ON s.id = tvg.show_id
ORDER  BY s.title, tvg.genre_id;
