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
            self.click_element(Locators.FLOWERS_CLICK)

    @allure.step('Fields Cart several')
    def fields_cart_several(self):
        with allure.step('Searching for the "flowers" button'):
            button = self.element_is_visible(Locators.FLOWERS_TWO)
            self.element_is_not_visible(button)
        with allure.step('Multiple selection'):
            self.click_element(Locators.FLOWERS_SEVERAL_CLICK)
            self.click_element(Locators.FLOWERS_SEVERAL_CLICK)
        with allure.step('Click "flowers" button'):
            self.click_element(Locators.FLOWERS_CLICK_SEVERAL)

    @allure.step('Fields Cart several TWO')
    def fields_cart_several_two(self):
        with allure.step('Searching for the "flowers" button'):
            button = self.element_is_visible(Locators.FLOWERS_TWO)
            self.element_is_not_visible(button)
        with allure.step('Multiple selection'):
            self.click_element(Locators.FLOWERS_SEVERAL_CLICK)
            self.click_element(Locators.FLOWERS_SEVERAL_CLICK)
            self.click_element(Locators.FLOWERS_SEVERAL_CLICK)
        with allure.step('Click "flowers" button'):
            self.click_element(Locators.FLOWERS_CLICK_SEVERAL)
