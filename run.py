import gspread
from google.oauth2.service_account import Credentials
import os
clear = lambda: os.system('cls') # taken from https://www.codegrepper.com/code-examples/python/how+to+make+a+clear+function+python


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
        first_name_str = input("Enter your first name: \n")
        last_name_str = input("Enter your last name: \n")
        job_role_str = input("Enter your job role:")

        if validate_role(job_role_str):
            print(f"Hello, {first_name_str.capitalize()} {last_name_str.capitalize()}")
            print(f"Your job role is {job_role_str.capitalize()} and can now access the inventory")
            break
    return validate_role(job_role_str)
        

def validate_role(role):
    """
    Inside this try, it checks that the role must be a Manager.
    Raises a TypeError if the string is incorrect.
    """
    try:
        if role.lower() != "manager":
            raise TypeError(
                "Only a Manager may access this doccument.\n"
            )
    except TypeError as e:
        print(f"Invalid job role: {e} please try again.\n")
        return False

    return True

def user_options():
    """
    User options for adding items or viewing current inventory
    """
    clear()
    print("Welcome to Inventory Management.")
    print("Please select an option below:\n")
    print("1 - Add Stock")
    print("2 - View Stock")
    
    choice = input("Choose option '1' or '2': ")    
    if choice == "1":
        add_stock()
    elif choice == "2":
        view_stock()

def add_stock():
    print("add Stock")

def view_stock():
    print("view Stock")

def main(): 
    """
    Run all program functions
    """
    user_info = get_user_info()
    options = user_options()

main()
