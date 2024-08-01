# Task Manager Application

## Overview

This project is a basic Task Manager application that helps users manage their to-do tasks. The application includes features such as user registration, login, task creation, viewing, updating, and deletion. It is built using Python and utilizes a simple SQLite database to store user credentials and tasks.

## Features

1. **User Registration**: Users can register with a unique username and password.
2. **User Login**: Registered users can log in to the application using their credentials.
3. **Create Task**: Users can create new tasks by providing a title and description.
4. **View Tasks**: Users can view a list of their created tasks.
5. **Update Task**: Users can update the title and description of their existing tasks.
6. **Delete Task**: Users can delete their tasks when they are completed.

## Requirements

- Python 3.8 or higher
- `pip` package manager


## Usage
### Running the Application
To start the application, run the following command:

```sh
python app.py
```
### Interacting with the Application
1. Register a New User
Open the application and navigate to the registration section. Provide a unique username and password to create a new account.

2. Login

Use the registered username and password to log in to the application.

3. Create a Task

After logging in, navigate to the task creation section. Provide a title and description for the new task.

4. View Tasks

View the list of all tasks you have created.

5. Update a Task

Select a task from the list and update its title and description.

6. Delete a Task

Select a task from the list and delete it once it is completed.

7. Code Structure
```arduino
.
├── config/
│   ├── agents.yaml
│   ├── tasks.yaml
├── src/
│   ├── python/
│   │   ├── crew.py
│   │   ├── app.py
│   │   └── init_db.py
├── .gitignore
├── README.md
├── requirements.txt
└── app.db
```
config/agents.yaml: Configuration for the agents used in the crewAI workflow.
config/tasks.yaml: Configuration for the tasks used in the crewAI workflow.
src/python/crew.py: Main script defining the agents, tasks, and crew for the crewAI workflow.
src/python/app.py: Main application script for running the task manager.
src/python/init_db.py: Script to initialize the SQLite database.
requirements.txt: List of Python dependencies.
