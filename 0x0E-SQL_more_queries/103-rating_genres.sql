-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tvg.name, SUM(rt.rate) AS rating
FROM tv_genres tvg
INNER JOIN tv_show_genres tsg ON tsg.genre_id = tvg.id
INNER JOIN tv_show_ratings rt ON rt.show_id = tsg.show_id
GROUP BY tvg.name
ORDER BY rating DESC;
