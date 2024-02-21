import inventory

# database
database = [
    # tambah kode barang
        {'ModelNumber': 'A2849', 'Model': 'iPhone 15 Pro Max', 'Status': 'new', 'Storage': 512, 'Price': 28999999, 'Stock': 7},
        {'ModelNumber': 'A3105', 'Model': 'iPhone 15', 'Status': 'new', 'Storage': 256, 'Price': 18499000, 'Stock': 12},
        {'ModelNumber': 'A2849', 'Model': 'iPhone 14 Pro', 'Status': 'second', 'Storage': 512, 'Price': 17500000, 'Stock': 15},
        {'ModelNumber': 'A3108', 'Model': 'iPhone 13 Pro', 'Status': 'second', 'Storage': 128, 'Price': 12200000, 'Stock': 17},
        {'ModelNumber': 'A3105', 'Model': 'iPhone 14 Pro', 'Status': 'new', 'Storage': 256, 'Price': 17900000, 'Stock': 15},
        {'ModelNumber': 'A3105', 'Model': 'iPhone 13', 'Status': 'new', 'Storage': 128, 'Price': 13499000, 'Stock': 3},
        {'ModelNumber': 'A3108', 'Model': 'iPhone 12', 'Status': 'new', 'Storage': 64, 'Price': 17900000, 'Stock': 15},
        {'ModelNumber': 'A2849', 'Model': 'iPhone 11 Pro Max', 'Status': 'second', 'Storage': 256, 'Price': 9000000, 'Stock': 2},
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
            choice = input("\nPlease input your choice (1-5): ")
            if choice == "1":
                inventory.display_item(database)
            elif choice == "2":
                inventory.add_item(database)
            elif choice == "3":
                inventory.modify_item(database)
            elif choice == "4":
                inventory.remove_item(database)
            elif choice == "5":
                print("Alright. Terminating the program. See you later!")
                break
            else:
                print("Oops, the option you have entered is invalid. Input num 1 to 5 only.")

# call menu() function
menu(database)