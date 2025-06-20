# Task 5 - Push Python Application
The goal of this task is to become familiar with another Git command that will push all your changes in the local machine to the remote location in GitHub. This will ensure you can effectively communicate with the remote location. Everytime you change code in the local machine, you must push it to the remote repository to see the changes there and to kick off any integrated tasks associated with the repository in GitHub. 

## Step 1: Navigate to Local Repository in Terminal 

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

1b. If working directory is not at your local repository path use the `cd` command to get to the desire path. 

- MacOS <br>
```bash 
cd ~/Desktop/github-actions-demo
```

- Windows <br>
```bash
cd $HOME\Desktop\github-actions-demo
```

## Step 2: Add Files to Staging Area
There are a few of commands that need to be executed before pushing the changes to the GitHub repository. The first of them is `git add`. This command will add all or selective files to the staging area which is a temporary holding area for files that have been changed or added. Its like a buffer zone between your local machine and your remote repository. Once added in the staging area you can still make changes to the file(s) but you will need to execute the command again to add the changes to the staging area. 

Execute the following command to add all files to the staging area 

```bash
git add . 
```

## Step 3: Commit Changes 
Once all files have been added to the staging area, its now time to commit that changes in the staging area. The `git commit -m "message"` command will create a snapshot of the files the files in the staging area. The snapshot will be identified with a unique identifier called a **commit hash**. This hash is a way to reference the snapshots over time because every commit becomes part of the version history where you can view it later, revert to it, or compare it with other commits. 

1. To commit the files in the staging are execute the following command

    ```bash
    git commit -m "creating initial python application"
    ```

2. On the first commit, you may be prompt to configure your username and email using `git config`. This is extremely important for identifying who made changes to files within the repository. Git repositories are designed for collaboration where multiple users can work out of the same repository. Due to this type of collaboration knowing who made the commit is critical. The following commands configures your identity in Git. 

    ```bash
    git config user.name "YOUR NAME"
    ```
    ```bash
    git config user.email "YOUR EMAIL"
    ```

## Step 4: Push Commit to GitHib Repository
The last command in pushing your changes to GitHub is the `git push` command. This command will upload all your local commits to the remote repository. All of the commit histories you have performed in your local repository will be pushed to the remote repository with this command. Thus if you delete the local repository or simply get a new computer, you can still pull down all the change history from your remote repository. Think of it as a back up of your work in a cloud environment or a server running elsewhere. 

Execute the command below to upload your local changes to GitHub

```bash
git push origin main
```

## Step 5: Verify GitHub Repository Upload
Now that you have executed all the commands to upload your changes from the local repository to the GitHub repository, visit the GitHub website by click the hyperlink or typing [https://github.com](https://github.com)

1. Once you are logged in, click on your profile in the top right corner of the webpage. 
!!! note
    To login or sign up for a GitHub account, please follow the instructions in [Task 1](task_1.md).

2. From the drop down menu, click `Your Repositories`

3. Click the Repository you created in [Task 2](task_2.md), (e.g github-actions-demo)

4. On the homepage of the repository, you should see an `app.py` file in the table displayed. 


<br>

**Congratulations:** Your code has now been uploaded to GitHub using version control.

<br>
