Assignment 3 – Django ORM Cash Register
=======================================
## Group 14
Hibba Khan, Leona Krasniqi, and Tanzina Eusra
## Overview

The assignment part 1 implements a simple Cash Register application, and it uses the Django ORM framework. It will populate a database with product UPC codes, names, and prices. Scan a product by entering its UPC and display the name and price. Then, exit the program when the user types 'done'. The key files and folders are below.

```
Django-ORM/
│
├── db/                     # This has the Django app files
│   ├── migrations/         # these are the automatically created migration files when we migrated
│   ├── screenshots/        # these are the screenshots showing setup and execution steps
│   │   ├── Step 1.png
│   │   ├── Step 2.png
│   │   ├── Step 3.png
│   │   └── Step 4.png
│   ├── __init__.py         # this is what initializes the db module
│   └── models.py           # this defines the Product model (UPC, name, price)
│
├── main.py                 # this is the main code that populates and scans the database
├── manage.py               # this is the Django management for migrations
├── settings.py             # this is the Django configuration file
├── db.sqlite3              # this is the SQLite database file that was created after migration
└── README.md               # The current file that outlines the assignment and steps
```

## Step 1:

Creating and activating the virtual environment before running the Django ORM commands. When the environment is active we can see the (venv) before the prompt. You will have to make sure that you have django and pip installed. Run these commands in the terminal, we used VS code.

![Step 1 Screenshot](https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-14/blob/master/screenshots/Step%201.png?raw=true)

## Step 2:

Running Database Migrations to build the database structure. You need to run these commands to create the tables for the project, and the last message shows that the database is created.

![Step 2 Screenshot](https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-14/blob/master/screenshots/Step%202.png?raw=true)

## Step 3:

Now you can start the program using the command below, it will automatically populate the database with sample products. It will show a list of items with the UPC codes, names and their prices.

![Step 3 Screenshot](https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-14/blob/master/screenshots/Step%203.png?raw=true)

## Step 4:

Scanning the products using their UPC is simple. Once prompted to enter the UPC, enter a product UPC from the list, you can keep entering the UPCs until you want to finish to exit the system. The following shows this demonstrated:

![Step 4 Screenshot](https://github.com/OTUSOFE365025/assignment-3-django-and-energy-group-14/blob/master/screenshots/Step%204.png?raw=true)

## How It Works
- When main.py runs, it checks if the product database is empty
- If it is empty, then it is then the program adds five sample products.
- Then it shows all the added and now available products. 
- You can enter a UPC to view the product name and price.
- Typing "done" ends the program and closes it.

## Technologies we used
- Python as the main programming language
- Django ORM to handle the database operations
- SQLite as the database 
- Visual Studio Code as the coding environment 
