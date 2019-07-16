from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

search_array = [
    "apple", "macbook pro", "dell", "ubuntu", "raspberry pi", "system76", "microsoft", "google", "bestbuy", "amazon",
    "Canadian news", "Top stories", "Canada", "World", "Entertainment", "Sci/Tech", "Business", "Politics", "Sports", "Lifestyle",
    "stock", "indeed", "sony", "part time job", "stock market", "hello world", "nikon", "logitech", "travel", "volkswagen"
]


def search(driver, key):
    print("Seaching " + key + "...")
    search_bar = driver.find_element_by_id("sb_form_q")
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
    browser = Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
    browser.get("https://www.bing.com/")

    # Wait for manual login
    print("Login? (y/n)")
    cmd = raw_input()
    if cmd == "y" or cmd == "Y":
        open_tabs(browser)
        elapsed_time = time.time() - start_time
        print("Search Completed in " + str(elapsed_time) + "s. Script ends.")
    else:
        print("Script ends.")


if __name__ == "__main__":
    main()
