# Workflow
This document describes the workflow for this project.


## Changing the models
1. Make necessary changes to the models in trippy/models.py

2. Run the following command:
    ```
    python manage.py makemigrations trippy
    ```
    This will create a migrations file that tells Django what changes we would like to make to the database.

3. Run the following command:
    ```
    python manage.py migrate
    ```
    This will apply all migrations to the database.

## Run the local server
Open http://127.0.0.1:8000/ on a web browser after running the following command:
```
python manage.py runserver
```

## Login to admin site
1. Run the local server.
2. Use the following credentials:
    ```
    username: admin
    password: abc123!!
    ```
