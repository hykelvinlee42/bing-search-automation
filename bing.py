from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform
import time
from datetime import date
from helpers.decrypt import get_passcode
import helpers.browsers as BrowserHelpers

search_array = []
LOGIN_BAR_ELEMENT_NAME = "loginfmt"
LOGIN_PASSWORD_INPUT_ELEMENT_NAME = "passwd"
SEARCH_BAR_ELEMENT_ID = "sb_form_q"


def load_search_array(filename="./search_keys"):
    global search_array
    file = open(filename, "r")
    search_array = [line.strip() for line in file.readlines()]
    file.close()


def login(driver):
    driver.get("https://login.live.com/")

    email_input = driver.find_element(By.NAME, LOGIN_BAR_ELEMENT_NAME)
    email_input.send_keys(input("Account: "))
    email_input.send_keys(Keys.ENTER)

    time.sleep(2)
    password_input = driver.find_element(By.NAME, LOGIN_PASSWORD_INPUT_ELEMENT_NAME)
    password_input.send_keys(get_passcode())

    for _i in range(2): # repeat one more time for confirming stay login
        time.sleep(1)
        submit_btn = driver.find_element(By.ID, "idSIButton9")
        submit_btn.submit()

    driver.get("https://account.microsoft.com/rewards/") # redirect to microsoft rewards
    return True


def search(driver, key):
    print("Seaching " + key + "...")
    search_bar = driver.find_element(By.ID, SEARCH_BAR_ELEMENT_ID)
    search_bar.send_keys(key)
    time.sleep(2)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(4)


def open_tabs_for_search(driver):
    for index, key in enumerate(search_array):
        tab_name = "tab" + str(index)
        window_cmd = "window.open('about:blank', " + "'" + tab_name + "')"

        driver.execute_script(window_cmd)
        driver.switch_to.window(tab_name)
        driver.get("https://www.bing.com/news/")

        search(driver, key)


def main():
    load_search_array()
    is_login = False
    start_time = time.time()
    if platform.system() == "Linux": 
        browser = BrowserHelpers.get_linux_chrome()
        browser.get("https://www.bing.com/")
        is_login = login(browser)
    elif platform.system() == "Windows":
        browser = BrowserHelpers.get_wins_edge()
        browser.get("https://account.microsoft.com/rewards/")
        is_login = True
    else:
        return

    if is_login:
        open_tabs_for_search(browser)
        elapsed_time = time.time() - start_time
        print("Search Completed in " + str(elapsed_time) + "s. Script ends.")
        print("Script ran on {0}".format(date.today().isoformat()))
    else:
        print("Script ends.")


if __name__ == "__main__":
    main()
