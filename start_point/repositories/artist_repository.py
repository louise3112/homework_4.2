from db.run_sql import run_sql
from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    db_list = run_sql(sql)

    for row in db_list:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    
    return artists

def select(id):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    db_list = run_sql(sql, values)

    if db_list:
        db_row = db_list[0]
        artist = Artist(db_row['name'], db_row['id'])
    
    return artist


def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)