# Task 3 - Clone Repository
To begin inserting code into your repository that was created in [Task 2](task_2.md), you will need to create the reference of the repository on your local machine. To do this you will use a tool called Git to interact with the repository. Git is a version control system (VCS) that manages the history of changes to files. 

Git is a powerful tool that has a lot of features. However, in this lab we will focus on a few of the Git commands that you will use. 

| Command           | Description                      |
| ----------------- | -------------------------------- |
| git init          | Initializes a new Git repository |
| git clone `[url]` | Clones a remote repository to the local machine |
| git add `[file]`  | Adds a file to the staging area that is require to commit and push |
| git commit -m `"message"` | Commits the files in staging area with a message |
| git push          | Pushes the commit to the remote repository |
| git pull          | Fetches and merges changes from the remote repository to the local repository |
| git checkout -b `branch_name` | Creates a copy of the current branch to a new branch |


## Step 1: Create Personal Access Token
To clone, pull, and push code to the repository over HTTPS, you will need a personal access token that you will use which will grant access to communicate with the remote repository. 

1. Once you are logged in, click on your profile in the top right corner of the webpage. 
!!! note
    To login or sign up for a GitHub account, please follow the instructions in [Task 1](task_1.md).

2. From the drop down menu, click `Settings`

3. On the settings page, click `Developer Settings` in the left toolbar at the very bottom. 

4. Click `General New Token (classic)` and select the following scopes. 
    - repo
    - workflow
    - admin:org
    - user

5. Once you have selected all scopes, click the green `Generate Token` button

6. Copy the generated token and save it somewhere. 
    !!! note
    Whenever you have the option to pass in a passkey or token, paste this token as the Token for the security measure. 

## Step 2: Navigate to the Repository 
1. Once you are logged in, click on your profile in the top right corner of the webpage. 
!!! note
    To login or sign up for a GitHub account, please follow the instructions in [Task 1](task_1.md).

2. From the drop down menu, click `Your Repositories`

3. Click the Repository you created in [Task 2](task_2.md), (e.g github-actions-demo)

## Step 3: Copy Repository URL
1. On the homepage of the repository, click the green button that's labeled `Code`

2. In the dropdown menu, click the `Local` tab

3. Next, click on the `HTTPS` option

4. Copy the HTTPS Url by highlighting all the text or clicking on the two square icon to the right of the text box.

## Step 4: Open Local Terminal 
- **MacOS:** Press the Command & Space buttons on the keyboard, type `Terminal` and press enter

- **Windows:** Click the `Start` button *(usually Windows icon)* at the bottom left corner of the screen. Type `cmd` and press enter
!!! info
    Terminal, is a text based interface used to interact with different applications or tools instead of a Graphical User Interface (GUI). In the terminal you will execute command to perform actions such as `git add`.

## Step 5: Navigate to Desktop Directory
In the terminal window, enter in the following command to set the working directory to the local desktop 

- MacOS
    ```bash
    cd ~/Desktop
    ```
- Windows
    ```bash
    cd $HOME\Desktop
    ```

## Step 6: Clone Repository
You will use `git clone {repository url}` to create the local reference of your GitHub Repository
``` {.bash .no-copy}
git clone https://github.com/kourtneya/github-actions-demo.git
```
!!! info
    If the Private visibility was selected when creating the repository, you will need to enter you GitHub account credentials

## Step 7: Navigate inside local repository 
Once the cloning has completed, use the `cd {repository_name}` command to set the working directory to the local repository location
```{.bash .no-copy} 
cd github-actions-demo
```

## Step 8: View Files within Local Repository 
To view the files in the cloned location execute the following command. You shall see the files that were in the GitHub Repository in the browser

- MacOS
    ```bash
    ls
    ```
- Windows
    ```bash
    dir
    ```

```{.bash .no-copy}
-rw-r--r--   1 user  staff   233 Mar 25 10:36 README.md
```


<br>

**Congratulations!!** You have now clone the GitHub repository to your local machine.

<br>