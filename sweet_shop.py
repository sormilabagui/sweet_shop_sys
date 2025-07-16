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
        return False
