from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextboxHandler:
    def on_get_element(driver, query, timeout=10):
        """
        Wait for and return a web element based on the query.

        :param driver: WebDriver instance
        :param query: String to locate the element (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the element (default is 10 seconds)
        :return: WebElement found using the constructed XPath
        """
        # Construct the XPath to find the textbox element with the specified query
        xpath = (
            f"//textarea[@name='{query}' or @title='{query}' or @id='{query}']|"
            f"//input[@name='{query}' and (@type='text' or @type='password')]|"
            f"//input[@title='{query}' and (@type='text' or @type='password')]|"
            f"//input[@id='{query}' and (@type='text' or @type='password' or @type='email')]"
        )

        # Wait until the element is found and return it
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
