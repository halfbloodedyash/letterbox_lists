# Letterbox Lists - Local Setup Guide

## 📌 Prerequisites
Make sure you have the following installed on your system before proceeding:

- Python (3.9 or later recommended) → [Download here](https://www.python.org/downloads/)
- pip (Python package manager)
- Virtual environment support (comes with Python)
- Git (optional, for cloning the repository)

## 🚀 Step 1: Clone the Repository

If you haven’t already, clone the repository using Git:
```sh
git clone https://github.com/halfbloodedyash/letterbox_lists.git
```
Then, navigate into the project directory:
```sh
cd letterbox_lists
```

## 📦 Step 2: Create a Virtual Environment

It’s best to use a virtual environment to manage dependencies.

### On macOS/Linux:
```sh
python3 -m venv venv
source venv/bin/activate
```

### On Windows (Command Prompt):
```sh
python -m venv venv
venv\Scripts\activate
```

Now you should see `(venv)` in your terminal, meaning the virtual environment is active.

## 📥 Step 3: Install Dependencies

Once the virtual environment is activated, install the required dependencies:
```sh
pip install -r requirements.txt
```
This will install Flask and other necessary libraries.

## ▶️ Step 4: Run the Flask App

Run the app using:
```sh
python app.py
```

Or, if using Flask CLI:
```sh
flask run
```

By default, Flask runs on **http://127.0.0.1:5000/**. Open it in your browser to verify the app is running.

## 🛑 Stopping the Server
To stop the server, press `CTRL + C` in the terminal.

To deactivate the virtual environment, run:
```sh
deactivate
```

## 🛠️ Troubleshooting

- **pip not found?** Try using `python -m pip install -r requirements.txt`.
- **Virtual environment not activating?** Ensure you’re using the correct command for your OS.
- **Port already in use?** Run `flask run --port=5001` to change the port.
- **Module not found?** Ensure dependencies are installed (`pip list`).

Happy coding! 🚀

