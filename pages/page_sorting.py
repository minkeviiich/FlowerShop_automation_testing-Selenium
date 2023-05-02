import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
import allure


class FormPageSorting(BasePage):

    @allure.step('Sorting by price')
    def sorting(self):
        with allure.step('Click the "ALL FLOWERS" button'):
            self.element_is_visible(Locators.ALL_FLOWERS).click()
        with allure.step('Click the "Sort by price" button'):
            self.element_is_visible(Locators.SORTING_CLICK).click()
