# Workflow
This document describes the workflow for this project.

## Backend Workflow
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

## Frontend Workflow
1. 
