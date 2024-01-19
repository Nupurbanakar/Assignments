import mysql.connector

class ItemRepository:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gst_db",
            port="3306"
        )
        self.cursor = self.connection.cursor()

        self.create_items_table()

    def create_items_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            item_type VARCHAR(255) NOT NULL,
            unit_price DECIMAL(10, 2) NOT NULL,
            units INT NOT NULL
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def add_item(self, item_type, unit_price, units):
        query = "INSERT INTO items (item_type, unit_price, units) VALUES (%s, %s, %s)"
        values = (item_type, unit_price, units)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_item_by_id(self, item_id):
        query = "SELECT * FROM items WHERE id = %s"
        values = (item_id,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            return {'id': result[0], 'item_type': result[1], 'unit_price': result[2], 'units': result[3]}
        else:
            return None

    def get_all_items(self):
        query = "SELECT * FROM items"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        items = []
        for result in results:
            items.append({'id': result[0], 'item_type': result[1], 'unit_price': result[2], 'units': result[3]})

        return items

    def update_item(self, item_id, new_item_type, new_unit_price, new_units):
        query = "UPDATE items SET item_type = %s, unit_price = %s, units = %s WHERE id = %s"
        values = (new_item_type, new_unit_price, new_units, item_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_item(self, item_id):
        query = "DELETE FROM items WHERE id = %s"
        values = (item_id,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
