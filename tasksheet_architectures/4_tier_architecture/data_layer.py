class DataStore:

    def __init__(self):
        self.songs = [
            {'title': 'Bohemian Rapsody', 'artist': 'Queen'},
            {'title': 'Smooth Criminal', 'artist': 'Michael Jackson'},
            {'title': 'In the Mood', 'artist': 'Glenn Miller'}
        ]
        self.status = None

    def load_songs(self):
        return self.songs

    def save_status(self, status):
        self.status = status

    def get_status(self):
        return self.status