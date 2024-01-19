import mysql.connector

class CategoryRepository:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gst_db",
            port="3306"
        )
        self.cursor = self.connection.cursor()


        self.add_category("Example Category", 18.0)

    def add_category(self, name, gst_rate):

        query = "INSERT INTO categories (name, gst_rate) VALUES (%s, %s)"
        values = (name, gst_rate)

        self.cursor.execute(query, values)
        self.connection.commit()

    def get_category_by_id(self, category_id):
        query = "SELECT * FROM categories WHERE id = %s"
        values = (category_id,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            return {'id': result[0], 'name': result[1], 'gst_rate': result[2]}
        else:
            return None

    def get_all_categories(self):
        query = "SELECT * FROM categories"

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        categories = []
        for result in results:
            categories.append({'id': result[0], 'name': result[1], 'gst_rate': result[2]})

        return categories

    def update_category(self, category_id, new_name, new_gst_rate):
        query = "UPDATE categories SET name = %s, gst_rate = %s WHERE id = %s"
        values = (new_name, new_gst_rate, category_id)

        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_category(self, category_id):
        query = "DELETE FROM categories WHERE id = %s"
        values = (category_id,)

        self.cursor.execute(query, values)
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
