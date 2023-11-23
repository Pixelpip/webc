# webc

##Steps to run the App

1. Install Python

If you haven't installed Python yet, download and install it from the official Python website. During installation, make sure to check the box that says "Add Python to PATH" (for Windows) or install it via a package manager like brew (for macOS) to easily access Python from the command line.
2. Install Flask

Open a terminal or command prompt and install Flask using pip, Python's package manager:

bash

pip install Flask

Running a Flask App:
Windows:

    Set up the Flask App:
    Create a directory for your Flask app and navigate to it using the command prompt.

    Set the Environment:
    Set the environment variable for the Flask app (replace app.py with your actual Flask app file):

    bash

set FLASK_APP=app.py

Run the App:
Start the Flask development server:

bash

    flask run

macOS / Linux:

    Set up the Flask App:
    Create a directory for your Flask app and navigate to it using the terminal.

    Set the Environment:
    Set the environment variable for the Flask app (replace app.py with your actual Flask app file):

    bash

export FLASK_APP=app.py

Run the App:
Start the Flask development server:

bash

    flask run

Additional Notes:

    If you're using different filenames or file structures, adjust the FLASK_APP environment variable accordingly.
    By default, the Flask development server will run on http://127.0.0.1:5000/. You can access your Flask app by visiting this address in a web browser.

Remember, these are general instructions. Your specific setup might require additional configurations or considerations, especially when dealing with more complex applications or deployment scenarios.
