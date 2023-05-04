import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
import allure


class FormPageSorting(BasePage):

    @allure.step('Sorting by price')
    def sorting(self):
        with allure.step('Click the "ALL FLOWERS" button'):
            self.click_element(Locators.ALL_FLOWERS)
        with allure.step('Click the "Sort by price" button'):
            self.click_element(Locators.SORTING_CLICK)

    @allure.step('Sorting by popular')
    def sorting_popular(self):
        with allure.step('Click the "ALL FLOWERS" button'):
            self.click_element(Locators.ALL_FLOWERS)
        with allure.step('Click the "Sort by Popular" button'):
            self.click_element(Locators.POPULAR_CLICK)
