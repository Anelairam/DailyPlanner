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
I decided for the purpose of the application to use Google Sheets with two worksheets, users and events. The application interacts with the data that are registered in the users worksheet to validate the username/email and password. In the events worksheet the application reads,writes and deletes each user's events based on his choices

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
