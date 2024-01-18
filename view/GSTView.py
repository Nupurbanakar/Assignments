class GSTView:
    @staticmethod
    def display_result(net_gst, final_price, details):
        print("\nDetails:")
        for detail in details:
            print(detail)

        print(f"\nTotal Net GST amount: {net_gst}")
        print(f"Total Final selling price: {final_price}")
