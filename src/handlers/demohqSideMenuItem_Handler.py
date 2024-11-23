from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideMenuItemHandler:
    def on_get_element(driver, itemName, timeout=10):
        """
        Wait for and return a web element based on the query.

        :param driver: WebDriver instance
        :param query: String to locate the element (e.g., name, title, or id)
        :param timeout: Maximum time to wait for the element (default is 10 seconds)
        :return: WebElement found using the constructed XPath
        """
        # Construct the XPath to find the textbox element with the specified query
        xpath = (
            f"//*[text()='{itemName}']"
        )

        # Wait until the element is found and return it
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
