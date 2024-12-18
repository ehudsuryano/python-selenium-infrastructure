from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.logger import get_logger
from src.base.base_handler import BaseHandler
logger = get_logger()


class DropdownHandler(BaseHandler):
    def on_get_elements(driver, dropmenu, timeout=10):
        """
        Wait for and return all web elements matching the query.

        :param driver: WebDriver instance
        :param dropmenu: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10 seconds)
        :return: List of WebElements found using the constructed XPath, or an empty list if none are found
        """
        xpath = (
            f"//div[@name='{dropmenu}' or @title='{dropmenu}' or @id='{dropmenu}']|" +
            f"//select[@name='{dropmenu}' or @title='{dropmenu}' or @id='{dropmenu}']|" +
            f"//input[@name='{dropmenu}' or @title='{dropmenu}' or @id='{dropmenu}']|" +
            f"//div[@class='{dropmenu}']"
        )

        logger.debug(f"Constructed XPath: {xpath}")

        try:
            # Wait until at least one element matching the XPath is present
            wait = WebDriverWait(driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            logger.debug(f"Found {len(elements)} elements matching query '{dropmenu}'.")
            return elements
        except TimeoutException:
            logger.error(f"No elements matching query '{dropmenu}' found within {timeout} seconds.")
            return []
