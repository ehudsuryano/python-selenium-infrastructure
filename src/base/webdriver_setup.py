from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverSetup:
    @staticmethod
    def get_driver(browser="chrome"):
        browser = browser.lower()
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif browser == "safari":
            driver = webdriver.Safari()  # Safari WebDriver comes pre-installed on macOS
        else:
            raise ValueError(f"Browser '{browser}' is not supported.")
        driver.maximize_window()
        return driver
