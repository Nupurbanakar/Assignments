from model import Product

class GSTController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.gst_rates = {
            "Food grains": 0,
            "Furniture": 5,
            "Electronics": 18,
            "Cosmetics": 28
        }

    def add_item(self, units, item_type, unit_price):
        item = Product(units, item_type, unit_price)
        self.model.append(item)  # Append the created Product to the model list

    def add_category(self, category, gst_rate):
        self.gst_rates[category] = gst_rate

    def calculate_total_gst(self):
        total_net_gst = 0
        total_final_price = 0
        details = []

        for item in self.model:
            gst_rate = self.gst_rates.get(item.item_type, 0)

            net_gst_per_unit = item.calculate_net_gst_per_unit(gst_rate)
            final_price_per_unit = item.calculate_final_selling_price(gst_rate)

            total_net_gst += net_gst_per_unit * item.units
            total_final_price += final_price_per_unit * item.units

            details.append(f"{item.item_type}: Net GST per unit - {net_gst_per_unit}, Final selling price - {final_price_per_unit}")

        return round(total_net_gst, 2), round(total_final_price, 2), details