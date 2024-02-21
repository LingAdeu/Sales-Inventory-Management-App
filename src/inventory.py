from tabulate import tabulate  # for displaying db in table
import os                      # for cleaning the display
import re                      # for matching iPhone model number

# ++++++++++ CLEAN DISPLAY ++++++++++ 
def clear_display():
    """Function to clear the screen
    Args:
        No args
    """
    # check user operating system
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")

# AUTHENTICATE USER
credentials = {"admin": "admin1234",
               "manager": "password1234"}


#  ++++++++++ AUTHENTICATE USER ++++++++++ 
def authenticate_user():
    """Function to authenticate user
    Args:
        No args

    Returns:
        Bool: Matching 
    """
    attempts = 3
    while attempts > 0:
        username_input = input("Key in your username: ")
        password_input = input("Enter your password: ")

        # check username and password
        if username_input in credentials and password_input == credentials[username_input]:
             print(f"Authentication success. Welcome to SmarPi Inventory Management, {username_input}!")
             return True
        else:
            # Reduce the attempts in each failure
            attempts -= 1
            print("Login failed. Please check your username and password.")
    
    print("Too many failed attempts.")
    return False

#  ++++++++++ DISPLAY ITEMS ++++++++++ 
def display_item(database):
    """Function to display items
    Args:
        database (list): Smartphone inventory
    """
    while True:
        # GANTI PRINT TIAP POIN SAJA-------------------------------
        print("""
Display Menu:
1. Show all items
2. Show low stock items
3. Show brand-new items
4. Show second-hand items
5. Back to main menu""")
        
        # request input for the submenu
        choice = input("Enter which items to display: ")

        if choice == "1":
            headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
            rows = []

            # iterate over idx and item in DB
            for idx, item in enumerate(database, start=1):
                row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
                # add row to rows
                rows.append(row)

            # display items in table
            print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
        elif choice == "2":
            threshold = 5
            # iterate over item in database if stock < 5
            low_stock_items = [item for item in database if item["Stock"] < threshold]

            # check if not 5
            if not low_stock_items:
                print("No low stock items found.")
            else:
                headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
                rows = []

                # iterate over idx and item in DB
                for idx, item in enumerate(low_stock_items, start=1):
                    row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
                    # add row to rows
                    rows.append(row)

                # display items in table
                print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
                
        elif choice == "3":
            new_items = [item for item in database if item["Status"] == "new"]

            if not new_items:
                print("No brand-new items found.")
            else:
                headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
                rows = []

                for idx, item in enumerate(new_items, start=1):
                    row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
                    rows.append(row)

                print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
                
        elif choice == "4":
            second_hand = [item for item in database if item["Status"] == "second"]

            if not second_hand:
                print("No second-hand items found.")
            else:
                headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
                rows = []

                for idx, item in enumerate(second_hand, start=1):
                    row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
                    rows.append(row)

                print(tabulate(rows, headers=headers, tablefmt="simple_outline"))

        elif choice == "5":
            break
        else: 
            print("Invalid input. Please enter valid number (1-3).")

#  ++++++++++ ADD NEW ITEMS ++++++++++ 
def add_item(database):
    print("Please prepare the Item Code, Model, Status, Storage, Price and Stock to add an item.")

    # request inputs
    code = input("Input the item code on the back of the box, e.g., A3105: ").upper()
    model = input("Enter the iPhone model, e.g., 'iPhone 15 Pro Max': ").title()
    status = input("Specify the status, e.g., 'New' or 'Second'): ").capitalize()

    # validate storage input
    while True:
        storage = input("Input the iPhone capacity (in Gb), e.g., 256, 512, or 1000: ")
        if storage.isdigit() and int(storage) > 0:
            break
        else:
            print("Invalid input. Please input a valid number for storage (in Gb): ")
    
    # validate price input
    while True:
        price = input("Enter the price (in Rupiahs): ")
        if price.isdigit() and int(price) > 0:
            break
        else:
            print("Invalid input. Please input a valid amount: ")
    
    # validate stock input
    while True:
        try:
            stock = int(input("Enter the stock quantity: "))
            if stock > 0:
                break
            else:
                print("Sorry, the quantity should be more than 0. Please re-input the correct value.")
        except ValueError:
            print("It seems you have entered invalid input for the stock. Please try again.")

    # add to database
    database.append({"ModelNumber": code,
                    "Model": model,
                     "Status": status,
                     "Storage": storage,
                     "Price": price,
                     "Stock": stock})
    
    # print confirmation
    print("Items added successfully. What do you want to do next?")

    # go back to main menu
    return

#  ++++++++++ CHECK VALIDITY OF INDEX  ++++++++++ 
def get_valid_index(max_idx, message):
    """Function to check validity of index

    Args:
        max_idx (int): _description_
        message (str): _description_

    Returns:
        _type_: _description_
    """
    while True:
        try:
            # request input
            idx = int(input(message))
            if 1 <= idx <= max_idx:
                return idx
            else:
                print("Sorry, index is invalid. Please type a number between a and {max_idx}")
        except ValueError:
            print("Oops, only a number allowed. Please enter a valid number.")


#  ++++++++++ MODIFY ITEMS ++++++++++ 
def modify_item(database):
    headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
    rows = []

    # iterate over idx and item in DB
    for idx, item in enumerate(database, start=1):
        row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
        # add row to rows
        rows.append(row)

    # display items in table
    print(tabulate(rows, headers=headers, tablefmt="simple_outline"))

    idx = get_valid_index(len(database), "Please input the item ID to start modifying: ")

    item_to_modify = database[idx - 1]
    # print(f"Selected item to modify: {item_to_modify}")

    # request and check new model number
    while True:
        new_model_number = input(f"Enter new model number (current: {item_to_modify['ModelNumber']}): ")
        if re.match(r"^[A-Za-z]\d{4}$", new_model_number):
            break
        else:
            print("Invalid input. Please input a valid model number based on the box.")

    # request input from user
    new_model = input(f"Enter new model (current: {item_to_modify['Model']}): ")
    new_status = input(f"Enter new status (current: {item_to_modify['Status']}) ")

    # request and check new storage
    while True:
        new_storage = input(f"Enter new storage (current: {item_to_modify['Storage']}): ")
        if new_storage.isdigit() and int(new_storage) > 0:
            break
        else:
            print("Invalid input. Please input a valid number for storage (in Gb)")

    # request and check new price
    while True:
        new_price = input(f"Enter new price (current: {item_to_modify['Price']}): ")
        if new_price.isdigit() and int(new_price) > 0:
            break
        else:
            print("Input invalid. Please input a valid amount.")
    
    # request and check new stock
    while True:
        try:
            new_stock = input(f"Enter new stock (current: {item_to_modify['Stock']}): ")
            if new_stock.isdigit() and int(new_stock) >= 0:
                break
            else: 
                print("Sorry, the quantity should be 0 or more. Please try again.")
        except:
            print("It seems you have entered invalid input for the stock. Please re-input the correct value.")

    # update the item details in the dict
    item_to_modify.update({
        "Model": new_model,
        "Status": new_status,
        "Storage": int(new_storage),
        "Price": int(new_price),
        "Stock": int(new_stock)
    })
    print("Updated. Please select 'Display items' to see the changes.")


# # REMOVE ITEMS
# def remove_item(database):
#     """Function to remove item from the database

#     Args:
#         table (dict): Smartphone inventory
#     """
#     display_item(database)
#     idx = get_valid_index(len(database), "Please enter the ID of the item to remove: ")

#     item = database[idx - 1]
#     print(f"{item} has been removed.")
#     print(display_item)