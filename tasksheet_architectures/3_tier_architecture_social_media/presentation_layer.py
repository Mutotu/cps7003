def display_menu():
    print("Social Media Network")
    print("1. View Posts")
    print("2. Create Post")
    print("3. Delete Post")
    print("4 Edit Post")
    print("5. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def display_posts(posts):
    if not posts:
        print("No posts available.")
    else:
        for idx, post in enumerate(posts):
            print(f"{idx + 1}. {post['user']}: {post['content']}")

def get_post_details():
    user = input("Enter your username: ")
    content = input("Enter your post content: ")
    return user, content

def delete_post():
    return input("Enter your username: ")

def edit_post():
    user = input("Enter your username: ")
    content = input("Enter your content: ")
    return user, content