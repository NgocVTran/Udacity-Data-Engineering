
# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays(
    songplay_id serial constraint songplay_pk primary key,
    start_time timestamp references time (start_time),
    user_id int references users (user_id),
    level varchar not null,
    song_id varchar references songs (song_id),
    artist_id varchar references artists (artist_id),
    session_id int not null, 
    location varchar,
    user_agent text
)
""")

user_table_create = ("""
create table if not exists users(
    user_id int constraint users_pk primary key,
    first_name varchar,
    last_name varchar,
    gender char(1),
    level varchar not null
)
""")

song_table_create = ("""
create table if not exists songs(
    song_id varchar constraint songs_pk primary key,
    title varchar,
    artist_id varchar references artists (artist_id),
    year int check (year >= 0),
    duration float
)
""")

artist_table_create = ("""
create table if not exists artists(
    artist_id varchar constraint artist_pk primary key,
    name varchar,
    location varchar,
    latitude decimal(9,6),
    longitude decimal(9,6)
)
""")

time_table_create = ("""
create table if not exists time(
    start_time timestamp constraint time_pk primary key,
    hour int not null check (hour >= 0),
    day int not null check (day >= 0),
    week int not null check (week >= 0),
    month int not null check (month >= 0),
    year int not null check (year >= 0),
    weekday varchar not null
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
insert into songplays values (default, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
insert into users(user_id, first_name, last_name, gender, level) 
values (%s, %s, %s, %s, %s) 
on conflict (user_id) do update 
set level = excluded.level
""")

song_table_insert = ("""
insert into songs (song_id, title, artist_id, year, duration) 
values (%s, %s, %s, %s, %s) 
on conflict (song_id) do nothing
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location, latitude, longitude) values (%s, %s, %s, %s, %s) 
on conflict (artist_id) do update set 
location = excluded.location,
latitude = excluded.latitude,
longitude = excluded.longitude
""")

time_table_insert = ("""
insert into time values (%s, %s, %s, %s, %s, %s, %s) on conflict (start_time) do nothing
""")

# FIND SONGS

song_select = ("""
select song_id, artists.artist_id
from songs join artists on songs.artist_id = artists.artist_id
where songs.title = %s
and artists.name = %s
and songs.duration = %s
""")


# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
