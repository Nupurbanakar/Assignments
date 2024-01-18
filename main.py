from view.gst_view import GSTView
from controllers.gst_controller import GSTController

def main():
    model = []
    view = GSTView()
    controller = GSTController(model, view)

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
