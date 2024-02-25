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
    # initialize attempts
    attempts = 3

    # enter loop to request and validate username and password
    while attempts > 0:
        username_input = input("Key in your username: ")
        password_input = input("Enter your password: ")

        # check username and password if matching with credentials dict
        if username_input in credentials and password_input == credentials[username_input]:
             # print to indicate successful login
             print(f"\nAuthentication success.\nWelcome to AppleHome Sales Inventory Management, {username_input}!")
             return True
        else:
            # Reduce the attempts in each failure
            attempts -= 1
            print(f"Login failed. You have {attempts} attempts left. \nPlease double-check your username and password.")
    
    # print to indicate unsuccesful login after 3 times
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
            headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock", "ItemSold"]
            rows = []

            # iterate over idx and item in DB
            for idx, item in enumerate(database, start=1):
                row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], 
                       item["Price"], item["Stock"], item["ItemSold"]]
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
                headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock", "ItemSold"]
                rows = []

                # iterate over idx and item in DB
                for idx, item in enumerate(low_stock_items, start=1):
                    row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], 
                           item["Stock"], item["ItemSold"]]
                    # add row to rows
                    rows.append(row)

                # display items in table
                print(tabulate(rows, headers=headers, tablefmt="simple_outline"))

        # execute code if user selects 3   
        elif choice == "3":
            # iterating over item in database where status is new
            new_items = [item for item in database if item["Status"] == "new"]

            # if no new items, print the message
            if not new_items:
                print("No brand-new items found.")
            
            # if any new items, put them in table
            else:
                headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock", "ItemSold"]
                rows = []

                # iterate over new items
                for idx, item in enumerate(new_items, start=1):
                    row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"], item["ItemSold"]]
                    # add the iteration results to rows
                    rows.append(row)

                # print results in table format
                print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
        
        # execute code if user selects 4
        elif choice == "4":
            second_hand = [item for item in database if item["Status"] == "second"]

            # print message if no second hand item found
            if not second_hand:
                print("No second-hand items found.")
            
            # execute following lines to second hand items
            else:
                headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock", "ItemSold"]
                rows = []

                for idx, item in enumerate(second_hand, start=1):
                    row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"], item["ItemSold"]]
                    rows.append(row)

                print(tabulate(rows, headers=headers, tablefmt="simple_outline"))

        # execute code if user selects 5
        elif choice == "5":
            break
        else: 
            print("Invalid input. Please enter valid number (1-3).")

#  ++++++++++ ADD NEW ITEMS ++++++++++ 
def add_item(database):
    """Function to add item
    Args:
        database (list): Smartphone data
    """
    print("\nTo proceed, prepare the Item Code, Model, Status, Storage, Price, Stock, and ItemSold.")
    while True:
        print("\nMenu")
        print("1. Continue")
        print("2. Back to main menu")
        choice = input("\nEnter your choice: ")
    
        if choice == "1":
            # request inputs
            while True:
                code = input("Input the item code on the back of the box, e.g., A2849: ").upper()

                # check if input consists of one letter + 4 digits
                if re.match(r"^[A-Za-z]\d{4}$", code):
                    # check if model number is already in database
                    if any(item["ModelNumber"] == code for item in database):
                        print("This entry already exists. Please try another.")
                        continue
                    else:
                        break
                else:
                    # print message if user input invalid model number
                    print("Invalid input. Please input a valid model number as shown on the box.")

            model = input("Enter the iPhone model, e.g., 'iPhone 15 Pro Max': ").title()
            status = input("Specify the status, e.g., 'New' or 'Second'): ").lower()

            # validate storage input
            while True:
                storage = input("Input the iPhone capacity (in Gb), e.g., 256, 512, or 1000: ")

                # check if storage input is numerical and bigger than 0
                if storage.isdigit() and int(storage) > 0:
                    break
                else:
                    print("Invalid input. Please input a valid number for storage (in Gb): ")
            
            # validate price input
            while True:
                price = input("Enter the price (in Rupiahs): ")

                # check if price input is numerical and bigger than 0
                if price.isdigit() and int(price) > 0:
                    break
                else:
                    print("Invalid input. Please input a valid amount: ")
            
            # validate stock input
            while True:
                try:
                    stock = int(input("Enter the stock quantity: "))
                    # check if stock greater or equal to 0
                    if stock >= 0:
                        break
                    else:
                        print("Invalid input. The value should be at least 0.")
                # if user input non-integer, print this error message
                except ValueError:
                    print("It seems you have entered invalid input for the stock. Please try again.")
            
            # validate item sold input
            while True:
                try:
                    n_sold = int(input("Enter the number of items sold: "))
                    # check if sold items bigger than or equal to 0
                    if n_sold >= 0:
                        break
                    else:
                        print("Invalid input. The value should be at least 0.")
                # if user input non-integer, print this error message
                except ValueError:
                    print("It seems you have entered invalid input for the ItemSold. Please try again.")

            while True:
                choice = input("Confirm the addition? [Y/N]: ").upper()

                # check if user input Y or YES
                if choice == "Y" or "YES":
                    # add the new values to database
                    database.append({"ModelNumber": code,
                            "Model": model,
                            "Status": status,
                            "Storage": storage,
                            "Price": price,
                            "Stock": stock,
                            "ItemSold": n_sold})
            
                    # print confirmation
                    print("Items added successfully. Please check 'Display items' to see the changes. \nWhat do you want to do next?")
                    # go back to main menu
                    return
                # check if user input N or NO
                elif choice == "N" or "NO":
                    print("OK. The deletion canceled.")
                    break
                else:
                    print("Invalid input. Please 'Y' or 'N'.")
        
            break

        elif choice == "2":
            break
        else:
            print("Invalid input. Please input a valid number (1 or 2).")
 

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
            print("Only a number allowed. Please enter a valid number.")


