from model.item import Item
from database.db_connector import DatabaseConnector

class ItemController:

    db_connector = DatabaseConnector(host='localhost', user='root', port='3306', password='', database='gst_db')

    def __init__(self,model):
        self.gst_rates = None
        self.model = model

    def add_item(self, units, item_type, unit_price):
        item = Item(units, item_type, unit_price)
        self.model.append(item)  # Append the created Item to the model list

    def add_category(self, category, gst_rate):
        self.gst_rates[category] = gst_rate
