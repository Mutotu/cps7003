# Data Store Layer

class DataStore:
    def __init__(self):
        self.posts = []

    def load_posts(self):
        return self.posts

    def save_post(self, post):
        self.posts.append(post)

    def delete_post(self, user):
        for post in self.posts:
            if post['user'] == user:
                self.posts.remove(post)
                print("Post deleted")
            else:
                print("User not found")

    def edit_post(self, user, content):
        for post in self.posts:
            if post['user'] == user:
                post['content'] = content
                print("Post edited")
            else:
                print("User not found")