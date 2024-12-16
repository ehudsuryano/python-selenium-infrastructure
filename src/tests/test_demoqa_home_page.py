import time

import pytest
import allure
from src.pages.demoqa_home_page import DemoqaHomePage
from src.pages.demoqa_elements_page import DemoqaElementsPage
from src.base.webdriver_setup import WebDriverSetup
from src.utilities.logger import get_logger
from src.utilities.screenshot_util import capture_screenshot  # Import the screenshot utility
from src.pages.demoqa_widgets_page import DemoqaWidgetsPage
logger = get_logger()


@pytest.fixture
def driver():
    driver = WebDriverSetup.get_driver("chrome")
    yield driver
    driver.quit()


#@pytest.mark.skip
def test_home_page(driver):
    logger.info("Starting test for Home Page")
    home_page = DemoqaHomePage(driver)
    home_page.load()
    logger.info("Loaded Home Page")

    try:
        assert "DEMOQA" in home_page.get_title(), "Page title mismatch"
        logger.info("Test passed")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise


#@pytest.mark.skip
def test_reach_elements_page(driver):
    logger.info("Starting test for Elements Page")
    home_page = DemoqaHomePage(driver)
    home_page.load()
    logger.info("Loaded Home Page")
    home_page.click_elements(driver)
    logger.info("Loaded Elements Page")
    elements_page = DemoqaElementsPage(driver)
    elements_page.click_side_menu_item(driver, "Text Box")
    elements_page.type_text(driver, "userName", "Ehud Suryano")
    elements_page.type_text(driver, "userEmail", "ehud@gmail.com")
    elements_page.type_text(driver, "currentAddress", "rishon lezion")
    elements_page.type_text(driver, "permanentAddress", "Rishon Lezion")
    elements_page.scroll_to_element(driver,"Submit")
    elements_page.click_button(driver, "Submit")
    time.sleep(3)
    try:
        assert "https://demoqa.com/text-box" in elements_page.get_url(), "Page title mismatch"
        logger.info("Test passed")
        assert elements_page.is_element_exist(driver, "output") is True
        logger.info("output exists")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise


def test_reach_widgets_page(driver):
    logger.info("Starting test for Widgets Page")
    home_page = DemoqaHomePage(driver)
    home_page.load()
    logger.info("Loaded Home Page")
    home_page.click_widgets(driver)
    logger.info("Loaded Widgets Page")
    widgets_page = DemoqaWidgetsPage(driver)
    widgets_page.scroll_to_element(driver, "Select Menu")
    widgets_page.click_side_menu_item(driver, "Select Menu")
    time.sleep(3)
    try:
        assert "https://demoqa.com/select-menu" in widgets_page.get_url(), "Page title mismatch"
        logger.info("Test passed")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise