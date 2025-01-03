from selenium.webdriver.common.by import By
from ..handlers import card_handler
from src.utilities.logger import get_logger
from src.base.base_page import BasePage  # Import the BasePage class

logger = get_logger()


class DemoqaHomePage(BasePage):  # Inherit from BasePage
    URL = "https://demoqa.com"

    def __init__(self, driver):
        super().__init__(driver)  # Initialize the BasePage with the driver

    def load(self):
        """
        Navigates to the specific page URL.
        """
        self.driver.get(self.URL)  # Use the URL attribute

    def click_elements(self, driver):
        try:

            element = card_handler.CardHandler.on_get_elements(driver, "Elements")[0]
            self.scroll_to_element(driver,element)
            element.click()
            logger.info("Elements card was clicked")
        except Exception("element not found"):
            logger.error("Elements card was NOT clicked")
        return

    def click_widgets(self, driver):
        try:
            element = card_handler.CardHandler.on_get_elements(driver, "Widgets")[0]
            self.scroll_to_element(driver,element)
            element.click()
            logger.info("Widgets card was clicked")
        except Exception("element not found"):
            logger.error("Widgets card was NOT clicked")
        return

    def scroll_to_element(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return driver
