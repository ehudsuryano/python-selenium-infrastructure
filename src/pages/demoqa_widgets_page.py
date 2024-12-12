from selenium.webdriver.common.by import By
from ..handlers import demohqSideMenuItem_Handler
from ..handlers import textbox_handler
from ..handlers import button_handler
from src.utilities.logger import get_logger
from src.base.base_page import BasePage  # Import the BasePage class

logger = get_logger()


class DemoqaWidgetsPage(BasePage):  # Inherit from BasePage
    URL = "https://demoqa.com/elements"

    def __init__(self, driver):
        super().__init__(driver)  # Initialize the BasePage with the driver

    def load(self):
        """
        Navigates to the specific page URL.
        """
        self.driver.get(self.URL)  # Use the URL attribute

    def click_side_menu_item(self, driver, item_name):
        try:

            demohqSideMenuItem_Handler.SideMenuItemHandler.on_get_elements(driver, item_name)[0].click()
            logger.info(f"side menu item{item_name}  was clicked")
        except Exception("element not found"):
            logger.error(f"side menu item{item_name} was NOT clicked")
        return

