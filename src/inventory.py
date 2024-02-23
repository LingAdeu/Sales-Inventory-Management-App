from tabulate import tabulate       # for displaying db in table
import os                           # for cleaning the display
import re                           # for matching iPhone model number

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


#  ++++++++++ AUTHENTICATE USER ++++++++++ 
credentials = {"admin": "admin1234",
               "manager": "password1234"}

def authenticate_user():
    """Function to authenticate user
    Args:
        No args

    Returns:
        Boolean: Matching inputted username and password with existing credentials
    """
    attempts = 3
    while attempts > 0:
        username_input = input("Key in your username: ")
        password_input = input("Enter your password: ")

        # check username and password if matching with credentials dict
        if username_input in credentials and password_input == credentials[username_input]:
             print(f"Authentication success. Welcome to AppleHome Sales Inventory Management, {username_input}!")
             return True
        else:
            # Reduce the attempts in each failure
            attempts -= 1
            print(f"Login failed. {attempts} attempts left. \nPlease check your username and password.")
    
    print("Max attempt reached. Terminating the program now...")
    return False

#  ++++++++++ DISPLAY ITEMS ++++++++++ 
def display_item(database):
    """Function to display items
    Args:
        database (list): Smartphone inventory
    """
    while True:
        print("\nDisplay Menu")
        print("1. Show all items")
        print("2. Show low-stock items")
        print("3. show brand-new items")
        print("4. Show second-hand items")
        print("5. Back to main menu")
        
        # request input for the submenu
        choice = input("\nEnter which items to display: ")

        # execute code if user selects 1
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
        
        # execute code if user selects 2
        elif choice == "2":
            threshold = 5
            # iterate over item in database if stock < 5
            low_stock_items = [item for item in database if item["Stock"] < threshold]

            # check if no stock lower than 5
            if not low_stock_items:
                print("No low stock items found.")
            # execute the following code if stock greater than 5
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

        # execute code if user selects 3   
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
        
        # execute code if user selects 4
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

        # execute code if user selects 5
        elif choice == "5":
            break
        else: 
            print("Invalid input. Please enter valid number (1-3).")

#  ++++++++++ ADD NEW ITEMS ++++++++++ 
# add menu 1 for continue and 2 for back to main menu
def add_item(database):
    """Function to add item

    Args:
        database (list): Smartphone data
    """
    print("Please prepare the Item Code, Model, Status, Storage, Price and Stock to add an item.")

    # request inputs
    while True:
        code = input("Input the item code on the back of the box, e.g., A3105: ").upper()
        if re.match(r"^[A-Za-z]\d{4}$", code):
            if any(item["ModelNumber"] == code for item in database):
                print("This entry already exists. Please try another.")
                continue
            else:
                break
        else:
            print("Invalid input. Please input a valid model number as shown on the box.")

    model = input("Enter the iPhone model, e.g., 'iPhone 15 Pro Max': ").title()
    status = input("Specify the status, e.g., 'New' or 'Second'): ").lower()

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

    while True:
        choice = input("Confirm the addition? [Y/N]: ").upper()

        if choice == "Y":
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
        elif choice == 'N':
            print("OK. The deletion canceled.")
            break
        else:
            print("Invalid input. Please 'Y' or 'N'.")

    # # add to database
    # database.append({"ModelNumber": code,
    #                 "Model": model,
    #                  "Status": status,
    #                  "Storage": storage,
    #                  "Price": price,
    #                  "Stock": stock})
    
    # # print confirmation
    # print("Items added successfully. What do you want to do next?")

    # # go back to main menu
    # return

