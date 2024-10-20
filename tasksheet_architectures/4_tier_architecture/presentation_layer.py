def display_menu():
    print("Music Streaming Service")
    print("1: View Songs, 2: Play Song, 3: Stop Song, 4: Exit")

def get_user_choice():
    return input("Enter your choice: ")

def display_songs(songs):
    print("Available songs:")
    if not songs:
        print("No song available")
        return
    for idx, song in enumerate(songs):
        print(f"{idx+1}: {song['title']} by {song['artist']}")

def get_song_choice():
    return int(input("Enter song number: ")) - 1

def display_status(status):
    print(f"Status: {status}")