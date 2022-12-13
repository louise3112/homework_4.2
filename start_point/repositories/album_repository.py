from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repo

def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    db_list = run_sql(sql)

    for row in db_list:
        artist = artist_repo.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['id'])
        albums.append(album)
    
    return albums

def select(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    db_list = run_sql(sql, values)

    if db_list:
        db_row = db_list[0]
        artist = artist_repo.select(db_row['artist_id'])
        album = Album(db_row['title'], artist, db_row['genre'], db_row['id'])
    
    return album


def select_album_by_artist(artist_id):
    albums = []

    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist_id]
    db_list = run_sql(sql, values)

    if db_list:
        for row in db_list:
            artist = artist_repo.select(row['artist_id'])
            album = Album(row['title'], artist, row['genre'], row['id'])
            albums.append(album)
    
    return albums

def update(album):
    sql = "UPDATE albums SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

