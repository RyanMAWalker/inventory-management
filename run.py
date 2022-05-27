import gspread
from google.oauth2.service_account import Credentials

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
    Get user name and role from user
    """
    first_name_str = input("Enter your first name: \n")
    last_name_str = input("Enter your last name: \n")
    job_role_str = input("Enter your job role:")

    validate_role(job_role_str)
    print(f"Hello, {first_name_str.capitalize()} {last_name_str.capitalize()} your job role is {job_role_str.capitalize()} and can now access the inventory")


def validate_role(role):
    """
    Inside this try, it checks that the role must be a Manager.
    Raises a TypeError if the string is incorrect.
    """
    try:
        if role.lower() != "manager":
            raise TypeError(
                f"Only a Manager may access this doccument.\n"
            )
    except TypeError as e:
        print(f"Invalid job role: {e} please try again.\n")

get_user_info()