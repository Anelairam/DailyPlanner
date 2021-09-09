import gspread
from google.oauth2.service_account import Credentials
import datetime

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
    global today
    today = datetime.datetime.now()    
    print(today.strftime("%x"))
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
            return userd[0]
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
    val_username = user_validation(user_data, "users")
    return val_username


#def new_user():
    """
    Asking for new user's data
        -Ask the user to add his username and password
        -Run user's information from the validator if the username already exists inform
            the user that the username exists and provide a new one
    """
#def events_of_the_day(user, date):


def new_event(user):
    """
    Askthe user to insert the new event's information in a specific way
    """
    try:
        print(f"Your new event will have the following format: 'Date' , 'Time' , 'Desciption' , 'Where', 'With Who' \n")
        date = input("When is your new event? ")
        time = input("What time is your event? ")
        description = input("What is the subject of the event? ")
        who = input("Who are you going to meet? ")
        location = input(f"Where are you going to meet with {who} ?")
            if choice != "1" and choice != "0":
                raise ValueError(
                    f"Enter 0 for excisting user or 1 for new user, you entered: {choice}"
                )
            else:
                return choice
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

#def delete_event(user):


#def exit():



def main_menu(val_user):
    """
    The funtion provides to the user his four navigating options:
        -1.Display the days events
        -2.Add a new event
        -3.Delete an event
        -4.Exit or log out
    """
    print(f"Hello {val_user} how can I help you today? \n")
    while True:
        try:
            print(f" 1.Display my events for today\n", f"2.Add a new event\n", f"3.Delete an event\n", f"4.Exit\n")
            menu_choice = input("Please choose from the options 1-4 : ")
            choice = int(menu_choice)
            if choice < 1 or choice > 4:
                raise ValueError(
                    f"You can choose between options 1-4, option {menu_choice} is not valid"
                )
            elif choice == 1:
                print("Your choice is 1")
                events_of_the_day(val_user, today)
            elif choice == 2:
                print("Your choice is 2")
                new_event(val_user)
            elif choice == 3:
                print("Your choice is 3")
                delete_event(val_user)
            else:
                print("Your choice is 4")
                exit()
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def main():
    us_choice = display()
    if us_choice == "1":
        valid_user = user()
        print(valid_user)
    else:
        new_user()
    main_menu(valid_user)


main()