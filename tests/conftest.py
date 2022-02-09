from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    options = Options()
    # Uncomment the following if testing on GitHub actions, the browser needs to run in headless mode
    # options.add_argument('--disable-gpu')
    # options.add_argument('--headless')
    return options
