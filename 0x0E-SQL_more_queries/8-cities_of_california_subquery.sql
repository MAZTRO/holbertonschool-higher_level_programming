-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- Find a specific state ID
SELECT id, name FROM cities a WHERE EXISTS (SELECT * FROM states b WHERE a.state_id = b.id) ORDER BY a.id ASC;
