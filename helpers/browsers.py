from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver import Chrome, Edge

def get_linux_chrome(driver="./chromedriver"):
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True) # Keep browser open after the program finishes running

    chrome_service = ChromeService(driver)
    return Chrome(service=chrome_service, options=chrome_options)


def get_wins_edge(driver="msedgedriver.exe", profile_path_files="./PROFILE_PATH"):
    print("Reading profile path")
    file = open(profile_path_files, "r")
    user_data_dir = file.readline()
    profile_directory = file.readline()
    file.close()

    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=" + user_data_dir)
    edge_options.add_argument("profile-directory=" + profile_directory)
    edge_options.add_experimental_option("detach", True) # Keep browser open after the program finishes running

    edge_service = EdgeService(driver)
    return Edge(service=edge_service, options=edge_options)
