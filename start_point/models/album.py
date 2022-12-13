class Album:

    def __init__(self, input_title, input_artist, input_genre, db_id = None):
        self.title = input_title
        self.artist = input_artist
        self.genre = input_genre
        self.id = db_id