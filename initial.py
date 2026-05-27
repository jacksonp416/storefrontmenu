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
          print("Placeholder")
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



