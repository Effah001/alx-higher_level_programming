-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT ts.title, SUM(rt.rate) AS rating
FROM tv_shows ts
INNER JOIN tv_show_ratings rt ON rt.show_id = ts.id
GROUP BY ts.title
ORDER BY rating DESC;
