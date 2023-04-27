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

    def fields_cart_several(self):
        button = self.element_is_visible(Locators.FLOWERS_TWO)
        self.element_is_not_visible(button)
        self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        self.element_is_visible(Locators.FLOWERS_CLICK_SEVERAL).click()

    def fields_cart_several_two(self):
        button = self.element_is_visible(Locators.FLOWERS_TWO)
        self.element_is_not_visible(button)
        self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        self.element_is_visible(Locators.FLOWERS_CLICK_SEVERAL).click()

    def result_cart_several(self):
        result = self.element_is_visible(Locators.BASKET_TEXT_NUMBER)
        result = result.text
        return result
