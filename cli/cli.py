import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")

    if response.status_code == 200:
        items = response.json()

        if not items:
            print("\nInventory is empty.\n")
            return

        print("\n====== INVENTORY ======")
        for item in items:
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Brand: {item['brand']}")
            print(f"Price: ${item['price']}")
            print(f"Quantity: {item['quantity']}")
            print("-" * 30)

    else:
        print("Error retrieving inventory.")


def view_item():
    item_id = input("Enter item ID: ")

    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        item = response.json()

        print("\nItem Details")
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Brand: {item['brand']}")
        print(f"Price: ${item['price']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Ingredients: {item.get('ingredients_text', '')}")

    else:
        print("Item not found.")


def add_item():
    name = input("Name: ")
    brand = input("Brand: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    payload = {
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    response = requests.post(f"{BASE_URL}/inventory", json=payload)

    if response.status_code == 201:
        print("Item added successfully!")
    else:
        print("Failed to add item.")


def update_item():
    item_id = input("Enter item ID: ")

    price = float(input("New price: "))
    quantity = int(input("New quantity: "))

    payload = {
        "price": price,
        "quantity": quantity
    }

    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}",
        json=payload
    )

    if response.status_code == 200:
        print("Item updated successfully!")
    else:
        print("Item not found.")


def delete_item():
    item_id = input("Enter item ID: ")

    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 200:
        print("Item deleted successfully!")
    else:
        print("Item not found.")


def search_openfoodfacts():
    barcode = input("Enter product barcode: ")

    response = requests.get(f"{BASE_URL}/external/{barcode}")

    if response.status_code == 200:
        product = response.json()

        print("\nProduct Found")
        print(f"Name: {product['product_name']}")
        print(f"Brand: {product['brands']}")
        print(f"Ingredients: {product['ingredients_text']}")
    else:
        print("Product not found.")


def main():
    while True:
        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. View Inventory")
        print("2. View Item by ID")
        print("3. Add Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Find Product (OpenFoodFacts)")
        print("0. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            view_inventory()

        elif choice == "2":
            view_item()

        elif choice == "3":
            add_item()

        elif choice == "4":
            update_item()

        elif choice == "5":
            delete_item()

        elif choice == "6":
            search_openfoodfacts()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
