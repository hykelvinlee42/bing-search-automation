import time
import argparse
import platform
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers.elements as Elements
import helpers.browsers as BrowserHelpers
from helpers.decrypt import get_passcode

search_array = []


def load_search_array(filename="./search_keys"):
    global search_array
    file = open(filename, "r")
    search_array = [line.strip() for line in file.readlines()]
    file.close()


def login(driver, acc):
    driver.get("https://www.bing.com/news/")
    time.sleep(2)

    login_form = driver.find_element(By.NAME, Elements.LOGIN_BTN_ELEMENT_NAME)
    login_form.click()

    email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, Elements.LOGIN_BAR_ELEMENT_NAME)))
    if not acc:
        acc = input("Account: ")

    email_input.send_keys(acc)
    email_input.send_keys(Keys.ENTER)

    password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, Elements.LOGIN_PASSWORD_INPUT_ELEMENT_NAME)))
    password_input.send_keys(get_passcode())

    for _i in range(2): # repeat one more time for confirming stay login
        time.sleep(1)
        submit_btn = driver.find_element(By.ID, Elements.LOGIN_SUBMIT_BTN_ELEMENT_ID)
        submit_btn.submit()
    
    WebDriverWait(driver, 10).until(EC.title_contains("Bing News"))
    return True


def search(driver, key):
    print("Seaching " + key + "...")
    search_bar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, Elements.SEARCH_BAR_ELEMENT_ID)))
    search_bar.send_keys(key)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(3)


def open_tabs_for_search(driver):
    for index, key in enumerate(search_array):
        tab_name = "tab" + str(index)
        window_cmd = "window.open('about:blank', '{0}')".format(tab_name)

        driver.execute_script(window_cmd)
        driver.switch_to.window(tab_name)
        driver.get("https://www.bing.com/news/")

        search(driver, key)


def usages():
    parser = argparse.ArgumentParser(description="Automation script to complete Microsoft Rewards - Bing search daily challenge")
    parser.add_argument('-u', nargs=1, help="prefill username for auto login")
    parser.add_argument("--headless", action=argparse.BooleanOptionalAction, help="toggle to run chrome in headless mode")
    args = parser.parse_args()
    return vars(args)


def main():
    args = usages()

    load_search_array()
    is_login = False
    start_time = time.time()

    if platform.system() == "Linux": 
        browser = BrowserHelpers.get_unix_chrome(is_headless=args["headless"])
        is_login = login(browser, args["u"])
    elif platform.system() == "Darwin":
        browser = BrowserHelpers.get_unix_chrome(is_headless=args["headless"])
        is_login = login(browser, args["u"]) 
    elif platform.system() == "Windows":
        browser = BrowserHelpers.get_wins_edge()
        is_login = True
    
    if not args["headless"]:
        browser.get("https://account.microsoft.com/rewards/")

    if is_login:
        open_tabs_for_search(browser)
        elapsed_time = time.time() - start_time
        print("Search Completed in " + str(elapsed_time) + "s. Script ends.")
        print("Script ran on {0}".format(date.today().isoformat()))
    else:
        print("Script ends.")


if __name__ == "__main__":
    main()
