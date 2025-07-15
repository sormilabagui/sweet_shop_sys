class SweetShop:
    def __init__(self):
        self.sweets = []  # This will store our sweet dictionaries

    def add_sweet(self, name, category, price):
        sweet = {
            'name': name,
            'category': category,
            'price': price
        }
        self.sweets.append(sweet)
        print("current sweets list:", self.sweets)

    def get_all_sweets(self):
        return self.sweets
