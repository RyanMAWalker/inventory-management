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
    print("Only a Manager or Supervisor may access this doccument.")
    job_role_str = input("Enter your job role:")

    validate_role(job_role_str)


def validate_role(role):
    """
    Inside this try, it checks that the role must be a "Supervisor" or "Manager".
    Raises a TypeError if the string is incorrect.
    """
    print(role)

get_user_info()