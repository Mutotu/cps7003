class DataService:
    def __init__(self, data_store):
        self.data_store =data_store

    def get_songs(self):
        return self.data_store.load_songs()

    def update_status(self, status):
        self.data_store.save_status(status)

    def get_status(self):
        return self.data_store.get_status()