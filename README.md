# python-newsfeed
News application restructured to use python back-end

## Installation

1. Set Up the Git Workflow
    1. Create and clone repository
    2. Create a new branch (git checkout -b <branch_name>)
    3. Create a .gitignore file

2. Set Up Python Environment (Windows)
    1. Enter the following commands in the terminal
        1. `python -m venv venv` or `python3 -m venv venv` (if computer requires it)
        2. `.\venv\Scripts\activate` to activate the virtual environment
        (if this does not work, enter `Set-ExecutionPolicy Unrestricted -Scope Process` in powershell, then try activation again) use `deactivate` to exit the virtual environment
    **NOTE: windows users would need to use powershell instead of bash as it would not run virtual environment for python

3. Create a Route
   1. Install Flask (just like Node.js has npm, Python has its own package manager called pip. The pip command installs along with Python, requiring no additional setup. Be sure that venv is running so taht dependencies get put into the right place.)
        1. `pip install flask`
    2. Create the App Package
        1. Create a new folder called app
        2. Create a new file called __init__.py (two underscores on each side of init)
        3. Start Flask server by running `python -m flask run` (this only works if the entry point of the app uses the default name of app)
    ** NOTE: The __init__.py file of a Python package corresponds to the index.js file of a Node.js module.

    ** Python Code Formatting: curly braces don't signify code blocks, nor do semicolons end expressions. Instead, Python uses indentation. So in the create_app() function, we indent everything the function contains by two spaces.
    3. Start the Flask Server
        1. `python -m flask run`
        ** Run command `$env:FLASK_APP = "app"` in powershell to set the environment variable

4. Create the Home View Routes
At this point, the app is set up to serve more complete pages. Now it's time to turn the attention to front end.
    1. Jinja2 Templating - In a Node.js project, templating requires a separate library (like Handlebars.js), but Flask has built-in templating. When Flask is installed, the Jinja2 template engine is also installed. Like Handlebars.js, Jinja allows you to design placeholders in your HTML content, to be filled in with data from the server.
    2. Create a routes folder in the app folder
    3. Create a new file inside routes folder called __init__.py and home.py
    ** NOTE: The routes directory is now a package because of the presence of the __init__.py file. The home.py file is a module within the routes package.