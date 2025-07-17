class SweetShop:
    def __init__(self):
        self.sweets = []  # This will store our sweet dictionaries

    def add_sweet(self, sweet_id, name, category, price, quantity):
        sweet = {
            'id' : sweet_id,
            'name': name,
            'category': category,
            'price': price,
            'qty' : quantity
        }
        self.sweets.append(sweet)
        print("current sweets list:", self.sweets)

    def get_all_sweets(self):
        return self.sweets

    def delete_sweet(self, sweet_id):
        for sweet in self.sweets:
            if sweet['id'] == sweet_id:
                self.sweets.remove(sweet)
                return True
        raise ValueError(f"No sweet found with ID: {sweet_id}")

    def view_sweets(self):
        if not self.sweets:
            print("No sweets available.")
        else:
            print("Available sweets:")
            for sweet in self.sweets:
                print(f"ID: {sweet['id']}, Name: {sweet['name']}, Category: {sweet['category']}, Price: ₹{sweet['price']}, Qty: {sweet['qty']}")

    def search_sweets_by_name(self, name):
        return [sweet for sweet in self.sweets if sweet['name'].lower() == name.lower()]

    def search_sweet_by_id(self, sweet_id):
        for sweet in self.sweets:
            if sweet['id'] == sweet_id:
                return sweet
        return None  # or raise ValueError("Sweet not found") if test expects error

    def search_sweets_by_category(self, category):
        return [sweet for sweet in self.sweets if sweet['category'].lower() == category.lower()]

    def search_sweets_by_price_range(self, min_price, max_price):
        return [sweet for sweet in self.sweets if min_price <= sweet['price'] <= max_price]


    def sort_sweets_by_price(self):
        return sorted(self.sweets, key=lambda x: x['price'])

    def sort_sweets_by_quantity(self):
        return sorted(self.sweets, key=lambda x: x['qty'])


    def purchase_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet['id'] == sweet_id:
                if sweet['qty'] >= quantity:
                    sweet['qty'] -= quantity
                    return
                else:
                    raise ValueError(f"Not enough stock for sweet ID: {sweet_id}")
        raise ValueError(f"No sweet found with ID: {sweet_id}")

    def restock_sweet(self, sweet_id, quantity):
        for sweet in self.sweets:
            if sweet['id'] == sweet_id:
                sweet['qty'] += quantity
                return
        raise ValueError(f"No sweet found with ID: {sweet_id}")
