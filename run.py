import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from email_validator import validate_email


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
    global currenttime
    currentday = datetime.now()
    currentday = currentday.strftime("%d-%m-%Y")
    currenttime = datetime.now()
    currenttime = currenttime.strftime("%H.%M")
    print(currentday, currenttime)
    print("Welcome to the Daily Planner")
    while True:
        try:
            choice = input("If you are a new user please enter 0 if you" +
                           "already are a user enter 1:\n")
            if choice != "1" and choice != "0":
                raise ValueError(
                    "Enter 0 for excisting user or 1 for new user," +
                    f"you entered: {choice}"
                )
            else:
                return choice
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")


def validEmail(userEmail):
    try:
        valid = validate_email(userEmail)
        userEmail = valid.email
        return userEmail
    except Exception:
        print("The email you provided is not valid please try again")


def user_validation(userd, worksheet):
    """
    Using user's input the fuction runs a for loop through the users
    worksheet and check if the provided data are valid
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
            username = input("Please enter your username:\n")
            passwrod = input("Please enter your password:\n")
            user_data.append(username)
            user_data.append(passwrod)
            print(f"Hello {username} processing the data you provided... ")
            print(user_data)
            val_username = user_validation(user_data, "users")
            if val_username != 0:
                validation = False
                return user_data
            else:
                user_data.pop(0)
                user_data.pop(0)
                raise ValueError(
                    "The username or the password you have entered is wrong," +
                    "please try again.")
        except ValueError as e:
            print(f"Invalid data: {e}")


def new_user():
    """
    Asking for new user's data
        -Ask the user to add his username and password
        -Run user's information from the validator if the
            username already exists inform the user that
            the username exists and provide a new one
    """
    id_sheet = SHEET.worksheet("users")
    new_entry = []
    while True:
        try:
            while True:
                n_user = input("Please enter your email address: \n")
                validatedMail = validEmail(n_user)
                if validatedMail == n_user:
                    break
            f_name = input("Please enter your name: \n")
            while True:
                n_password = input("Please enter your password: \n")
                v_password = input("Re enter your password for validation: \n")
                print("Hello we are now processing your data.")
                if n_password != v_password:
                    print(f"Unfortunatelly {f_name} the password you" +
                          "provided do not match the original, please" +
                          "try again...")
                else:
                    break
            print(f"Welcome to Daily Planner {f_name}, we will direct you to" +
                  "the main menu.")
            new_entry.append(n_user)
            new_entry.append(n_password)
            new_entry.append(f_name)
            id_sheet.append_row(new_entry)
            return n_user
        except Exception:
            print(f"You have entered: '{f_name}'. This is not a" +
                  "valid email, please try again...")


def get_data(action, user):
    """
    Loop through the database and display only
    the data that are corresponding to today's date
    """
    events_sheet = SHEET.worksheet("events")
    ids = events_sheet.col_values(1)
    user_ids = events_sheet.col_values(2)
    days = events_sheet.col_values(3)
    hours = events_sheet.col_values(4)
    subjects = events_sheet.col_values(5)
    persons = events_sheet.col_values(6)
    locations = events_sheet.col_values(7)
    eventCounter = 0
    if action == 1:
        print(f"{user} We are searching for your events...\n")
        for id, user_id, day, hour, subject, person, location in zip(ids, user_ids, days, hours, subjects, persons, locations):
            if user_id == user[0]:
                eventCounter += 1
                print(f"#{id}. {day} Meeting at {hour}" +
                      f" with {person} at {location} for {subject} \n")
        if eventCounter == 0:
            print(f"{user} you do not have any events scheduled.")
    else:
        print(f"{user} you have scheduled the following events:\n")
        for id, user_id, day, hour, subject, person, location in zip(ids, user_ids, days, hours, subjects, persons, locations):
            if user_id == user[0]:
                print(f"#{id}. {day} Meeting at {hour}" +
                      f" with {person} at {location} for {subject} \n")
        while True:
            try:
                del_event = input("Choose which event you want to delete" +
                                  "by entering it's id number without the #: ")
                if int(del_event) < len(ids):
                    cell = events_sheet.find(del_event)
                    events_sheet.delete_row(cell.row)
                    break
                else:
                    raise ValueError(
                        "The id you have entered does not exist.")
            except ValueError as e:
                print(f"Indalid input. {e} Please try again")


def new_event(user):
    """
    Ask the user to insert the new event's information in a specific way
    Add all the user's information into the db
    """
    events_sheet = SHEET.worksheet("events")
    event_id = events_sheet.col_values(1)
    event_data = []
    while True:
        try:
            while True:
                try:
                    while True:
                        day_input = input("Please enter the date as" +
                                          "(DD-MM-YYYY): ")
                        
                        if datetime.strptime(day_input, "%d-%m-%Y"):
                            
                            #userDay, userMonth, userYear = day_input.split("-")
                            #todayDay, todayMonth, todayYear =
                            #currentday.split('-')
                            #d1 = [userDay, userMonth, userYear]
                            #d2 = [todayDay, todayMonth, todayYear]
                            #d1 = datetime.strptime(day_input, "%d-%m-%Y")
                            #d2 = datetime.strptime(currentday, "%d-%m-%Y")
                            break
                        day_input = datetime.strptime(day_input, "%d-%m-%Y")
                    if day_input < currentday or day_input == currentday:
                        break
                    else:
                        raise ValueError(
                            "You might have entered an old date."
                        )
                except ValueError as e:
                    print(f"The date you provided it is not correct, {e}," +
                          "please try again...")
            while True:
                try:
                    while True:
                        time = input("Please ente the time of your event as" +
                                     "(HH.MM) in 24-hour format: ")
                        if datetime.strptime(time, "%H.%M"):
                            userHour, userMinute = time.split(".")
                            todayHour, todayMinute = currenttime.split(".")
                            t1 = [userHour, userMinute]
                            t2 = [todayHour, todayMinute]
                        break
                    if d1 == d2 and t1 > t2:
                        break
                    elif d1 > d2:
                        break
                    else:
                        raise ValueError(
                            "The time you have entered has passed. "
                        )
                except ValueError as e:
                    print(f"The time you provided it is not correct, {e}," +
                          "please try again...")
            description = input("What is the subject of the event?")
            who = input("Who are you going to meet? ")
            location = input("Where is the meeting? ")
            print("Here are the details of you new event: \n")
            print(f"Date:{day_input}, Time:{time}, Subject:{description}," +
                  f"With:{who}, At:{location}")
            while True:
                update_event = input("Are the information correct? " +
                                     "Enter 1 as yes and 0 as no: ")
                if int(update_event) == 1 or int(update_event) == 0:
                    break
            if int(update_event) == 1:
                event_data.append(len(event_id)+1)
                event_data.append(user[0])
                event_data.append(day_input)
                event_data.append(time)
                event_data.append(description)
                event_data.append(who)
                event_data.append(location)
                events_sheet.append_row(event_data)
                print("Your event list is now updated")
                break
            else:
                raise ValueError(
                    "Please enter again the information of your new event."
                )
        except ValueError as e:
            print(f"Data are not correct. {e}")


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
            print(" 1.Display my events for today\n", "2.Add a new event\n", "3.Delete an event\n", "4.Exit\n")
            menu_choice = input("Please choose from the options 1-4 :\n")
            choice = int(menu_choice)
            if choice < 1 or choice > 4:
                raise ValueError(
                    "You can choose between options 1-4, option" +
                    f"{menu_choice} is not valid"
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
                print("In case you want to start again press the refresh" +
                      "button")
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
