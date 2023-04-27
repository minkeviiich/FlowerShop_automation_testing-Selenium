import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageParametrSelection(BasePage):

    def parameter_selection(self):
        self.element_is_visible(Locators.PRICE_MIN).send_keys('60')
        self.element_is_visible(Locators.PRICE_MAX).send_keys('130')
        self.element_is_visible(Locators.PRICE_ENTER).click()

    def fields_catalog_flowers(self):
        button = self.element_is_visible(Locators.FLOWERS_CATALOG)
        self.element_is_not_visible(button)
        self.element_is_visible(Locators.FLOWERS_CATALOG_CLICK).click()

    def catalog_flowers_all(self):
        self.element_is_visible(Locators.ALL_FLOWERS).click()
