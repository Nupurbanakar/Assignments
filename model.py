class Product:
    def __init__(self, units, item_type, unit_price):
        self.units = units
        self.item_type = item_type
        self.unit_price = unit_price

    def calculate_net_gst_per_unit(self, gst_rate):
        return round((gst_rate / 100) * self.unit_price,2)

    def calculate_final_selling_price(self, gst_rate):
        net_gst_per_unit = self.calculate_net_gst_per_unit(gst_rate)
        return self.unit_price + net_gst_per_unit
