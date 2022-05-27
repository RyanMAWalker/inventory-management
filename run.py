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

def add_stock():
    subprocess.run("clear")
    print("Add Stock".upper())
    print("Please select an option below:\n")
    print("1 - Add One Item")
    print("2 - Add Multiple Items\n")

    while True:
        choice = input("Choose option '1' or '2': ")    
        if choice in ["1" , "2"]:
            break

    if choice == "1":
        print()
        while True:
            item_name = input("Item Name: ")
            if item_name != "":
                break
            while True:
                print("stage 3")
                item_quantity = input("Quantity: ")
                if item_quantity.isdigit():
                    break
            

    elif choice == '2':
        print()
        while True:
            item_number = input("Enter the number of items to be added: ")
            if item_number.isdigit():
                break
        item_number = int(item_number)
        user_items = {}
        for i in range(1, item_number+1):
            while True:
                print()
                item_name = input("Item Name: ")
                if item_name != '':
                    break
            while True:
                item_quantity = input("Quantity: ")
                if item_quantity.isdigit():
                    break
            user_items.update({item_name: int(item_quantity)})
    
def view_stock():
    print("view Stock")

def main(): 
    """
    Run all program functions
    """
    user_info = get_user_info()
    options = user_options()

main()
