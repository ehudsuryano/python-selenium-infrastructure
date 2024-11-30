from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.logger import get_logger
from src.base.base_handler import BaseHandler
logger = get_logger()


class TextboxHandler(BaseHandler):
    def on_get_elements(driver, query, timeout=10):
        """
        Wait for and return all web elements matching the query.

        :param driver: WebDriver instance
        :param query: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10 seconds)
        :return: List of WebElements found using the constructed XPath, or an empty list if none are found
        """
        xpath = (
            f"//textarea[@name='{query}' or @title='{query}' or @id='{query}']|"
            f"//input[@name='{query}' and (@type='text' or @type='password')]|"
            f"//input[@title='{query}' and (@type='text' or @type='password')]|"
            f"//input[@id='{query}' and (@type='text' or @type='password' or @type='email')]"
        )

        logger.debug(f"Constructed XPath: {xpath}")

        try:
            # Wait until at least one element matching the XPath is present
            wait = WebDriverWait(driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            logger.debug(f"Found {len(elements)} elements matching query '{query}'.")
            return elements
        except TimeoutException:
            logger.error(f"No elements matching query '{query}' found within {timeout} seconds.")
            return []
