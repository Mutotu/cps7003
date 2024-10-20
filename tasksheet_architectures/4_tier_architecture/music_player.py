# Business Logic Layer

class MusicPlayer:
    def __init__(self, data_service):
        self.data_service = data_service
        self.current_song = None
    def view_songs(self):
        return self.data_service.get_songs()

    def play_song(self, song_index):
        songs = self.data_service.get_songs()
        self.current_song = songs[song_index]
        self.data_service.update_status(f"Playing {self.current_song['title']} by {self.current_song['artist']}")

    def stop_song(self):
        self.current_song = None
        self.data_service.update_status("Stopped")

    def get_status(self):
        return self.current_song.get_status()