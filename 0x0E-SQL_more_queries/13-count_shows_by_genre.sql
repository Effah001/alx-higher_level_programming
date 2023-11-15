SELECT tvg.name AS genre, COUNT(tvg.name) AS nunber_of_shows
FROM tv_genres tvg
INNER JOIN tv_show_genres AS tsg
ON tvg.id = tsg.genre_id
INNER JOIN tv_shows AS ts
ON ts.id = tsg.show_id
GROUP BY tvg.name
ORDER BY number_of_shows DESC;
