import gspread
from google.oauth2.service_account import Credentials
from datetime import date
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
    global currentday  
    currentday = date.today() 
    print(currentday)
    print(currentday.strftime("%d"),currentday.strftime("%B"),currentday.strftime("%Y"))
    print("Welcome to the Daily Planner")
    while True:
        try:
            choice = input("If you are a new user please enter 0 if you already are a user enter 1:\n")
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
    user_email = user_sheet.col_values(1)
    user_pass = user_sheet.col_values(2)
    find = 0
    for i in zip(user_email, user_pass):
        if i == tuple(userd):
            find = 1
            return find
    if find == 0:
        print("The username or the password you provided might be wrong")
        return find


def user():
    """
    Asking for user's data
        -Take user's name and password
        -Run user's information from the validator of the current entries
    """
    user_data = []
    validation = True
    while validation:
        try:        
            username = input(f"Please enter your username:\n")
            passwrod = input(f"Please enter your password:\n")
            user_data.append(username)
            user_data.append(passwrod)
            print(f"Hello {username} processing the data you provided... ")
            val_username = user_validation(user_data, "users")
            if val_username != 0:
                validation = False
                return user_data
            else:
                raise ValueError(
                    f"The username or the password you have entered is wrong, please try again.")
        except ValueError as e:
            print(f"Invalid data: {e}")


def new_user(): 
    """
    Asking for new user's data
        -Ask the user to add his username and password
        -Run user's information from the validator if the username already exists inform
            the user that the username exists and provide a new one
    """
    id_sheet = SHEET.worksheet("users")
    new_entry = []
    while True:
        try:
            n_user = input("Please enter your email address: \n")
            f_name = input("Please enter your name: \n")
            while True:
                n_password = input("Please enter your password: \n")
                v_password = input("Re enter your password for validation: \n")
                print("Hello we are now processing your data.")
                if n_password != v_password:
                    print(f"Unfortunatelly {f_name} the password you provided do not match the original, please try again...")
                else:
                    break
            print(f"Welcome to Daily Planner {f_name}, we will direct you to the main menu.")
            new_entry.append(n_user)
            new_entry.append(n_password)
            new_entry.append(f_name)
            id_sheet.append_row(new_entry)
            return n_user
        except:
            print(f"You have entered: '{f_name}'. This is not a valid email, please try again...")


def get_data(action, user):
    """
    Loop through the database and display only the data that are corresponding to today's date
    """
    events_sheet = SHEET.worksheet("events")
    ids = events_sheet.col_values(1)
    user_ids = events_sheet.col_values(2)
    days = events_sheet.col_values(3)
    hours = events_sheet.col_values(4)
    subjects = events_sheet.col_values(5)
    persons = events_sheet.col_values(6)
    locations = events_sheet.col_values(7)    
    if action == 1:
        #Display user's events
        print(f"{user} here are your events:\n")
        for id, user_id, day, hour, subject, person, location in zip(ids ,user_ids, days, hours, subjects, persons, locations):
            if user_id == user:
                print(f"#{id}. {day} Meeting at {hour} with {person} at {location} for {subject} \n")
    else:
        #Display all of the user's events and give the option to delete events
        print(f"{user} you have scheduled the following events:\n")
        for id, user_id, day, hour, subject, person, location in zip(ids, user_ids, days, hours, subjects, persons, locations):
            if user_id == user:
                print(f"#{id}. {day} Meeting at {hour} with {person} at {location} for {subject} \n")


def new_event(user):
    """
    Ask the user to insert the new event's information in a specific way
    Add all the user's information into the db
    """
    events_sheet = SHEET.worksheet("events")
    event_id = events_sheet.col_values(1)
    event_data = []
    try:
        print(f"Your new event will have the following format: 'Date' , 'Time' , 'Desciption' , 'With Who', 'Where' \n")
        while True:
            try:
                format = "%d-%m-%Y"
                day_input = input(f"Please enter the date as (DD-MM-YYYY): ")
                datetime. datetime. strptime(day_input, format)
            except ValueError:
                print("The date you provided it is not correct, please try again...")
        time = input(f"What time is your event?")
        description = input(f"What is the subject of the event?\n")
        who = input(f"Who are you going to meet? ")
        location = input(f"Where are you going to meet with {who} ?\n")
        event_data.append(len(event_id)+1)
        event_data.append(user[0])
        event_data.append(day_input)
        event_data.append(time)
        event_data.append(description)
        event_data.append(who)
        event_data.append(location)
        events_sheet.append_row(event_data)           
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


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
            menu_choice = input(f"Please choose from the options 1-4 :\n")
            choice = int(menu_choice)
            if choice < 1 or choice > 4:
                raise ValueError(
                    f"You can choose between options 1-4, option {menu_choice} is not valid"
                )
            elif choice == 1:
                print("You chose to see your events...")
                get_data(choice, val_user)
            elif choice == 2:
                print("You chose to add a new event...")
                new_event(val_user)
            elif choice == 3:
                print("You chose to delete an event...")
                get_data(choice, val_user)
            else:
                print("Shame that you want to go, see you soon. Bye!")
                print("In case you want to start again press the refresh button")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def main():
    us_choice = display()
    if us_choice == "1":
        valid_user = user()
    else:
        valid_user = new_user()
    main_menu(valid_user)


main()