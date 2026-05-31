import json

tax = 0.07
datafile = "json path"

try:
  file = open(datafile, "r")
  data = json.load(file)
  inventory = data["inventory"]
  sales = data["sales"]

while True:
    print("Main menu")
    print("1. Owner menu")
    print("2. Customer")
    print("3. Exit program")
    choice = input("Enter your choice: ")
    if choice == "1":
      while True:
        print("Owner Menu")
        print("1. Add a product")
        print("2. Remove a product")
        print("3. Change item quantity")
        print("4. View current inventory")
        print("5. Print sales report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
          name = input("Item name:")
          if name in inventory:
            print(f"'{name}' already exists in inventory")
          else:
            try:
              cost = float(input("Item cost: "))
              qty = int(input("Item quantity: "))
              inventory[name] = {cost, qty}
              file = open(datafile, "w")
              json.dump(inventory, sales)
              file.close
              print(f"'{name}' added to inventory")

        
        elif choice == "2":
          name = input("Item name:")
          if name in inventory:
            del inventory[name]
            file = open(datafile, "w")
            json.dump(inventory, sales)
            file.close
          else:
            print(f"'{name}' not found in inventory")

        
        elif choice == "3":
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
                file = open(datafile, "w")
                json.dump(inventory, sales)
                file.close()
                print(f"'{name}' quantity updated to {new_qty}")

        
        elif choice == "4":
          if len(inventory) = 0:
            print("Inventory is empty")
          else:
            print("Current Inventory:")
            for name in inventory:
              cost = inventory[name][0]
              price = inventory[name][1]
              qty = inventory[name][2]
              print(f"{name}: cost: ${cost}, price: ${price}, quantity: {qty}")

        
        elif choice == "5":
          if len(sales) = 0:
            print("No sales data available")
          else:
            revenue_by_item = {}
            total_revenue = 0
            for sale in sales:
              sale_name = sale[0]
              sale_total = sale[4]
              total_revenue = total_revenue + sale_total
              if sale_name in revenue_by_item:
                revenue_by_item[sale_name] = revenue_by_item[sale_name] + sale_total
              else:
                revenue_by_item[sale_name] = sale_total
              print("sales by item")
              for name in revenue_by_item:
                print(f"{name}: ${revenue_by_item[name]}")
              print(f"total revenue: ${total_revenue}")
            
                  
        elif choice == "6":
          print("Back to main menu")
          break

        else:
          print("dummy")
          
    elif choice == "2":
        while True:
          print("Customer Menu")
          print("products placeholder")
          print("1. View products")
          print("2. Add item to cart")
          print("3. Exit")
          choice = input("Enter your choice: ")
          if choice == "1":
            if len(inventory) = 0:
              print("Inventory is empty")
            else:
              for name in inventory:
                price = inventory[name][1]
                print(f"{name}: ${price}")

            
          elif choice == "2":
            name = input("Item name:")
            if name not in inventory:
              print(f"'{name}' not found in inventory")
            else:
              qty_available = inventory[name][2]
              if qty_available = 0:
                print(f"'{name}' is out of stock")
              else:
                try:
                  qty = int(input("Enter quantity: "))
                  if qty_wanted <= 0:
                    print("Error: Quantity must be positive")
                  elif qty_wanted > qty_available:
                    print(f"error")
                  else
                    unit_price = inventory[name][1]
                    subtotal = unit_price * qty_wanted
                    tax = subtotal * tax
                    total = subtotal + tax

                    print("Receipt")
                    print(f"Item: {name}")
                    print(f"Quantity: {qty_wanted}")
                    print(f"Unit: ${unit_price}")
                    print(f"Subtotal: ${subtotal}")
                    print(f"Tax: ${tax}")
                    print(f"Total: ${total}")
                
                    inventory[name][2] = qty_available - qty_wanted
                    sales.append([name, qty_wanted, unit_price, subtotal, tax, total])
                    file = open(datafile, "w")
                    json.dump(inventory, sales)
                    file.close()
            
          elif choice == "3":
            break
    else:
        print("Invalid choice")



