from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep

search_array = [
    "apple", "macbook pro", "dell", "ubuntu", "raspberry pi", "system76", "microsoft", "logitech", "bestbuy", "amazon"
    "Canadian news", "Top stories", "Canada", "World", "Entertainment", "Sci/Tech", "Business", "Politics", "Sports", "Lifestyle",
    "stock", "indeed", "sony", "part time job", "stock market", "hello world", "microsoft", "google", "travel", "volkswagen"
]


def search(driver, key):
    print("Seaching " + key + "...")
    search_bar = driver.find_element_by_id("sb_form_q")
    search_bar.send_keys(key)
    sleep(1)
    search_bar.send_keys(Keys.ENTER)
    sleep(2)


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
    else:
        print()


if __name__ == "__main__":
    main()
