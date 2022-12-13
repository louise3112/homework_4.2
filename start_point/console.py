from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repo
import repositories.artist_repository as artist_repo

artist_repo.delete_all()

artist_1 = Artist("Shania Twain")
artist_2 = Artist("John Mayer")
artist_3 = Artist("Beyonce")

artist_repo.save(artist_1)
artist_repo.save(artist_2)
artist_repo.save(artist_3)

all_artists = artist_repo.select_all()
for artist in all_artists:
    print(artist.__dict__)

specific_artist = artist_repo.select(8)
print(specific_artist.__dict__)


album_repo.delete_all()

album_1_artist = artist_repo.select(7)
album_1 = Album("Come On Over", album_1_artist, "Country")
album_2_artist = artist_repo.select(8)
album_2 = Album("Continuum", album_2_artist, "Blues / Rock")

album_repo.save(album_1)
album_repo.save(album_2)

all_albums = album_repo.select_all()
for album in all_albums:
    print(album.__dict__)

specific_album = album_repo.select(5)
print(specific_album.__dict__)


albums_by_artist_id_7 = album_repo.select_album_by_artist(7)
for album in albums_by_artist_id_7:
    print(album.__dict__)

artist_4 = Artist("Kelly Rowland", 9)
artist_repo.update(artist_4)
updated_artist = artist_repo.select(9)
print(updated_artist.__dict__)

artist_repo.delete(9)
deleted_artist = artist_repo.select(9)
print(deleted_artist)

album_3_artist = artist_repo.select(8)
album_3 = Album("xo", album_3_artist, "Rock / Blues", 6)
album_repo.update(album_3)
updated_album = album_repo.select(6)
print(updated_album.__dict__)

album_repo.delete(6)
deleted_album = album_repo.select(6)
print(deleted_album)