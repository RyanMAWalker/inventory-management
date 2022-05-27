import gspread
from google.oauth2.service_account import Credentials
import subprocess


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('inventory_management_RW')

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False



def get_user_info():
    """
    Get user name and role from user.
    Runs while loop to collect a valid string from the user.
    """
    while True: 
        name_str = input("Enter your full name: \n")
        job_role_str = input("Enter your job role:")

        if validate_role(job_role_str):
            print(f"Hello, {name_str.capitalize()}")
            print(f"Your job role is {job_role_str.capitalize()} and can now access the inventory")
            break
    return validate_role(job_role_str)
        

def validate_role(role):
    """
    Inside this try, it checks that the role must be a Manager.
    Raises a TypeError if the string is incorrect.
    """
    try:
        role = role.lower()
        if role not in ["manager", "supervisor"]:
            raise TypeError(
                "Only a Manager & Supervisor may access this doccument.\n"
            )
    except TypeError as e:
        print(e)
        return False

    return True

def user_options():
    """
    User options for adding items or viewing current inventory
    """
    subprocess.run("clear")
    print("Welcome to Inventory Management.")
    print("Please select an option below:\n")
    print("1 - Add Stock")
    print("2 - View Stock")
    
    while True:
        choice = input("Choose option '1' or '2': ")    
        if choice == "1":
            add_stock()
            break
        elif choice == "2":
            view_stock()
            break

def add_single_item():
    while True:
        item_name = input("Item Name: ")
        if item_name != "":
            break
    while True:
        item_quantity = input("Quantity: ")
        if item_quantity.isdigit():
            break
    while True:
        item_value = input("Value: ")
        if isfloat(item_value):
            break

def add_multiple_items():
    while True:
        number_of_items = input("Enter the number of items to be added: ")
        if number_of_items.isdigit():
            break
        number_of_items = int(number_of_items)
        user_items = {}
        for i in range(1, number_of_items+1):
            while True:
                print()
                item_name = input("Item Name: ")
                if item_name != "":
                    break
            while True:
                item_quantity = input("Item Quantity: ")
                if item_quantity.isdigit():
                    break
            while True:
                item_value = input("Value: ")
                if isfloat(item_value):
                    break

def add_stock():
    """
    User options for adding one item, or adding multiple.
    """
    subprocess.run("clear")
    print("Add Stock".upper())
    print("Please select an option below:\n")
    print("1 - Add One Item")
    print("2 - Add Multiple Items\n")

    while True:
        choice = input("Choose an option: ")
        if choice in ['1', '2']:
            break
    if choice == '1':
        print()
        add_single_item()


    elif choice == '2':
        print()
        add_multiple_items()
        user_items.update({item_name: int(item_quantity)})

        addItemsToFile(user_items, clear=False)

    
def view_stock():
    """
    User option for viewing current stock list.
    Edit and delete functionaility.
    """
    subprocess.run("clear")
    print("View Stock")   
    print("Choose and Option:")
    print("1 - Edit Item")
    print("2 - Delete Item")
    print()
    while True:
        choice = input("Choose option '1' or '2': ")    
        if choice == "1":
            print("This will edit")
            edit_item()
            break
        elif choice == "2":
            print("this will delete")
            delete_item()
            break

 
def add_stock_to_sheet(add_stock):
    """
    Update worksheet with the input stock data to add a new row
    """
    print("Updating worksheet")
    stock_worksheet = SHEET.worksheet("stock")
    stock_worksheet.append_row(add_stock)
    print("Stock worksheet updated")


def main(): 
    """
    Run all program functions
    """
    user_info = get_user_info()
    options = user_options()
    add_stock_to_sheet(add_stock())

main()
