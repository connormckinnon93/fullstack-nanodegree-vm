-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create the players table
-- id is the primary key and auto incremented
-- time could be a useful column for debugging
CREATE TABLE players ( id SERIAL PRIMARY KEY,
                     name TEXT NOT NULL,
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Create the matches table
-- id is the primary key and auto incremented
-- can't use a multi-column primary
-- because winners and losers could face each other more than once
-- record the winner and loser for each unique match
-- time could be a useful column for debugging
CREATE TABLE matches ( id SERIAL PRIMARY KEY,
					 winner INT REFERENCES players(id),
					 loser INT REFERENCES players(id),
                     time TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

-- Create the view for standings
-- Inspired by the discussion here: https://discussions.udacity.com/t/problem-with-playerstandings-function/161726/6
-- Without this discussion I wouldn't have been able to fix a view with subselects
-- still would to see if I could solve this with left join
CREATE VIEW standings AS
	SELECT players.id, players.name,
		   (SELECT COUNT(matches.winner) FROM matches WHERE players.id = matches.winner) AS num_wins,
		   (SELECT COUNT(*) FROM matches WHERE players.id = matches.winner or players.id = matches.loser) AS num_matches
	FROM players
	ORDER BY num_wins DESC, num_matches DESC