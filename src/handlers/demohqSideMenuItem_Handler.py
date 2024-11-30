from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.logger import get_logger
from src.base.base_handler import BaseHandler
logger = get_logger()


class SideMenuItemHandler(BaseHandler):
    def on_get_elements(driver, item_name, timeout=10):
        """
        Wait for and return a web element based on the query.

        :param driver: WebDriver instance
        :param item_name: String to locate the element (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the element (default is 10 seconds)
        :return: WebElement found using the constructed XPath
        """
        # Construct the XPath to find the textbox element with the specified query
        xpath = (
            f"//*[text()='{item_name}']"
        )

        logger.debug(f"Constructed XPath: {xpath}")

        try:
            # Wait until at least one element matching the XPath is present
            wait = WebDriverWait(driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            logger.debug(f"Found {len(elements)} elements matching query '{item_name}'.")
            return elements
        except TimeoutException:
            logger.error(f"No elements matching query '{item_name}' found within {timeout} seconds.")
            return []
