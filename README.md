# Arva Field Management System

## Introduction
Arva Field Management System is a web application built with Django that allows users to manage their Fields. Users can create, update, and delete Fields.

## Features
- Create, update, and delete Fields
- View and browse existing client Fields
- Upload CSV files to import client Field data into the database

## Getting started

Follow the instructions below to get started with Arva Field Management System and run the project locally on your machine

### Prerequisites

- Python 3.10 or higher
- Django 4.2.4 or higher

### Installation

1. Clone the repo:
    ```git clone https://github.com/kontrol/arva_field_management.git```

2. cd into the project directory:
    ```cd arva_field_management```

3. Create virtual environment:
    ```python3 -m venv venv```

4. Activate virtual environment:
    On Mac/Linux: ```source venv/bin/activate```
    On Windows: ```venv\Scripts\activate```
    
5. Install dependencies:
    ```pip install -r requirements.txt```

6. Run migrations:
    ```python manage.py migrate```

### Running the project

1. Run the server:
    ```python manage.py runserver```

2. Open the project in your browser at http://127.0.0.1:8000/

3. Navigate
    - Click on "Browse Existing Clients" to view the list of clients and their fields
    - Click on "Upload CSV" to import client data from a CSV file 
        - The CSV file must have the following columns: "field_name", "field_location", "acreage", "field_type"
        - The CSV file name must match the client name

    
## Notes
- I made a decision to go with Django as it's a very common framework for Python web development.  I have experience with it and felt I could get the task done in a timely manner.  I also considered Flask, but I felt that I could modify some models and views and get the project done quicker with Django.
- I made a decision to use SQLite as the database mainly because it came with Django and I didn't have to mess around with any db hooks.  PostgreSQL would have been my choice if I'm trying to go production ready.
- There are some other considerations I had as well, such as doing a completely different type of DB, such as a graph database, but I felt that would have been overkill for this project.
- The project is not styled.  Likely I would have used Vue.js for the front-end and Django for the back-end. But I made a decision to use Django for the front-end as well to save time.  There are a couple of other ways as well, React, Angular, etc.  I could have also used a CSS framework such as Bootstrap or Tailwind.  
- The project does not have any tests.  I would have used pytest for testing, but for times sake I did not write any tests.
- The project does not have any authentication or authorization. I would have used Django's built-in authentication and authorization or Django Rest Framework.  The requirements didn't specify any, but from the nature of the problem, I would assume that authentication and authorization would be required.
- The project does not have any logging. For logging, I would probably do something in line with the 12-factor app methodology, such as Sentry. 
- The project does not have much in the way of error handling. There are a couple different ways I would have handled it. Try/except blocks, Django's built-in error handling, or Django Rest Framework's built-in error handling.

## Future Improvements
- Add ability to add new clients in app instead of through the Django admin or migrations
- Add ability to add, edit, update, delete Channel Partners in app instead of through the Django admin or migrations
- Add CSS to make it look better
- Add authentication and authorization
- Add logging
- Add error handling
- Add tests