# ++++++++++ MODIFY ITEMS ++++++++++
def modify_item(database):
    """Function to modify or update item in database

    Args:
        database (list): Smartphone data
    """
    while True:
        print("You will modify data in the inventory. Please enter '1' to continue.")
        print("\nMenu")
        print("1. Continue")
        print("2. Back to main menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("Here is the current inventory:")
            headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock", "ItemSold"]
            rows = []

            # iterate over idx and item in database
            for idx, item in enumerate(database, start=1):
                row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"], item["ItemSold"]]
                
                # add row to rows
                rows.append(row)

            # display items in table
            print(tabulate(rows, headers=headers, tablefmt="simple_outline"))

            # get item to modify
            idx = get_valid_index(len(database), "Which item do you want to modify?\nPlease input the item ID to start modifying: ")
            item_to_modify = database[idx - 1]

            # ask user to specify the modification
            while True:
                print("\nSelect item detail to modify")
                print("1. Model number")
                print("2. Model")
                print("3. Status")
                print("4. Storage")
                print("5. Price")
                print("6. Stock")
                print("7. ItemSold")
                print("8. Modify all details")
                print("9. Back to menu")

                choice = input("\nEnter your choice (1-9): ")

                if choice == "1":
                    while True:
                    # modify model number
                        new_model_number = input(f"Enter new model number (current: {item_to_modify['ModelNumber']}): ").upper()

                        if re.match(r"^[A-Za-z]\d{4}$", new_model_number):
                            if any(item["ModelNumber"] == new_model_number for item in database):
                                print("This entry already exists. Please try another.")
        
                            else:
                                item_to_modify["ModelNumber"] = new_model_number
                                print("Model number updated. Back to main menu to see the update.")
                                break
                        else:
                            print("Invalid input. Please input a valid model number based on the box: ")

                elif choice == "2":
                    # modify model
                    new_model = input(f"Enter new model (current: {item_to_modify['Model']}): ").title()
                    item_to_modify["Model"] = new_model
                    print("Model updated. Back to main menu to see the update.")
                
                elif choice == "3":
                    # modify status
                    new_status = input(f"Enter new status (current: {item_to_modify['Status']}): ")
                    item_to_modify["Status"] = new_status
                    print("Status has been updated. Back to main menu to see the update.")
                
                elif choice == "4":
                    # modify storage
                    new_storage = input(f"Enter new storage (current: {item_to_modify['Storage']}): ")
                    if new_storage.isdigit() and int(new_storage) > 0:
                        item_to_modify["Storage"] = new_storage
                        print("Storage has been updated. Back to main menu to see the update.")
                    else:
                        print("Invalid input. Please input a valid number for storage.")
                
                elif choice == "5":
                    # modify price
                    new_price = input(f"Enter new price amount (current: {item_to_modify['Price']}): ")
                    if new_price.isdigit() and int(new_price) > 0:
                        item_to_modify["Price"] = int(new_price)
                        print("Price has been updated. Back to main menu to see the update.")
                    else:
                        print("Invalid input. Please input a valid amount.")
                
                elif choice == "6":
                    # modify stock
                    try:
                        new_stock = input(f"Enter new number of stock (current: {item_to_modify['Stock']}): ")
                        if new_stock.isdigit() and int(new_stock) >= 0:
                            item_to_modify["Stock"] = int(new_stock)
                            print("Stock has been updated. Back to main menu to see the update.")
                        else:
                            print("Sorry, the quantity should be 0 or more. Please try again.")
                    except ValueError:
                        print("Invalid input. Please input a valid number.")
                
                elif choice == "7":
                    # modify item sold
                    try:
                        new_item_sold = input(f"Enter new number item sold (current: {item_to_modify['ItemSold']}): ")
                        if new_item_sold.isdigit() and int(new_item_sold) >= 0:
                            new_item_sold["Stock"] = int(new_item_sold)
                            print("Number of items sold has been updated. Back to main menu to see the update.")
                        else:
                            print("Sorry, the quantity should be 0 or more. Please try again.")
                    except ValueError:
                        print("Invalid input. Please input a valid number.")
                
                elif choice == "8":
                    # modify entire row
                    new_model_number = input(f"Enter new model number (current: {item_to_modify['ModelNumber']}): ").upper()
                    new_model = input(f"Enter new model (current: {item_to_modify['Model']}): ").title()
                    new_status = input(f"Enter new status(current: {item_to_modify['Status']}): ").lower()
                    new_storage = input(f"Enter new storage (current: {item_to_modify['Storage']}): ")
                    new_price = input(f"Enter new amount (current: {item_to_modify['Price']}): ")
                    new_stock = input(f"Enter new number of stock (current: {item_to_modify['Stock']}): ")
                    new_item_sold = input(f"Enter new quantity of the sold item (current: {item_to_modify['ItemSold']}): ")

                    if (
                        re.match(r"^[A-Za-z]\d{4}$", new_model_number) 
                        and any(item["ModelNumber"] == new_model_number for item in database)
                        and new_price.isdigit() and int(new_price) > 0
                        and new_stock.isdigit() and int(new_stock) >= 0
                        and new_item_sold.isdigit() and int(new_item_sold) >= 0
                    ):
                        item_to_modify.update({
                            "ModelNumber": new_model_number,
                            "Model": new_model,
                            "Status": new_status,
                            "Storage": int(new_storage),
                            "Price": int(new_price),
                            "Stock": int(new_stock),
                            "ItemSold": int(new_item_sold)
                        })
                        print("All details have been updated. Back to main menu to see the update.")
                    else:
                        print("Invalid input(s). Please check your input(s) and try again.")
                    
                elif choice == "9":
                    break
                else:
                    print("Invalid input. Please enter a valid number (1-8).")

        elif choice == "2":
            break
        else:
            print("Invalid input. Please input a valid number (1 or 2).")


# ++++++++++ REMOVE ITEMS ++++++++++
def remove_item(database):
    """Function to remove item from the database

    Args:
        table (list): Smartphone data
    """
    print("\nYou will remove an item in the inventory. Please enter '1' to continue.")
    while True:
        print("\nMenu")
        print("1. Remove an item")
        print("2. Back to main menu")

        choice = input("\nEnter your choice (1 or 2): ")

        if choice == "1":
            headers = ["ID", "ModelNumber", "Model", "Status", "Storage", "Price", "Stock", "ItemSold"]
            rows = []

            # iterate over idx and item in DB
            for idx, item in enumerate(database, start=1):
                row = [idx, item["ModelNumber"], item["Model"], item["Status"], item["Storage"], item["Price"], item["Stock"], item["ItemSold"]]
                # add row to rows
                rows.append(row)

            # display items in table
            print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
            idx = get_valid_index(len(database), "Please enter the ID of the item to remove: ")

            while True:
                choice = input("Confirm the deletion? [Y/N]: ").upper()

                if choice == "Y" or "YES":
                    database.pop(idx - 1)
                    print(f"ID {idx} has been removed. Go to the main menu to see the update.\nWhat do you want to do next?")
                    break
                elif choice == "N" or "NO":
                    print("OK. The deletion canceled.")
                    break
                else:
                    print("Invalid input. Please 'Y' or 'N'.")
        elif choice == "2":
            break
        else:
            "Invalid input. Please enter a valid number (1 or 2)."
    