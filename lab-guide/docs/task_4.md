# Task 4 - Create Python Application
If [Task 1](task_1.md) - [Task 3](task_3.md) are completed, lets begin to create the python application. The python application is a simple application that has a single RESTful endpoint. The endpoint is a health endpoint that will have the status of OK. This application will be instrumental in the CI/CD setup with GitHub Actions a little later in the lab. 

## Step 1: Open Code Editor
This lab can work with any text editor but for the purpose of this lab, the text editor that will be reference is [Visual Studio Code](https://code.visualstudio.com/). 

!!! note
    The lab machines at Cisco Live have Visual Studio Code (VS Code) installed. 

1. Open the terminal, 

    - **MacOS:** Press the Command & Space buttons on the keyboard, type `Terminal` and press enter

    - **Windows:** Click the `Start` button *(usually Windows icon)* at the bottom left corner of the screen. Type `cmd` and press enter

2. Enter in the following command to set the working directory to the local repository. *Remember to replace the name of the repository if needed*

    - MacOS
        ```bash
        cd ~/Desktop/github-actions-demo
        ```
    - Windows
        ```bash
        cd Desktop/github-actions-demo
        ```

3. Type the following command in the terminal to open Visual Studio Code in the repository's location. 
```bash
code . 
```

## Step 2: Create New File in VS Code
1. At the top left corner in the tool bar, click `File`

2. In the drop down menu select `New -> File`

3. Name the file `app.py`

## Step 3: Import Flask
Flask is a lightweight library for python that is design to quickly create a RESTful service with very little configuration. 

!!! info
    RESTful or RESTful API (Representational State Transfer) is a method commonly used to create APIs (Application Programming Interface) that communicates of the HTTP network.

Import flask in the `app.py` file using the following code.
```python
from flask import Flask, jsonify
```

!!! note
    **jsonify** is another python library used to parse, transform, and write json objects

## Step 4: Initialize Flask
Now that you have imported the Flask framework, initialize flask to create a web server when the application starts. Insert the following code in the same `app.py` under the import statement.  

```python 
app = Flask (__name__)
```

## Step 5: Create Health API Endpoint 
If the application was to start now it wouldn't have any routes and you would see a `HTTP 404 NOT FOUND` error when navigating to your service in the web browser. To avoid this, create a `/health` route that returns a JSON response signifying that the web service is up and running. 

```python
@app.route('/health', methods=['GET']) 
def health_check():
    return jsonify({'status':'OK'})
```

- `@app.route('/health', methods=['GET'])` is a method decorator which is a function that takes two arguments. The first argument is the route `/health`. This is the path you want to see the expected results The second argument is the HTTP method you expect our route to respond on. To learn more about HTTP methods, [W3schools](https://www.w3schools.com/tags/ref_httpmethods.asp) is a good resource. 

- `def health_check():` is a function declaration in python. Always start a function in pythong with the `def` keyword follow by the name of your choice. 

- `return jsonify({'status':'OK'})` is the response you want to give when this method is invoked. The `return` keyword is used to respond with a value and terminate the function. **jsonify** is used to return the string as a JSON value.

## Step 6: Python Main
Every web service written in python has an entrypoint. The common and recommended practice to create this entrypoint is using the `if __name__ == "__main__":` idiom. Using this ensures that the indented code below will only execute when the script is ran directly. (e.g python app.py)

Insert the following code to create the entrypoint to the application

```python
if __name__ == '__main__':
    app.run(debug=True)
```

## Step 7: Code Overview 
Your `app.py` file should be similar to the code below

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET']) 
def health_check():
    return jsonify({'status':'OK'})

if __name__ == '__main__':
    app.run(debug=True)
```

## Step 8: Save File
1a. In the top left corner, click `File`, then `Save` in the drop down menu

1b. Use the respective shortcuts to save the file 

- MacOS <br>
<kbd>Command</kbd> + <kbd>S</kbd>

- Windows <br>
<kbd>Ctrl</kbd> + <kbd>S</kbd>

## Step 9: Install Flask
Although you imported flask into the python application, however, that's simple not enough. Importing the library allows you to use it in your code base. You need to install flask because its a third-party library and is not bundled into the python application. You need to install the library so that the python interpret can recognize it during runtime. 

To install flask execute the following command in your terminal window
```bash
pip install Flask --break-system-packages
```

## Step 10: Run Python application
Now that the code has been written and that the library has been installed. You can perform the next few steps to start the Python web service. 

1. In your terminal, ensure you that your working directory is at your local repository path. 

- MacOS <br>
```bash 
pwd
```
```{.bash .no-copy}
/Users/(username)/Desktop/github-actions-demo
```

- Windows <br>
```bash
pwd
```
```{.bash .no-copy}
\Users\(username)\Desktop\github-actions-demo
```

2. Starte the python application
```bash 
python app.py
```

## Step 11: Test Health Endpoint 
The application is now running, let's open a browser and navigate to the application. 

1. Open new browser window or a new tab in the browser 

2. In the address bar, type in the following address or click the hyperlink to view the application. [http://127.0.0.1:5000/health](http://127.0.0.1:5000/health)

3. You should see a webpage with `{"status": "OK"}`

4. To stop the application, in the terminal window press <kbd>Ctrl</kbd> + <kbd>C</kbd> on the keyboard

<br>

**Congratulations!!** You have created a RESTful API application.

<br>