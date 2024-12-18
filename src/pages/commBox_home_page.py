from selenium.webdriver.common.by import By
from src.utilities.logger import get_logger
from src.base.base_page import BasePage  # Import the BasePage class
from ..handlers import button_handler
from ..handlers import textbox_handler
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


logger = get_logger()


class CommBoxPage(BasePage):  # Inherit from BasePage
    URL = "https://www.commbox.io/"

    def __init__(self, driver):
        super().__init__(driver)  # Initialize the BasePage with the driver

    def load(self):
        """
        Navigates to the specific page URL.
        """
        self.driver.get(self.URL)  # Use the URL attribute

    def move_body(self, driver):
        script = """
        const evt = new MouseEvent('mousemove', {
            bubbles: true,
            cancelable: true,
            view: window,
            clientX: 200, // X-coordinate
            clientY: 100  // Y-coordinate
        });
        document.body.dispatchEvent(evt);
        """
        driver.execute_script(script)

    def click_chat_btn(self, driver, btn_name):
        try:
            button_handler.ButtonHandler.on_get_elements(driver, btn_name)[0].click()
            logger.info(f"side menu item{btn_name}  was clicked")
        except Exception("element not found"):
            logger.error(f"side menu item{btn_name} was NOT clicked")
        return

    def click_start_new_chat(self,driver):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='welcomeStartConversationCTA pointer']//button[@id='startChat']")))
        element.click()

    def switch_to_chat(self,driver):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located(
            (By.ID, "ifrChat")))
        driver.switch_to.frame(element)

    def type_text_in_chat(self, driver, texttotypy):
        try:
            textbox_handler.TextboxHandler.on_get_elements(driver, "txtMessage")[0].send_keys(texttotypy)
            logger.info(f"{texttotypy} was typed into textarea")
        except Exception("element not found"):
            logger.error(f"{texttotypy} was NOT typed into textarea")