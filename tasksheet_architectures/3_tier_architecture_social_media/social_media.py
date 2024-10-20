# Business Logic

class SocialMedia:

    def __init__(self, data_store):
        self.data_store = data_store

    def view_posts(self):
        return self.data_store.load_posts()

    def create_post(self, user, content):
        post = {"user": user, "content": content}
        self.data_store.save_post(post)

    def delete_post(self, user):
        self.data_store.delete_post(user)

    def edit_post(self, user, content):
        self.data_store.edit_post(user, content)