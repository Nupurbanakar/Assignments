from view.gst_view import GSTView
from controllers.gst_controller import GSTController
from repository.item_repository import ItemRepository
from repository.category_repository import CategoryRepository
import mysql.connector

def main():
    model = []
    view = GSTView()
    controller = GSTController(model, view)

    self.connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gst_db",
        port="3306"
    )
    self.cursor = self.connection.cursor()

    item_repo = ItemRepository(db_url)
    category_repo = CategoryRepository(db_url)

    item_repo.add_item(item_type='Electronics', unit_price=1000, units=5)
    category_repo.add_category(name='Electronics', gst_rate=18)

    while True:
        try:
            units = int(input("Enter the no. of units (0 to exit): "))

            if units == 0:
                break

            item_type = input("Enter item type: ").capitalize()

            if item_type not in controller.gst_rates:
                new_category = input("New category! Enter GST rate: ")
                controller.add_category(item_type, float(new_category))

            unit_price = float(input("Enter initial unit price: "))
            controller.add_item(units, item_type, unit_price)

        except ValueError:
            print("Please enter valid numeric values.")

    net_gst, final_price, details = controller.calculate_total_gst()
    view.display_result(net_gst, final_price, details)

if __name__ == "__main__":
    main()
