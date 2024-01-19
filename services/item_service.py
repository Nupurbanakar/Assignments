from repository.item_repository import ItemRepository

class ItemService:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    def add_item(self, item_type, unit_price, units):
        self.item_repository.add_item(item_type, unit_price, units)

    def get_item_by_id(self, item_id):
        return self.item_repository.get_item_by_id(item_id)

    def get_all_items(self):
        return self.item_repository.get_all_items()

    def update_item(self, item_id, new_item_type, new_unit_price, new_units):
        self.item_repository.update_item(item_id, new_item_type, new_unit_price, new_units)

    def delete_item(self, item_id):
        self.item_repository.delete_item(item_id)
