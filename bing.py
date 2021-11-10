from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver import Chrome, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import platform
import time

search_array = [
    "apple", "microsoft", "google", "amazon", "facebook", "netflix", "salesforce", "nvidia", "volkswagen", "tesla", 
    "Canadian news", "Top stories", "Canada", "World", "Entertainment", "Sci/Tech", "Business", "Politics", "Sports", "Lifestyle",
    "stock", "ubuntu", "system76", "raspberry pi", "arduino", "sony", "nikon", "logitech", "hello world", "Hong Kong"
]
SEARCH_BAR_ELEMENT_ID = "sb_form_q"


def search(driver, key):
    print("Seaching " + key + "...")
    search_bar = driver.find_element(By.ID, SEARCH_BAR_ELEMENT_ID)
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
    if platform.system() == "Linux":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_experimental_option("detach", True) # Keep browser open after the program finishes running
        chrome_service = ChromeService("./chromedriver")
        browser = Chrome(service=chrome_service, options=chrome_options)
        browser.get("https://www.bing.com/")
    elif platform.system() == "Windows":
        print("Reading profile path")
        file = open("PROFILE_PATH", "r")
        user_data_dir = file.readline()
        profile_directory = file.readline()
        file.close()
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        # edge_options.add_argument("-inprivate")
        edge_options.add_argument("user-data-dir=" + user_data_dir)
        edge_options.add_argument("profile-directory=" + profile_directory)
        edge_options.add_experimental_option("detach", True) # Keep browser open after the program finishes running
        edge_service = EdgeService("msedgedriver.exe")
        browser = Edge(service=edge_service, options=edge_options)
        browser.get("https://account.microsoft.com/rewards/")
    else:
        return

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
