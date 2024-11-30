from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utilities.logger import get_logger
logger = get_logger()


class BaseHandler:
    def __init__(self, driver):
        self.driver = driver
