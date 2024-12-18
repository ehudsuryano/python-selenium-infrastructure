from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverSetup:
    @staticmethod
    def get_driver(browser="chrome"):
        browser = browser.lower()

        if browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--force-device-scale-factor=0.50")
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )

        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.set_preference("layout.css.devPixelsPerPx", "0.25")
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=firefox_options
            )

        elif browser == "edge":
            edge_options = EdgeOptions()
            edge_options.add_argument("--force-device-scale-factor=0.25")
            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=edge_options
            )

        elif browser == "safari":
            driver = webdriver.Safari()  # Safari does not have an explicit zoom setting

        else:
            raise ValueError(f"Browser '{browser}' is not supported.")

        driver.maximize_window()
        return driver
