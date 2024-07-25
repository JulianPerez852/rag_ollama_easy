from repositories.indexes_repository import IndexesRepository

class IndexesManagerService:
    def __init__(self, indexes_repositorie: IndexesRepository):
        self.indexes_manager = indexes_repositorie

    def create_index(self, path):
        return self.indexes_manager.create_indexes(path)
    
    def save_index(self, index, name):
        path = "indexes/" + name
        return self.indexes_manager.save_indexes(index, path)
    
    def load_index(self, path):
        return self.indexes_manager.load_indexes(path)
    
    def delete_index(self, index):
        return self.indexes_manager.delete_indexes(index)
    
    def update_index(self, index):
        return self.indexes_manager.update_indexes(index)
    
    