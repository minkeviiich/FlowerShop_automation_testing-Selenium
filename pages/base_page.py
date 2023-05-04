from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from configuration import CAPTURE_PATH


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, timeout=10)

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_not_visible(self, locator):
        return ActionChains(self.driver).move_to_element(locator).perform()

    def send_text(self, locator, value):
        self.wait.until(ec.element_to_be_clickable(locator)).send_keys(value)

    def click_element(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator)).text

    def check_sort(self, array):
        return all([x >= y for x, y in zip(array, array[1:])])

