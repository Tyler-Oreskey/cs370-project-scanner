## How to run this program

1. Make sure pipenv is installed by running the command: **pipenv --version**
    - if its not installed, run the command: **brew install pipenv**

2. Create a **.env** file in the root of this project directory
    - use the **.env.sample** file to see what is needed in the .env file
    - the .env file should contain:
    ```
    BASE_URL=enter api url
    ```

3. run the command in the root of the project directory: **pipenv install**
    - this will install all the dependencies needed to run this script.

4. run the script: **python3 script.py**