To activate the Pipenv shell, navigate to the directory where your Pipfile is located, then enter the following command:

```bash
pipenv shell
```

This command will create a virtual environment (if it doesn’t already exist) and activate it. You’ll see your command prompt change to indicate that you’re now inside the Pipenv shell.

If you need to exit the Pipenv shell, simply type:
```bash
pipenv exit
```

If you're using Pipenv and want to install these packages into your Pipenv environment, you’ll need to install them manually since Pipenv uses a Pipfile instead of requirements.txt. You can convert requirements.txt to a Pipfile by running:

```bash
pipenv install -r requirements.txt
```

This will add each package from requirements.txt into your Pipfile and install them in the virtual environment managed by Pipenv.

To run the Python app using Pipenv, follow these steps:

1. **Ensure you have Pipenv installed**:
   If you don't have Pipenv installed, you can install it using:
   ```sh
   pip install pipenv
   ```

2. **Create a Pipenv environment and install dependencies**:
   Create a 

Pipfile

 and install the necessary dependencies (`selenium` in this case):
   ```sh
   pipenv install selenium
   ```

3. **Add the ChromeDriver dependency**:
   Make sure you have the ChromeDriver executable downloaded and its path set correctly in the script.

4. **Run the app**:
   Use Pipenv to run your Python script:
   ```sh
   pipenv run python your_script.py
   ```

Here is a summary of the commands you need to run:

```sh
pipenv run python app.py
```

This will set up the environment and execute your script within the Pipenv-managed virtual environment.