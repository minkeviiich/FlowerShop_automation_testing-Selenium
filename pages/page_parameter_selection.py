import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
import allure


class FormPageParametrSelection(BasePage):

    @allure.step('Parameter selection')
    def parameter_selection(self):
        with allure.step('Setting the minimum and maximum values'):
            self.element_is_visible(Locators.PRICE_MIN).send_keys('60')
            self.element_is_visible(Locators.PRICE_MAX).send_keys('130')
        with allure.step('Click "PRICE ENTER"'):
            self.element_is_visible(Locators.PRICE_ENTER).click()

    @allure.step('Fields catalog flowers')
    def fields_catalog_flowers(self):
        with allure.step('Searching for the "flowers catalog" button'):
            button = self.element_is_visible(Locators.FLOWERS_CATALOG)
            self.element_is_not_visible(button)
        with allure.step('Click "flowers catalog" button'):
            self.element_is_visible(Locators.FLOWERS_CATALOG_CLICK).click()

    @allure.step('Fields catalog flowers all')
    def catalog_flowers_all(self):
        self.element_is_visible(Locators.ALL_FLOWERS).click()
