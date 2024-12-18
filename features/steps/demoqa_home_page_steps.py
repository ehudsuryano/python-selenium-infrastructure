from behave import given, when, then
from src.base.webdriver_setup import WebDriverSetup
from src.pages.demoqa_home_page import DemoqaHomePage


@given('a')
def open_browser(context):
    context.driver = WebDriverSetup.get_driver("chrome")
    context.driver.implicitly_wait(10)


@when('b')
def navigate_home(context):
    context.home_page = DemoqaHomePage(context.driver)
    context.home_page.load()


@then('c')
def verify_title(context, title):
    assert title in context.home_page.get_title(), "Page title mismatch"
    context.driver.quit()
