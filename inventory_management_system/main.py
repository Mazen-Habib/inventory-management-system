from user import authenticate
from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()

    username = input("Enter username: ")
    password = input("Enter password: ")

    user = authenticate(username, password)
    if not user:
        print("Invalid credentials")
        return

    print(f"Welcome, {'Admin' if user.is_admin else 'User'} {username}!")

    while True:
        if user.is_admin:
            print("\n1. Add Product\n2. View Products\n3. Delete Product\n4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                product_id = input("Product ID: ")
                name = input("Product Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                stock_quantity = int(input("Stock Quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                inventory.add_product(product)
                print("Product added successfully.")
            elif choice == "2":
                inventory.view_products()
            elif choice == "3":
                product_id = input("Enter Product ID to delete: ")
                if inventory.remove_product(product_id):
                    print("Product deleted successfully.")
                else:
                    print("Product not found.")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
        else:
            print("\n1. View Products\n2. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                inventory.view_products()
            elif choice == "2":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
