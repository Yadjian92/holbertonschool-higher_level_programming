-- Script that lists all Comedy shows in the database
-- Results are sorted in ascending order by show title
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
