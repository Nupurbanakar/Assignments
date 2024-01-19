from repository.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def add_category(self, name, gst_rate):
        self.category_repository.add_category(name, gst_rate)

    def get_category_by_id(self, category_id):
        self.category_repository.get_category_by_id(category_id)

    def get_all_categories(self):
        self.category_repository.get_all_categories(self)

    def update_category(self, category_id, new_name, new_gst_rate):
        self.category_repository.update_category(category_id,new_name,new_gst_rate)

    def delete_category(self, category_id):
        self.category_repository.delete_category(category_id)
