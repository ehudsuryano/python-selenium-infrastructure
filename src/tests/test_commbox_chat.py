import time
import pytest
import allure
from src.base.webdriver_setup import WebDriverSetup
from src.utilities.logger import get_logger
from src.utilities.screenshot_util import capture_screenshot  # Import the screenshot utility
from src.pages.commBox_home_page import CommBoxPage
logger = get_logger()
import pyautogui



@pytest.fixture
def driver():
    driver = WebDriverSetup.get_driver("chrome")
    yield driver
    driver.quit()

#@pytest.mark.skip
def test_commBox_home_page(driver):
    logger.info("Starting test for CommBox Home Page")
    home_page = CommBoxPage(driver)
    home_page.load()
    logger.info("Loaded Home Page")

    try:
        assert "CommBox" in home_page.get_title(), "Page title mismatch"
        logger.info("Test passed")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise

def test_commbox_chat(driver):
    logger.info("Starting test for chat")
    home_page = CommBoxPage(driver)
    home_page.load()
    logger.info("Loaded Home Page")
    home_page.move_body(driver)  # To get chat button to appear
    time.sleep(3)
    home_page.click_chat_btn(driver, "btnImgPreButton_ifrChat")
    home_page.switch_to_chat(driver)
    home_page.click_start_new_chat(driver)
    home_page.type_text_in_chat(driver, "testing testing testing")
    time.sleep(5)
