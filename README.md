# Daily Planner

Welcome to the Daily Planner, a Python application which runs in the Code Institure mock terminal on Heroku.

The purpose of this application is for the user to register, preview and delete his events.
Each user has access on his own events only and need to be an authorised user in order to interact with the data.

Here is the live version of my project.

## How to use the application
In order for the user to start register his events he has to enroll into the application's system. If he is already a user he can log in and if not, he can register and become a user. For a user to log in it is required a valid email and password which he had already entered during his registration. For any new user the application will request a few informarion, validate them and then register the new person as a valid user.
When the validation of the user is completed, the application will provide the user a 4 choice menu from which he can navigate through the application, interact with the data by viewing existing events, adding new events, delete events and exit.

## Features
### Existing Features

* Welcome message with information regardin the current date and entry start menu
* (Entry picture)
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Future Features

Future features that had been thought through the deployment of the application and are planned to be added in the application in the new future are
* Option for the user to edit the existing events
* Option for the user to change password and username
* Option for the events of the user to be displayed per day, per month and future

## Data Model
I decided for the purpose of the application to use Google Sheets with two worksheets, users and events. The application interacts with the data that are registered in the users worksheet to validate the username/email and password. In the events worksheet the application reads,writes and deletes each user's events based on his choices.

## Testing
I have manually tested the project applying the following:
*Given valid and invalid input combinations:
  *Invalid email address formats
  *Invalid username and password
  *Invalid date and time combination while adding a new event
*Tested in Heroku and gitpod terminal
*Passed the code thourhg a PEP8 validator

## Bugs
### Solved bugs

* When I was trying to access certain data for user validation a type error occured at the iteration statement. I fixed this issue by converting the userd into a tupple using:   tuple(userd)
* During the process of displaying the events and giving the user the ability to delete any desired event of his, I realised that every event should have a unique id in order to be recognised from the others that the user had. In order to fix this issue I created a new column into the events worksheet in which every new event will be assigned with a unique number. Providing the number to the user and asking for the desired event with the unique number to be deleted, I targeted the event's row using the:
    **cell = events_sheet.find(del_event)
    **events_sheet.delete_row(cell.row) 
    
### Reamining Bugs

During the testing period it was spotted that there was an issue with the date validation regarding the comparison with the past and present or future dates.
Steps that had been followed till now for resolving this issue are:
* Convert the data type and compare
* Try different types of data comparison and reverse

## Validators Test

## Deployment
This project was deployed using the Code Institure's terminal Heroku.

Steps followed for deployment:
* Clone of the repository from code institute's template
* Create new Heroku app
* Set the Config Vars
* Set the buildpacks to Python and NodeJs
* Link the application to the repository
* Deploy the project

## Credits
Deployment:
* Code Institute deployment terminal
* https://sempioneer.com/python-for-seo/google-sheets-with-python/
* https://docs.gspread.org/en/latest/user-guide.html
* https://www.geeksforgeeks.org/comparing-dates-python/
* https://www.kite.com/python/answers/how-to-validate-a-date-string-format-in-python
* https://pypi.org/project/email-validator/
* My mentor for the great support and guidance
* Slack community supportive with solution ideas by facing similar issues

-----
Thank you!
