## How to run this program

1. Make sure pipenv is installed by running the command: **pipenv --version**
    - If not installed, run the command: **brew install pipenv**

2. Create a **.env** file in the root of this project directory
    - Use the **.env.sample** file to see what is needed in the .env file
    - The .env file should contain:
    ```
    BASE_URL=enter_api_url
    ```

3. Run the command in the root of the project directory: **pipenv install**
    - This will install all script dependencies.

4. Run the script: **python3 script.py**
