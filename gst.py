class Product:
    def __init__(self, units, item_type, unit_price):
        self.units = units
        self.item_type = item_type
        self.unit_price = unit_price

    def calculate_net_gst_per_unit(self, gst_rate):
        return (gst_rate / 100) * self.unit_price

    def calculate_final_selling_price(self, gst_rate):
        net_gst_per_unit = self.calculate_net_gst_per_unit(gst_rate)
        return self.unit_price + net_gst_per_unit


class GSTCalculator(Product):
    def __init__(self):
        super().__init__(0, "", 0)  # Initialize with default values
        self.gst_rates = {}

    def add_item(self, units, item_type, unit_price):
        super().__init__(units, item_type, unit_price)

    def add_category(self, category, gst_rate):
        self.gst_rates[category] = gst_rate

    def calculate_total_gst(self):
        total_net_gst = 0
        total_final_price = 0

        for item_type, gst_rate in self.gst_rates.items():
            net_gst_per_unit = super().calculate_net_gst_per_unit(gst_rate)
            final_price_per_unit = super().calculate_final_selling_price(gst_rate)

            total_net_gst += net_gst_per_unit * self.units
            total_final_price += final_price_per_unit * self.units

            print(f"{item_type}: Net GST per unit - {net_gst_per_unit}, Final selling price - {final_price_per_unit}")

        return round(total_net_gst, 2), round(total_final_price, 2)

    def process_purchase(self, units, item_type, unit_price):
        self.add_item(units, item_type, unit_price)

    def process_new_category(self, category, gst_rate):
        self.add_category(category, gst_rate)


def main():
    gst_calculator = GSTCalculator()

    while True:
        try:
            units = int(input("Enter the no. of units (0 to exit): "))

            if units == 0:
                break

            item_type = input("Enter the type of item: ").capitalize()

            if item_type not in gst_calculator.gst_rates:
                # Dynamically add new category
                new_category = input("New category! Enter GST rate: ")
                gst_calculator.process_new_category(item_type, float(new_category))

            unit_price = float(input("Enter initial unit price: "))
            gst_calculator.process_purchase(units, item_type, unit_price)

        except ValueError:
            print("Please enter valid numeric values.")

    net_gst, final_price = gst_calculator.calculate_total_gst()

    print(f"\nTotal Net GST amount: {net_gst}")
    print(f"Total Final selling price: {final_price}")


if __name__ == "__main__":
    main()