#  ++++++++++ CHECK VALIDITY OF INDEX  ++++++++++ 
def get_valid_index(max_idx, message):
    """Function to check validity of index

    Args:
        max_idx (int): Max index
        message (str): Information to display to user

    Returns:
        idx: _description_
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


# ++++++++++ MODIFY ITEMS ++++++++++
def modify_item(database):
    """Function to modify or update item in database

    Args:
        database (table): Smartphone data
    """
    print("Here is the current inventory:")
    headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
    rows = []

    # iterate over idx and item in database
    for idx, item in enumerate(database, start=1):
        row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
        
        # add row to rows
        rows.append(row)

    # display items in table
    print(tabulate(rows, headers=headers, tablefmt="simple_outline"))

    # get item to modify
    idx = get_valid_index(len(database), "Which item will you modify? \nPlease input the item ID to start modifying: ")
    item_to_modify = database[idx - 1]

    # ask user to specify the modification
    while True:
        print("\nSelect item detail to modify")
        print("1. Model Number")
        print("2. Model")
        print("3. Status")
        print("4. Storage")
        print("5. Price")
        print("6. Stock")
        print("7. Modify All Details")
        print("8. Back to Main Menu")

        choice = input("\nEnter your choice (1-8): ")

        if choice == "1":
            # modify model number
            new_model_number = input(f"Enter new model number (current: {item_to_modify['ModelNumber']}): ")
            if re.match(r"^[A-Za-z]\d{4}$", new_model_number):
                if any(item["ModelNumber"] == new_model_number for item in database):
                    print("This entry already exists. Please try another.")
                else:
                    item_to_modify["ModelNumber"] == new_model_number
                    print("Model nuumber updated.")
            else:
                print("Invalid input. Please input a valid model number based on the box: ")

        elif choice == "2":
            # modify model
            new_model = input(f"Enter new model number (current: {item_to_modify['Model']}): ")
            item_to_modify["Model"] = new_model
            print("Model updated.")
        
        elif choice == "3":
            # modify status
            new_status = input(f"Enter new model number (current: {item_to_modify['Status']}): ")
            item_to_modify["Status"] = new_status
            print("Status has been updated.")
        
        elif choice == "4":
            # modify storage
            new_storage = input(f"Enter new model number (current: {item_to_modify['Storage']}): ")
            if new_storage.isdigit() and int(new_storage) > 0:
                item_to_modify["Storage"] = new_storage
                print("Storage has been updated.")
            else:
                print("Invalid input. Please input a valid number for storage.")
        
        elif choice == "5":
            # modify price
            new_price = input(f"Enter new model number (current: {item_to_modify['Price']}): ")
            if new_price.isdigit() and int(new_price) > 0:
                item_to_modify["Price"] = int(new_price)
                print("Price has been updated.")
            else:
                print("Invalid input. Please input a valid amount.")
        
        elif choice == "6":
            # modify stock
            try:
                new_stock = input(f"Enter new model number (current: {item_to_modify['Stock']}): ")
                if new_stock.isdigit() and int(new_stock) >= 0:
                    item_to_modify["Stock"] = int(new_stock)
                    print("Stock has been updated.")
                else:
                    print("Sorry, the quantity should be 0 or more. Please try again.")
            except ValueError:
                print("Invalid input. Please input a valid number.")
        
        elif choice == "7":
            # modify entire row
            new_model_number = input(f"Enter new model number (current: {item_to_modify['ModelNumber']}): ")
            new_model = input(f"Enter new model number (current: {item_to_modify['Model']}): ")
            new_status = input(f"Enter new model number (current: {item_to_modify['Status']}): ")
            new_storage = input(f"Enter new model number (current: {item_to_modify['Storage']}): ")
            new_price = input(f"Enter new model number (current: {item_to_modify['Price']}): ")
            new_stock = input(f"Enter new model number (current: {item_to_modify['Stock']}): ")

            if (
                re.match(r"^[A-Za-z]\d{4}$", new_model_number)
                and new_model.isdigit()
                and new_price.isdigit()
                and new_stock.isdigit() and int(new_stock) >= 0
            ):
                item_to_modify.update({
                    "ModelNumber": new_model_number,
                    "Model": new_model,
                    "Status": new_status,
                    "Storage": int(new_storage),
                    "Price": int(new_price),
                    "Stock": int("new_stock")
                })
                print("All details have been updated.")
            else:
                print("Invalid input. Please check your inputs and try again.")
            
        elif choice == "8":
            break
        else:
            print("Invalid input. Please enter a valid number (1-8).")

# REMOVE ITEMS
def remove_item(database):
    """Function to remove item from the database

    Args:
        table (list): Smartphone data
    """
    headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock"]
    rows = []

    # iterate over idx and item in DB
    for idx, item in enumerate(database, start=1):
        row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"]]
        # add row to rows
        rows.append(row)

    # display items in table
    print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
    idx = get_valid_index(len(database), "Please enter the ID of the item to remove: ")

    while True:
        choice = input("Confirm the deletion? [Y/N]: ").upper()

        if choice == "Y":
            database.pop(idx - 1)
            print(f"ID {idx} has been removed. Please select 'Display items' to see the changes.")
            break
        elif choice == 'N':
            print("OK. The deletion canceled.")
            break
        else:
            print("Invalid input. Please 'Y' or 'N'.")
    