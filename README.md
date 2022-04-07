<p align="center">
<img src=https://user-images.githubusercontent.com/53227127/162168308-f5b3249e-1cd5-4eae-b604-b34ef8d40f3a.png></img>
</p>

# Money Bird

Stock trading can be very tedious and challenging, especially when someone is a beginner. Most of the time, novices blindly trust unverified online sources such as tips from self-acclaimed "experts" or fishy investing forums. News can be cited as trusted sources, but it has a delay factor. We need something faster than news because, in the financial world, results can change in an eye blink. Today, social media is the king. Nothing can beat the speed at which information travels through social media. You can find information related to events that even most local news outlets don't cover on social media.

Talking about social media and finance, Finance Twitter is a reasonably mature place where people discuss their financial viewpoints. With features such as cashtags ($ hashtags) and crypto integrations, Twitter is the place for quality financial data. It is real-time (very, very low latency), trustable, and user-friendly (Twitter's API is a well-documented API, better than any other social media platform).

After analyzing these potential features of the platform, we decided to make an app that could help a beginner get some insight into the public's mood online before investing; introducing -- Money Bird. Money Bird provides sentiment analysis of the most popular tweets related to a particular company. It also gives a company's average sentiment score (using an AFINN model) based on the most relevant recent tweets. Money Bird is still in the pre-alpha development stage but works satisfactorily well for NASDAQ and NYSE stocks. Feel free to contribute and give your insights on our project.

**Check out our app (Limited frontend):** [App's deployment link](https://money-bird-39e83.web.app/)

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

1. **Creating config file in the app folder of the repository** **

    Create a file named `config.py` in the app folder of the repository. This file will contain your API credentials. Your API credentials should remain secret.

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

## Future Works / TODOs

- Use our own custom sentiment analyser which is more accustomed to the financial lingo and technical jargons.
- More UI optimisations
- Better visuals and smooth animations for better UX.
- Implemnt dark mode.
- Report button in case the tweet is not relevant to the user.
- Include all major Exchanges. For now we are only working with NYSE and NASDAQ.
- Add more metrics for sorting the tweets according to relevance.

