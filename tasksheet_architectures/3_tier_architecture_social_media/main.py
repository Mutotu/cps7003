from data_store import DataStore
from social_media import SocialMedia
from presentation_layer import display_menu, get_post_details, get_user_choice, display_posts, delete_post, edit_post

def main():
    data_store = DataStore()
    social_media = SocialMedia(data_store)
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == '1':
            posts = social_media.view_posts()
            display_posts(posts)
        elif choice == '2':
            user, content = get_post_details()
            social_media.create_post(user, content)
            print("Post created successfully!")
        elif choice == '3':
            user = delete_post()
            social_media.delete_post(user)
        elif choice == '4':
            user, content = edit_post()
            social_media.edit_post(user, content)
        elif choice == '5':
            print("Exiting the platform. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()