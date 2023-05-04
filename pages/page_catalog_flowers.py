import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
import allure


class FormPageFlowers(BasePage):

    @allure.step('Fields catalog flowers')
    def fields_catalog_flowers(self):
        with allure.step('Searching for the "flowers catalog" button'):
            button = self.element_is_visible(Locators.FLOWERS_CATALOG)
            self.element_is_not_visible(button)
        with allure.step('Click "flowers catalog" button'):
            self.click_element(Locators.FLOWERS_CATALOG_CLICK)

    @allure.step('Click catalog flowers all')
    def catalog_flowers_all(self):
        self.click_element(Locators.ALL_FLOWERS)

    @allure.step('Click catalog flowers gladiolus')
    def catalog_flowers_gladiolus(self):
        self.click_element(Locators.FLOWERS_GLADIOLUS)

    @allure.step('Click catalog flowers alstromeria')
    def catalog_flowers_alstromeria(self):
        self.click_element(Locators.FLOWERS_ALSTROMERIA)

    @allure.step('Click catalog flowers gvozdika')
    def catalog_flowers_gvozdika(self):
        self.click_element(Locators.FLOWERS_GVOZDIKA)

    @allure.step('Click catalog flowers hypsophila')
    def catalog_flowers_hypsophila(self):
        self.click_element(Locators.FLOWERS_HYPSOPHILA)

    @allure.step('Click catalog flowers gortenzy')
    def catalog_flowers_gortenzy(self):
        self.click_element(Locators.FLOWERS_GORTENZY)

    @allure.step('Click catalog flowers redrose')
    def catalog_flowers_redrose(self):
        self.click_element(Locators.FLOWERS_REDROSE)

    @allure.step('Click catalog flowers customrose')
    def catalog_flowers_customrose(self):
        self.click_element(Locators.FLOWERS_CUSTOMROSE)

    @allure.step('Click catalog flowers lilya')
    def catalog_flowers_lilya(self):
        self.click_element(Locators.FLOWERS_LILYA)

    @allure.step('Click catalog flowers orkhideya')
    def catalog_flowers_orkhideya(self):
        self.click_element(Locators.FLOWERS_ORKHIDEYA)

    @allure.step('Click catalog flowers pion')
    def catalog_flowers_pion(self):
        self.click_element(Locators.FLOWERS_PION)

    @allure.step('Click catalog flowers podsoln')
    def catalog_flowers_podsoln(self):
        self.click_element(Locators.FLOWERS_PODSOLN)

    @allure.step('Click catalog flowers rose')
    def catalog_flowers_rose(self):
        self.click_element(Locators.FLOWERS_ROSE)

    @allure.step('Click catalog flowers romashki')
    def catalog_flowers_romashki(self):
        self.click_element(Locators.FLOWERS_ROMASHKI)

    @allure.step('Click catalog flowers tulpan')
    def catalog_flowers_tulpan(self):
        self.click_element(Locators.FLOWERS_TULPAN)

    @allure.step('Click catalog flowers exotic')
    def catalog_flowers_exotic(self):
        self.click_element(Locators.FLOWERS_EXOTIC)
