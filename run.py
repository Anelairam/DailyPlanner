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


def display():
    """
    Welcome message to the user:
        -ask information from the user if it is a new or an excisting one
    """

    today = date.today()
    print(today)    
    print("Welcome to the Daily Planner")
    while True:
        try:
            choice = input("If you are a new user please enter 0 if you already are a user enter 1: ")
            if choice != "1" and choice != "0":
                raise ValueError(
                    f"Enter 0 for excisting user or 1 for new user, you entered: {choice}"
                )
            else:
                return choice
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
                

def user_validation(userd, worksheet):
    """
    Using user's input the fuction runs a for loop through the users worksheet and check if 
    the provided data are valid
    """
    user_sheet = SHEET.worksheet(worksheet)
    user_data = user_sheet.get_all_values()
    for i in user_data:
        if i == userd:
            print(i)
        else:
            print("The username or the password you provided might be wrong")
    


def user():
    """
    Asking for user's data
        -Take user's name and password
        -Run user's information from the validator of the current entries
    """
    user_data = []
    username = input("Please enter your username: ")
    passwrod = input("Please enter your password: ")
    user_data.append(username)
    user_data.append(passwrod)
    print(f"Hello {username} processing the data you provided... ")
    user_validation(user_data, "users")




def new_user():
    """
    Asking for new user's data
        -Ask the user to add his username and password
        -Run user's information from the validator if the username already excists inform
            the user that the username exists and provide a new one
    """





def main():
    us_choice = display()
    if us_choice == "1" :
        user()
    else:
        new_user()
    main_menu()


main()