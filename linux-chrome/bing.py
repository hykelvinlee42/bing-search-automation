from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

search_array = [
    "apple", "microsoft", "google", "amazon", "facebook", "netflix", "nvidia", "amd", "salesforce", "tesla", "volkswagen",
    "Canadian news", "Top stories", "Canada", "World", "Sci/Tech", "Business", "Politics", "Sports",
    "stock", "ubuntu", "system76", "raspberry pi", "arduino", "sony", "nikon", "logitech", "hello world", "Hong Kong"
]
SEARCH_BAR_ELEMENT_ID = "sb_form_q"


def search(driver, key):
    print("Seaching " + key + "...")
    search_bar = driver.find_element_by_id(SEARCH_BAR_ELEMENT_ID)
    search_bar.send_keys(key)
    time.sleep(2)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(4)


def open_tabs(driver):
    i = 0
    for key in search_array:
        tab_name = "tab" + str(i)
        window_cmd = "window.open('about:blank', " + "'" + tab_name + "')"
        driver.execute_script(window_cmd)
        driver.switch_to.window(tab_name)
        driver.get("https://www.bing.com/news/")
        search(driver, key)
        i += 1


def main():
    start_time = time.time()
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    browser = Chrome(executable_path="./chromedriver", options=chrome_options)
    browser.get("https://www.bing.com/")

    # Wait for manual login
    print(" _                 _      ___     __         __  __  ")
    print("| |               (_)    |__ \   / /        / /  \ \ ")
    print("| |     ___   __ _ _ _ __   ) | | |_   _   / / __ | |")
    print("| |    / _ \ / _` | | '_ \ / /  | | | | | / / '_ \| |")
    print("| |___| (_) | (_| | | | | |_|   | | |_| |/ /| | | | |")
    print("|______\___/ \__, |_|_| |_(_)   | |\__, /_/ |_| |_| |")
    print("              __/ |              \_\__/ |        /_/")   
    print("             |___/                 |___/            ")
    print("Login? (y/n)")
    cmd = input()
    if cmd == "y" or cmd == "Y":
        open_tabs(browser)
        elapsed_time = time.time() - start_time
        print("Search Completed in " + str(elapsed_time) + "s. Script ends.")
    else:
        print("Script ends.")


if __name__ == "__main__":
    main()
