import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
import allure


class FormPageCart(BasePage):

    @allure.step('Fields Cart')
    def fields_cart(self):
        with allure.step('Searching for the "flowers" button'):
            button = self.element_is_visible(Locators.FLOWERS)
            self.element_is_not_visible(button)
        with allure.step('Click "flowers" button'):
            self.element_is_visible(Locators.FLOWERS_CLICK).click()

    @allure.step('Fields Cart result')
    def result_cart(self):
        result = self.element_is_visible(Locators.BASKET_TEXT)
        result = result.text
        return result

    @allure.step('Fields Cart several')
    def fields_cart_several(self):
        with allure.step('Searching for the "flowers" button'):
            button = self.element_is_visible(Locators.FLOWERS_TWO)
            self.element_is_not_visible(button)
        with allure.step('Multiple selection'):
            self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
            self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        with allure.step('Click "flowers" button'):
            self.element_is_visible(Locators.FLOWERS_CLICK_SEVERAL).click()

    @allure.step('Fields Cart several TWO')
    def fields_cart_several_two(self):
        with allure.step('Searching for the "flowers" button'):
            button = self.element_is_visible(Locators.FLOWERS_TWO)
            self.element_is_not_visible(button)
        with allure.step('Multiple selection'):
            self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
            self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
            self.element_is_visible(Locators.FLOWERS_SEVERAL_CLICK).click()
        with allure.step('Click "flowers" button'):
            self.element_is_visible(Locators.FLOWERS_CLICK_SEVERAL).click()

    @allure.step('Fields Cart several')
    def result_cart_several(self):
        result = self.element_is_visible(Locators.BASKET_TEXT_NUMBER)
        result = result.text
        return result
