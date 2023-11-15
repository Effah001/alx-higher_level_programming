--  a script that lists all shows contained in the database
SELECT s.title, tvg.genre_id
FROM tv_shows s LEFT OUTER JOIN tv_show_genres tvg
ON s.id = tvg.show_id
ORDER  BY s.title, tvg.genre_id;
