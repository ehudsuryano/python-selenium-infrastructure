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
