from data_service_layer import DataService
from data_layer import DataStore
from music_player import MusicPlayer
from presentation_layer import display_menu, get_user_choice, display_songs, display_status, get_song_choice

def main():
    data_store = DataStore()
    data_service = DataService(data_store)
    music_player = MusicPlayer(data_service)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            display_songs(music_player.view_songs())
        elif choice == '2':
            songs = music_player.view_songs()
            display_songs(songs)
            song_index = get_song_choice()
            music_player.play_song(song_index)
            print(f"Playing")
        elif choice == '3':
            music_player.stop_song()
            print("Music Stopped")
        elif choice == '4':
            print("Exiting the service ")
            break
        else:
            print("Invalid choice...")



if __name__ == '__main__':
    main()