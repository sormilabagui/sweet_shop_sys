from sweet_shop import SweetShop

def display_sweets(sweets):
    if not sweets:
        print("No sweets to display.")
        return

    print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Qty':<5}")
    print("-" * 55)
    for sweet in sweets:
        print(f"{sweet['id']:<5} {sweet['name']:<15} {sweet['category']:<15} ₹{sweet['price']:<10} {sweet['qty']:<5}")


def main():
    shop = SweetShop()


    while True:
        print("\n -----Sweet shop Management System---------")
        print("1. Add sweet")
        print("2. Delete sweet")
        print("3. View all sweets")
        print("4. Search")
        print("5. Sort")
        print("6. Purchase")
        print("7. Restock")
        print("0. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            try:
                sweet_id = int(input("Enter sweet ID: "))
                name = input("Enter sweet name: ")
                category = input("Enter category: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                shop.add_sweet(sweet_id, name, category, price, quantity)
                print(" Sweet added successfully!")
            except Exception as e:
                print(f" Error: {e}")

        elif ch == "2":
            try:
                sweet_id = int(input("Enter sweet ID to delete: "))
                shop.delete_sweet(sweet_id)
                print("Sweet deleted")
            except Exception as e:
                print(f"Error: {e}")
        
        elif ch == "3":
            sweets = shop.view_sweets()
            

        elif ch == "4":
            while True:
                print("\n Search Menu")
                print("1. Search by ID")
                print("2. Search by Name")
                print("3. Search by Category")
                print("4. Search by Price Range")
                print("0. Back to Main Menu")
                search_choice = input("Choose search option: ")

                if search_choice == "1":
                    try:
                        sweetid = int(input("Enter ID:"))
                        results = shop.search_sweet_by_id(sweetid)
                        if results:
                            display_sweets(results)
                        else:
                            print("no sweet found with that id.")
                    except Exception as e:
                        print("invalid ID", e)

                elif search_choice == "2":
                    name = input("Enter name: ")
                    results = shop.search_sweets_by_name(name)
                    display_sweets(results)

                elif search_choice == "3":
                    category = input("Enter category: ")
                    results = shop.search_sweets_by_category(category)
                    if results:
                        display_sweets(results)
                    else:
                        print("no sweet found with that id.")

                elif search_choice == "4":
                    try:
                        min_p = float(input("Min price: "))
                        max_p = float(input("Max price: "))
                        results = shop.search_sweets_by_price_range(min_p, max_p)
                        display_sweets(results)
                    except Exception as e:
                        print("not available", e)

                elif search_choice == "0":
                    break

                else:
                    print("Invalid choice. Try again.")

        elif ch == "5":
            while True:
                print("\n Sort Menu")
                print("1. Sort by quantity")
                print("2. Sort by Price")
                print("0. Back to Main Menu")
                sort_choice = input("Choose sort option: ")

                if sort_choice == "1":
                    results = shop.sort_sweets_by_quantity()
                    print("Sorted by quantity:")
                    display_sweets(results)

                elif sort_choice == "2":
                    results = shop.sort_sweets_by_price()
                    print("Sorted by price:")
                    display_sweets(results)

                elif sort_choice == "0":
                    break

                else:
                    print("Invalid choice. Try again.")
        
        elif ch == "6":
            try:
                sweet_id = int(input("Enter sweet ID to purchase: "))
                quantity = int(input("Enter quantity: "))
                shop.purchase_sweet(sweet_id, quantity)
                print(" Purchase successful!")
            except Exception as e:
                print(f" Error: {e}")

        elif ch == "7":
            try:
                sweet_id = int(input("Enter sweet ID to restock: "))
                quantity = int(input("Enter quantity to add: "))
                shop.restock_sweet(sweet_id, quantity)
                print(" Restocked successfully!")
            except Exception as e:
                print(f" Error: {e}")

        elif ch == "0":
            print("----- Thank you for visiting the Sweet Shop. Bye!-----")
            break

        else:
            print(" Invalid choice. Try again.")
        

if __name__ == "__main__":
    main()