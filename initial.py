import json

tax = 0.07
datafile = "put file path here"

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
          print("Placeholder")
        elif choice == "3":
          print("Placeholder")
        elif choice == "4":
          print("Placeholder")
        elif choice == "5":
          print("Placeholder")
        elif choice == "6":
          print("Back to main menu")
          break

        else:
          print("Invalid choice")
          
    elif choice == "2":
        while True:
          print("Customer Menu")
          print("products placeholder")
          print("1. View products")
          print("2. Add item to cart")
          print("3. Remove item from cart")
          print("4. View cart")
          print("5. Checkout")
          print("6. Exit")
          choice = input("Enter your choice: ")
          if choice == "1":
            print("Placeholder")
          elif choice == "2":
            print("Placeholder")
          elif choice == "3":
            print ("Placeholder")
          elif choice == "4":
            print("Placeholder")
          elif choice == "5":
            print("Placeholder")
          elif choice == "6":
            print("Back to main menu")
            break
            
    elif choice == "3":
        print("Exiting program")
        break
    else:
        print("Invalid choice")



