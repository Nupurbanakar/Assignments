class GST:
    def __init__(self):
        self.gst_rates = {
            "Food grains": 0,
            "Furniture": 5,
            "Electronics": 18,
            "Cosmetics": 28
        }
        self.items = []

    def add_item(self,units,item_type,unit_price):
        self.items.append(units,item_type,unit_price)

    def add_category(self,category, gst_rate):
        self.gst_rates[category] = gst_rate

    @staticmethod
    def calculate_net_gst_per_unit(gst_rate, unit_price):
        return (gst_rate/ 100) * unit_price

    def calculate_final_selling_price(self,gst_rate, unit_price):
        net_gst_per_unit= self.calculate_net_gst_per_unit(gst_rate,unit_price)
        return unit_price + net_gst_per_unit

    def calculate_total_gst(self):
        total_net_gst = 0
        total_final_price = 0

        for item in self.items:
            gst_rate = self.gst_rates.get(item.item_type, 0)
            net_gst_per_unit = (gst_rate / 100) * item.unit_price
            final_price_per_unit = item.unit_price + net_gst_per_unit

            total_net_gst += net_gst_per_unit * item.units
            total_final_price += final_price_per_unit * item.units

            print(f"{item.item_type}: Net GST per unit-{net_gst_per_unit},Final selling price - {final_price_per_unit}")

        return round(total_net_gst, 2), round(total_final_price, 2)

def main():
    gst_calculator = GSTCalculator()

    while True:
        try:
            units = int(input("Enter the number of units (0 to exit): "))

            if units == 0:
                break

            item_type = input("Enter the type of item: ").capitalize()

            if item_type not in gst_calculator.gst_rates:
                # Dynamically add new category
                new_category = input("New category! Enter GST rate for the category: ")
                gst_calculator.add_category(item_type, float(new_category))

                unit_price = float(input("Enter the initial unit price for the new category: "))
                item = Item(units, item_type, unit_price)
            else:
                unit_price = float(input("Enter the initial unit price: "))
                item = Item(units, item_type, unit_price)

            gst_calculator.add_item(item)

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    net_gst, final_price = gst_calculator.calculate_total_gst()

    print(f"\nTotal Net GST amount: {net_gst}")
    print(f"Total Final selling price: {final_price}")

if __name__ == "__main__":
    main()
