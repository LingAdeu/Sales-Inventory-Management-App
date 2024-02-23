![Header](ReadMeHeader.png)

## About
SmartPi is a sales inventory management developed for AppleHome, a fictional store inspired by a real SME business in Bantul, Yogyakarta. Because this inventory management was designed to access and update the sales inventory, not everyone should be able to use the application (find the dummy credentials below).

## Credentials

> [!IMPORTANT] 
> For security purposes, only two roles are given the access. Here are dummy credentials that can be used to operate the application.

- `admin`: `admin1234`,
- `manager`: `password1234`

## Main features
1. Display items
	1. This feature allows users to see available items by different options such as all items, low-stock items, brand-new or second-hand items. 
2. Add a new item
	1. Users can add a new entry to the existing data.
	2. Add to DB?
3. Modify an item
	1. Users have several options to modify an existing item based on the item ID. Users are free to update whether an entire row or specific column in a row.
	2. Add to DB?
4. Remove an item
	1. An item removal can be performed once the users specify which item ID to remove from the DB. 
5. Exit and log out
	1. For security purposes, this program is complemented with the exit menu. Once the users exit, they will be automatically logged out, and they will need to login when they want to operate the app again. 

## Project Organization

    .
    ├── README.md            <- The top-level README for developers using this project.
    ├── docs
    │   └── requirements.txt <- The requirements file for reproducing the env. Generated using `pip freeze > requirements.txt`
    └── src                  <- Source codes
        ├── __main__.py      <- The main file used to run the program.
        └── inventory.py     <- The module file containing the functions.


## Task
- To update the readme image header
- Tidy up 