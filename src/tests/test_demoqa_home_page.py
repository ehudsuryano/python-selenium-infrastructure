import time

import pytest
import allure
from src.pages.demoqa_home_page import DemoqaHomePage
from src.pages.demoqa_elements_page import DemoqaElementsPage
from src.base.webdriver_setup import WebDriverSetup
from src.utilities.logger import get_logger
from src.utilities.screenshot_util import capture_screenshot  # Import the screenshot utility

logger = get_logger()


@pytest.fixture
def driver():
    driver = WebDriverSetup.get_driver("chrome")
    yield driver
    driver.quit()


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


@pytest.fixture
def driver():
    driver = WebDriverSetup.get_driver("chrome")
    yield driver
    driver.quit()


def test_reach_elements_page(driver):
    logger.info("Starting test for Home Page")
    home_page = DemoqaHomePage(driver)
    home_page.load()
    logger.info("Loaded Home Page")
    home_page.click_elements(driver)
    logger.info("Loaded Elements Page")
    elements_page = DemoqaElementsPage(driver)
    elements_page.click_side_menu_item(driver, "Text Box")
    elements_page.type_text(driver, "userName", "Ehud Suryano")
    time.sleep(3)
    try:
        assert "https://demoqa.com/text-box" in elements_page.get_url(), "Page title mismatch"
        logger.info("Test passed")
    except AssertionError as e:
        # Capture screenshot on failure
        capture_screenshot(driver, "failure-home-page")
        logger.error("Test failed, screenshot captured")
        raise
