from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    Base class for all page objects. Contains shared methods and utilities.
    """

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """
        Navigates the WebDriver to the given URL.
        This method should be overridden in child classes.
        """
        raise NotImplementedError("The 'load' method must be overridden in the child class.")

    def get_title(self):
        """
        Returns the title of the current page.
        """
        return self.driver.title

    def get_url(self):
        """
        Returns the current URL of the browser.
        """
        return self.driver.current_url

    def scroll_to_element(self, driver, element_name):
        element = driver.find_element(By.XPATH, f"//*[text()='{element_name}']")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return driver

    def is_element_exist(self, driver, element_name):
        try:
            driver.find_element(By.ID, element_name)
            return True
        except :
            return False
