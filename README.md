# Daily Planner

Welcome to the Daily Planner, a Python application which runs in the Code Institure mock terminal on Heroku.

The purpose of this application is for the user to register, preview and delete his events.
Each user has access on his own events only and need to be an authorised user in order to interact with the data.

Here is the live version of my project.


In order for the user to start register his events he first needs to be a valid user of the application.to login and start registe his events first of all he needs to have an accountThis is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
