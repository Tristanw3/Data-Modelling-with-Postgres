# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays(
        songplay_id SERIAL PRIMARY KEY NOT NULL, 
        start_time BIGINT, 
        user_id INT, 
        level TEXT, 
        song_id TEXT, 
        artist_id TEXT, 
        session_id INT, 
        location TEXT, 
        user_agent TEXT
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INT NOT NULL, 
        first_name TEXT, 
        last_name TEXT, 
        gender TEXT, 
        level TEXT,
        PRIMARY KEY( user_id )
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs(
        song_id TEXT NOT NULL, 
        title TEXT, 
        artist_id TEXT NOT NULL, 
        year INT, 
        duration DECIMAL,
        PRIMARY KEY( song_id )
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists(
        artist_id TEXT NOT NULL,
        name TEXT, 
        location TEXT,
        latitude INT, 
        longitude INT,
        PRIMARY KEY (artist_id)
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time(
        start_time BIGINT NOT NULL, 
        hour INT, 
        day INT, 
        week INT, 
        month INT, 
        year INT, 
        weekday INT,
        PRIMARY KEY (start_time)
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) 
    DO UPDATE SET
    (level) = (EXCLUDED.level)
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) 
    DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) 
    DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, s.artist_id
    FROM songs s
    INNER JOIN artists ON s.artist_id = artists.artist_id
    WHERE s.title = %s
    AND name = %s
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]