# Task 7 - Python Unit Test
Before you can create a Test Pipeline in GitHub Actions, you first need to create unit test within the Python application. Unit Tests are essential for verifying that each chunk of code, such as functions, perform as expected. Unit Tests also help catch bugs early and assist in verifying that any refactoring or updates doesn't break existing functionality. These tests improves the quality of the code and builds confidence that the software can be released without critical risks. 

## Step 1: Create a New Test File
In Visual Studio Code, first click anywhere in the open area on the left side toolbar in the Project Explorer. This will ensure that when you create the new file it will be created in the project's root directory. The new file should appear at the same level as the `app.py`, `requirement.text`, and `Dockerfile`. 

1. At top left corner in the tool bar, click `File`

2. In the drop down menu select `New -> File`

3. Name the file `test_app.py`

## Step 2: Import Testing Module
The most basic way to test functions in python is to use the built-in testing framework. The `unittest` library provides a structured way to write and run unit tests. The frame work includes a set of functions called assertions that check for conditions and raise errors if those conditions are not met which will result in a failed test. In the `test_app.py` file, import the unit test library and the app module that you want to test. 

```python
import unittest
from app import app
```

## Step 3: Create the Test Class Method
To create test in Python is by creating test cases by using the `unittest.TestCase`. In these classes, you define methods that begin with `test_`. Each of the methods will test a specific part of the code. In this lab, the python application only has one function that is an HTTP endpoint that returns a JSON response. Create the test class method that accepts `unittest.TestCase` as a parameter. 

```python
class TestHealthEndpoint(unittest.TestCase):
```

## Step 4: Implement Test Scenario
Indented inside of the `TestHealthEndpoint` class, define a method to test the `/health` endpoint of your application. The Flask framework has provides a method to return a test client which allows you to send fake HTTP request which is perfect for unit tests since it does so without a running server. Just like a running server, the test client will route your request to the intended method for the API endpoint. Create the test health endpoint method and verify the correct result using assertions. 

```python
class TestHealthEndpoint(unittest.TestCase):
    def test_health_endpoint(self):
        apiTest = app.test_client(self)
        resp = apiTest.get('/health', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, {'status':'OK'})
```
    
- **`apiTest = app.test_client(self)`**: Declares  the `apiTest` variable that acts as an reference to the fake http client. `self` is a keyword used within class methods to refer to the current instance of the class
- **`resp = apiTest.get('/health', content_type='application/json')`**: Declares the variable `resp` variable that acts as a reference to the response from the method that is called when invoking the `/health` API endpoint 
- **`self.assertEqual(resp.status_code, 200)`**: Returns true or false if the response status code from the HTTP request is equal to 200 
- **`self.assertEqual(resp.json, {'status':'OK'})`**: Returns true or false if the response body from the HTTP request is equal to the response provided by the method that is called when invoking the `/health` API endpoint 

## Step 5: Complete Unit Test Code
Here is the complete unit test code of the API health endpoint.

```python
import unittest
from app import app

class TestHealthEndpoint(unittest.TestCase):
    def test_health_endpoint(self):
        apiTest = app.test_client(self)
        resp = apiTest.get('/health', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, {'status':'OK'})
```

## Step 6: Save Unit Test File
1a. In the top left corner, click `File`, then `Save` in the drop down menu

1b. Use the respective shortcuts to save the file 

- MacOS <br>
<kbd>Command</kbd> + <kbd>S</kbd>

- Windows <br>
<kbd>Ctrl</kbd> + <kbd>S</kbd>

## Step 7: Run Python Unit Test
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

    - If working directory is not at your local repository path use the `cd` command to get to the desire path.

        - MacOS <br>
        ```bash 
        cd ~/Desktop/github-actions-demo
        ```

        - Windows <br>
        ```bash
        cd $HOME\Desktop\github-actions-demo
        ```

2. Execute the following command to run the unit test locally.

    ```bash
    python -m unittest test_app.py
    ```

<br>

**Congratulations:** You have now created a python unit test. Next up, creating the CI/CD pipeline to execute the unit test.

<br>