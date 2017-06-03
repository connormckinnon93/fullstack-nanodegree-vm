#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

# import psql interface and a sanitization library
import psycopg2, bleach
DBNAME = "tournament"


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    
    return psycopg2.connect(database=DBNAME)


def push_to_db(query, string=None):
    """Create a cursor and commit changes to the database."""

    # Create the db connection
    db = connect()
    # Create a cursor for the db connection
    c = db.cursor()
    # Execute a query with a substitution string if its available
    c.execute(query, string)
    # Commit the changes to the db
    db.commit()
    # Close the connection
    db.close()


def pull_from_db(query):
    """Create a cursor and execute a fetchall and return the results"""

    # Create the db connection
    db = connect()
    # Create a cursor for the db connection
    c = db.cursor()
    # Execute a query with a substitution string if its available
    c.execute(query)
    # Fetch the results of the query
    result = c.fetchall()
    # Close the connection
    db.close()
    # Return the results of the fetch
    return result


def deleteMatches():
    """Remove all the match records from the database."""

    push_to_db("delete from matches")


def deletePlayers():
    """Remove all the player records from the database."""

    push_to_db("delete from players")


def countPlayers():
    """Returns the number of players currently registered."""

    count = pull_from_db("select count(*) as num from players")
    # Return the player count from the results of the pull_from_db
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    push_to_db("insert into players (name) values (%s)", (bleach.clean(name),))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    # Get the current standings from the view we created in tournament.sql
    standings = pull_from_db("select * from standings")
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    push_to_db("insert into matches (winner, loser) values (%s, %s)", ((bleach.clean(winner),), (bleach.clean(loser),)))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # This function is based off this discussion here: https://discussions.udacity.com/t/swissparings-function/203520/5
    # Wouldn't have known to use Zip without it
    # Still would love to figure out how to do this with psql

    # Create array for listing the pairings
    pairings = []
    # Create array to save the even numbered player
    players_even = []
    # Create array to save the odd numbered player
    players_odd = []

    # Return the current player standings
    standings = playerStandings()

    # Initialize count to use in the for loop
    i = 0
    # Start cycling through the players in order
    for player in standings:
        # Add to the even array if even
        if i % 2 == 0:
            players_even.append([player[0],player[1]])
        # Add to the odd array if even
        else:
            players_odd.append([player[0],player[1]])
        # Increase the count after each player is added
        i += 1

    # Zip the two lists together and cycle
    for i,j in zip(players_even, players_odd):
        # Create a pair from the information in the zipped list
        pair = ([i[0],i[1],j[0],j[1]])
        # Append the pair to pairing array
        pairings.append(pair)

    # Return the pairings
    return pairings


