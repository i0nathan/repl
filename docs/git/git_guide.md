# Vim Personal Command Guide
    - Adding Files to git involves 3 steps
        1. Add to the staging area (locally) =>
            ```bash
            $ git add [options: use -A to add all] <filename>
            ```
        2. Commit those changes to the local version control =>
            ```bash
            $ git commit -m "Commit message"
            ```
        3. Pushing changes to the distributed repository =>
            ```bash
            $ git push -u origin master
            ```

## To start a new local repository
    ```bash
    git init
    ```

## To clone a repository
    ```bash
    git clone <url> <where to clone>
    ```
