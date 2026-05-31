import json

TAX_RATE = 0.07
datafile = "data.json"

try:
    with open(datafile, "r") as file:
        data = json.load(file)
        inventory = data["inventory"]
        sales = data["sales"]
except (FileNotFoundError, KeyError, json.JSONDecodeError):
    inventory = {}
    sales = []

def save_data():
    with open(datafile, "w") as file:
        json.dump({"inventory": inventory, "sales": sales}, file)

while True:
    print("\nMain menu")
    print("1. Owner menu")
    print("2. Customer")
    print("3. Exit program")
    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            print("\nOwner Menu")
            print("1. Add a product")
            print("2. Remove a product")
            print("3. Change item quantity")
            print("4. View current inventory")
            print("5. Print sales report")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Item name: ")
                if name in inventory:
                    print(f"'{name}' already exists in inventory")
                else:
                    try:
                        cost = float(input("Item cost: "))
                        price = float(input("Item selling price: "))
                        qty = int(input("Item quantity: "))
                        inventory[name] = {"cost": cost, "price": price, "qty": qty}
                        save_data()
                        print(f"'{name}' added to inventory")
                    except ValueError:
                        print("Error: Please enter valid numbers")

            elif choice == "2":
                name = input("Item name: ")
                if name in inventory:
                    del inventory[name]
                    save_data()
                    print(f"'{name}' removed from inventory")
                else:
                    print(f"'{name}' not found in inventory")

            elif choice == "3":
                name = input("Item name: ")
                if name not in inventory:
                    print(f"'{name}' not found in inventory")
                else:
                    try:
                        change = int(input("Enter quantity change: "))
                        current_qty = inventory[name]["qty"]
                        new_qty = current_qty + change
                        if new_qty < 0:
                            print("Error: Quantity cannot be negative")
                        else:
                            inventory[name]["qty"] = new_qty
                            save_data()
                            print(f"'{name}' quantity updated to {new_qty}")
                    except ValueError:
                        print("Error: Please enter a valid number")

            elif choice == "4":
                if len(inventory) == 0:
                    print("Inventory is empty")
                else:
                    print("\nCurrent Inventory:")
                    for name in inventory:
                        cost = inventory[name]["cost"]
                        price = inventory[name]["price"]
                        qty = inventory[name]["qty"]
                        print(f"{name}: cost: ${cost:.2f}, price: ${price:.2f}, quantity: {qty}")

            elif choice == "5":
                if len(sales) == 0:
                    print("No sales data available")
                else:
                    revenue_by_item = {}
                    total_revenue = 0
                    for sale in sales:
                        sale_name = sale["name"]
                        sale_total = sale["total"]
                        total_revenue += sale_total
                        if sale_name in revenue_by_item:
                            revenue_by_item[sale_name] += sale_total
                        else:
                            revenue_by_item[sale_name] = sale_total
                    print("\nSales by item:")
                    for name in revenue_by_item:
                        print(f"{name}: ${revenue_by_item[name]:.2f}")
                    print(f"Total revenue: ${total_revenue:.2f}")

            elif choice == "6":
                print("Back to main menu")
                break

            else:
                print("Invalid choice")

    elif choice == "2":
        while True:
            print("\nCustomer Menu")
            print("1. View products")
            print("2. Buy an item")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                if len(inventory) == 0:
                    print("Inventory is empty")
                else:
                    print("\nProducts:")
                    for name in inventory:
                        price = inventory[name]["price"]
                        qty = inventory[name]["qty"]
                        print(f"{name}: ${price:.2f} (qty: {qty})")

            elif choice == "2":
                name = input("Item name: ")
                if name not in inventory:
                    print(f"'{name}' not found in inventory")
                else:
                    qty_available = inventory[name]["qty"]
                    if qty_available == 0:
                        print(f"'{name}' is out of stock")
                    else:
                        try:
                            qty_wanted = int(input("Enter quantity: "))
                            if qty_wanted <= 0:
                                print("Error: Quantity must be positive")
                            elif qty_wanted > qty_available:
                                print(f"Error: Only {qty_available} available")
                            else:
                                unit_price = inventory[name]["price"]
                                subtotal = unit_price * qty_wanted
                                tax_amount = subtotal * TAX_RATE
                                total = subtotal + tax_amount

                                print("\nReceipt")
                                print(f"Item: {name}")
                                print(f"Quantity: {qty_wanted}")
                                print(f"Unit price: ${unit_price:.2f}")
                                print(f"Subtotal: ${subtotal:.2f}")
                                print(f"Tax: ${tax_amount:.2f}")
                                print(f"Total: ${total:.2f}")

                                inventory[name]["qty"] = qty_available - qty_wanted
                                sales.append({
                                    "name": name,
                                    "qty": qty_wanted,
                                    "unit_price": unit_price,
                                    "subtotal": subtotal,
                                    "tax": tax_amount,
                                    "total": total
                                })
                                save_data()
                        except ValueError:
                            print("Error: Please enter a valid number")

            elif choice == "3":
                break
            else:
                print("Invalid choice")

    elif choice == "3":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
