import inventory

# database
database = [
        {'ModelNumber': 'A2849', 'Model': 'iPhone 15 Pro Max', 'Status': 'new', 'Storage': 512, 'Price': 28999999, 'Stock': 7, 'ItemSold': 9},
        {'ModelNumber': 'A3090', 'Model': 'iPhone 15', 'Status': 'new', 'Storage': 256, 'Price': 18499000, 'Stock': 12, 'ItemSold': 14},
        {'ModelNumber': 'A2889', 'Model': 'iPhone 14 Pro', 'Status': 'second', 'Storage': 512, 'Price': 17500000, 'Stock': 15, 'ItemSold': 19},
        {'ModelNumber': 'A3108', 'Model': 'iPhone 13 Pro', 'Status': 'second', 'Storage': 128, 'Price': 12200000, 'Stock': 17, 'ItemSold': 17},
        {'ModelNumber': 'A2891', 'Model': 'iPhone 14 Pro', 'Status': 'new', 'Storage': 256, 'Price': 17900000, 'Stock': 15, 'ItemSold': 12},
        {'ModelNumber': 'A2631', 'Model': 'iPhone 13', 'Status': 'new', 'Storage': 128, 'Price': 13499000, 'Stock': 3, 'ItemSold': 29},
        {'ModelNumber': 'A3108', 'Model': 'iPhone 12', 'Status': 'new', 'Storage': 64, 'Price': 17900000, 'Stock': 15, 'ItemSold': 17},
        {'ModelNumber': 'A2220', 'Model': 'iPhone 11 Pro Max', 'Status': 'second', 'Storage': 256, 'Price': 9000000, 'Stock': 2, 'ItemSold': 6}
]

# main menu function
def menu(database):
    """Function to display main menu
    Args:
        database (list): table containing data
    """
    # clear display
    inventory.clear_display()
    # authenticate user
    authenticated_user = inventory.authenticate_user()

    # if authenticated, proceed with the loop
    if authenticated_user:
        while True:
            print("\nMain Menu")
            print("1. Display items")
            print("2. Add a new item")
            print("3. Modify an item")
            print("4. Remove an item")
            print("5. Exit and log out")

            # request a user input
            choice = input("\nPlease input your choice (1-5): ")

            if choice == "1":
                inventory.display_item(database)
            elif choice == "2":
                inventory.add_item(database)
            elif choice == "3":
                inventory.modify_item(database)
            elif choice == "4":
                # MASIH BELUM 
                inventory.remove_item(database)
            elif choice == "5":
                print("Terminating the program. See you later!")
                break
            else:
                print("Invlid input. Please enter number (1-5).")

# call menu() function
menu(database)