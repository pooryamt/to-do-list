To-Do List CLI

A command-line To-Do List application built with Python. It allows users to manage their tasks, track their status, and save task data locally between program executions.

Features

- Add new tasks.
- View all tasks.
- Search for a task by ID.
- Edit existing tasks.
- Delete tasks with confirmation.
- Mark tasks as completed.
- View pending tasks.
- View completed tasks.
- Assign priorities to tasks.
- Set an optional due date.
- Automatically save task changes to a local JSON file.

Requirements

- Python 3
- No external Python packages are required.

The application uses Python's standard library, including the "json" module, to manage local task data.

Getting Started

1. Download or Clone the Repository

Clone the repository from GitHub, or download the project files to your computer.

2. Open the Project Directory

Open the "to_do_list" directory in your terminal or code editor.

3. Run the Application

Run the following command:

python to_do_list.py

On Windows, you can also use:

py to_do_list.py

Follow the instructions displayed in the command-line menu to manage your tasks.

Data Storage

The application stores task data in a local file named "tasks.json".

Task changes are saved automatically, allowing the application to load previously saved tasks when it is started again.

The "tasks.json" file is excluded from version control because it may contain personal or temporary task data. It is created locally when the application saves its data.

When running the application for the first time without an existing data file, the application starts with an empty task list.

Project Structure

to_do_list/
├── to_do_list.py
├── README.md
├── .gitignore
└── tasks.json

The "tasks.json" file is generated or maintained locally and is not included in the GitHub repository.

Learning Goals

This project was developed to practice Python programming concepts, including:

- Functions and separation of responsibilities
- Lists and dictionaries
- Input validation and conditional logic
- Searching, adding, editing, and deleting data
- File handling
- JSON serialization and deserialization
- Exception handling
- Automatic data persistence

License

No license has been specified for this project.