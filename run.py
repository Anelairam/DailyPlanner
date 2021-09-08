import gspread
from google.oauth2.service_account import Credentials
from datetime import date

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("DaillyPannerDb")

users = SHEET.worksheet("users")

users_data = users.get_all_values()

print(users_data)

def display:
    """
    Welcome message to the user:
        -ask information from the user if it is a new or an excisting one
    """

    today = date.today()
    print(today)    
    print("Welcome to the Daily Planner")
    choice = input("If you are a new user please enter 0 if you already have an account enter 1: /n")
    return choice

def user:
    """
    Asking for user's data
        -Take user's name and password
        -Run user's information from the validator of the current entries
    """

    


def new_user:
    """
    Asking for new user's data
        -Ask for username and password
        -Run user's information from the validator if the username excists or not provide 
            the correct message and run the process again to get a right username
    """

def main:
    us_choice = display()