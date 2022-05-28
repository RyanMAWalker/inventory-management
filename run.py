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

stock = SHEET.worksheet('stock')
data = stock.get_all_values()

def get_user_info():
    """
    Get user name and role from user.
    Runs while loop to collect a valid string from the user.
    """
    while True: 
        name_str = input("Enter your full name: \n")
        print("Only a Manager or Supervisor may access this document.")
        print("Please enter your position below")
        job_role_str = input("Enter your position here:")

        if validate_role(job_role_str):
            print(f"Hello, {name_str.capitalize()}")
            print(f"Your job role is {job_role_str.capitalize()} and can now access the inventory.")
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
    """
    Gets stock input from the user
    """
    subprocess.run("clear")
    print("Please enter the data as the following:")
    print("Item, Quantity, Price per Item\n")
    print("For Example:")
    print("Item: Shoes")
    print("Quantity: 2")
    print("Price: 26.50 \n")


    user_item_name = [input("Enter Item Name: ")]
    user_item_quan = [input("Enter Item Quantity: ")]
    user_item_price = [input("Enter Price: ")]

    print(f"{user_item_name}, {user_item_price}, {user_item_quan}")

def main():

    get_user_info()
    user_options()

main()
