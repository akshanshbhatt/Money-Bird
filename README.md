# Money Bird

## Local setup

Follow these steps to run the Money Bird app on your local machine:

1. Installing Python

    * **Linux (Ubuntu and similar distros)**

        ```sh
        sudo apt-get install python3-pip
        ```

    * **Windows**

        Go to https://www.python.org/downloads/ and download the latest version of Python setup executable.

        Open the setup and follow the commands to install Python on your system.

        Then, open command prompt and run the following commands:

        ```sh
        pip install --upgrade pip
        ```

    * **MacOS**

        Follow same steps mentioned for windows or if you have brew installed:

        ```sh
        brew update
        brew install python3
        ```

    Checking version of Python:

    * Linux and MacOS:

        ```sh
        python3 --version
        ```

    * Windows:

        ```sh
        python --version
        ```

1. Install Git

    * **Linux (Ubuntu and similar distros)**

        ```sh
        sudo apt-get install git
        ```

    * **Windows**

        Follow the steps on https://git-scm.com/downloads to install Git on your system.

    * **MacOS**

        Git comes already installed with MacOS.

1. Cloning the repository

    ```sh
    git clone https://github.com/akshanshbhatt/Money-Bird.git
    cd Money-Bird
    ```

1. Creating a Virtual Environment in Python

    ```sh
    python3 -m venv moneybird-env
    source moneybird-env/bin/activate
    pip install -r requirements.txt
    ```

1. **Creating config file in the root of the repository** **

    Create a file named `config.py` in the root of the repository. This file will contain your API credentials. Your API credentials should remain secret.

    This file is already included in the `.gitignore` file. Therefore you don't have to worry about committing your API credentials when you make any contributions to the repository.

    <br/>

    Template of the config file:

    ```python
    ALPHA_VANTAGE_API_KEY = 'YOUR_API_KEY'
    COIN_API_KEY = 'YOUR_API_KEY'
    ```

1. Running the app

    ```sh
    flask run
    ```

    You can now go to http://localhost:5000/ to see the app in action.

## Contributing

In order to submit a patch:

1. Fork the repository on GitHub. This will create a new repository on GitHub under your account with the same name as the original repository.

1. If you have already cloned the repository (following the steps mentioned above), you don't need to clone it again. Just make sure that your `origin` remote URL is set to the newly forked one and `upstream` is set to this repo's original URL. On running `git remote -v` you should see the following:

    ```
    origin	https://github.com/{YOUR_GH_USERNAME}/Money-Bird.git (fetch)
    origin	https://github.com/{YOUR_GH_USERNAME}/Money-Bird.git (push)
    upstream	https://github.com/akshanshbhatt/Money-Bird.git (fetch)
    upstream	https://github.com/akshanshbhatt/Money-Bird.git (push)
    ```

1. Make sure to fetch the upstream repository before making any changes. Use `git fetch upstream` to fetch the latest changes from the upstream repository. You can also use `git pull upstream` to do the same. You can also use `git merge upstream/master` to merge the latest changes from the upstream repository.

1. Commit the changes to the forked repository. You can then visit your forked repo URL on GitHub and see the changes and make a pull request.
