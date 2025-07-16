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
