--  a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT tvg.name
FROM tv_genres tvg
INNER JOIN tv_show_genres tsg
ON tvg.id = tsg.genre_id
WHERE tvg.id NOT IN(SELECT tsg.genre_id
                    FROM tv_show_genres tsg INNER JOIN tv_shows ts 
                    ON ts.id = tsg.show.id
                    WHERE ts.title = "Dexter")
ORDER BY tvg.name;
