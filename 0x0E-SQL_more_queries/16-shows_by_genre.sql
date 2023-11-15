-- a script that lists all shows, and all genres linked to that show
SELECT ts.title, tvg.name
FROM tv_shows ts
LEFT OUTER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
LEFT OUTER JOIN tv_genres tvg
ON tvg.id = tsg.genre_id
ORDER BY ts.title, tvg.name;
