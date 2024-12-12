from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.logger import get_logger
from src.base.base_handler import BaseHandler
logger = get_logger()


class ButtonHandler(BaseHandler):
    def on_get_elements(driver, btn, timeout=10):
        """
        Wait for and return all web elements matching the query.

        :param driver: WebDriver instance
        :param btn: String to locate elements (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the elements (default is 10 seconds)
        :return: List of WebElements found using the constructed XPath, or an empty list if none are found
        """
        xpath = (f"//button[@type='button' and @id='submit']|" +
                 f"//button[@type='submit' and @role='button' and @value='{btn}']|" +
                 f"//button[@type='submit' and @role='button' and @value='{btn}']|" +
                 f"//button[@id='submit']"
                 )

        logger.debug(f"Constructed XPath: {xpath}")
        try:
            # Wait until at least one element matching the XPath is present
            wait = WebDriverWait(driver, timeout)
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
            logger.debug(f"Found {len(elements)} elements matching query '{btn}'.")
            return elements
        except TimeoutException:
            logger.error(f"No elements matching query '{btn}' found within {timeout} seconds.")
            return []
