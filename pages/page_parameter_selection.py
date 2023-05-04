import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
import allure


class FormPageParametrSelection(BasePage):

    @allure.step('Parameter selection')
    def parameter_selection(self):
        with allure.step('Setting the minimum and maximum values'):
            self.send_text(Locators.PRICE_MIN, '60')
            self.send_text(Locators.PRICE_MAX, '130')
        with allure.step('Click "PRICE ENTER"'):
            self.click_element(Locators.PRICE_ENTER)

    @allure.step('Fields catalog flowers')
    def fields_catalog_flowers(self):
        with allure.step('Searching for the "flowers catalog" button'):
            button = self.element_is_visible(Locators.FLOWERS_CATALOG)
            self.element_is_not_visible(button)
        with allure.step('Click "flowers catalog" button'):
            self.click_element(Locators.FLOWERS_CATALOG_CLICK)

    @allure.step('Fields catalog flowers all')
    def catalog_flowers_all(self):
        self.click_element(Locators.ALL_FLOWERS)
