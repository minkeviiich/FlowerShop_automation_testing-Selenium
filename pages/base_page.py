from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from configuration import CAPTURE_PATH


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_not_visible(self, locator):
        return ActionChains(self.driver).move_to_element(locator).perform()

    def check_sort(self, array):
        return all([x >= y for x, y in zip(array, array[1:])])
