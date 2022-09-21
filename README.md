# bing-search-automation
This Python (3.8) automation tool uses Selenium for completing the Microsoft Rewards daily challenge.

## Getting Started
### Prerequisites

Download the right version browser driver for your [chrome browser](https://sites.google.com/a/chromium.org/chromedriver/home) or [edge browser](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).  

Then install the Selenium and other required libraries,

```
pip install selenium==4.0.0
pip install rsa==4.9
```

#### Creating Essential search_key File
Create a `search_key` file which contains all the keywords (separated by newline) you want to search.

#### Creating and Encrypt Login Credential File
```
python helpers/encrypt_pw.py
```
Running the command above will ask for the login passcode you want to encrypt and then generate two files, `passcode` and `private_key`. These two files are used in `bing.py` for auto login.

### Windows Edge Specific Instructions
#### Creating Essential PROFILE_PATH File

Create an empty text file and name it as `PROFILE_PATH` (without extension name).  

![profile_path](./screenshots/path.png)

Copy and paste profile path to the `PROFILE_PATH` file. Then separate the profile path in two lines. `C:\Users\uname\AppData\Local\Microsoft\Edge\User Data\` prefix on the first line and whatever comes after on the second line as shown in the screenshot above.

### Running
#### General
```
python bing.py
```

#### Windows Edge
```
run.bat
```
or double clicking the `run.bat` batch file

## Script Options
```
usage: bing.py [-h] [-u U] [--headless | --no-headless]

Automation script to complete Microsoft Rewards - Bing search daily challenge

options:
  -h, --help            show this help message and exit
  -u U                  prefill username for auto login
  --headless, --no-headless
                        toggle to run chrome in headless mode
```
