import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageCart(BasePage):

    def fields_cart(self):
        button = self.element_is_visible(Locators.FLOWERS)
        self.element_is_not_visible(button)
        self.element_is_visible(Locators.FLOWERS_CLICK).click()

    def result_cart(self):
        result = self.element_is_visible(Locators.BASKET_TEXT)
        result = result.text
        return result
