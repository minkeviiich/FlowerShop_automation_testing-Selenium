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
            self.element_is_visible(Locators.FLOWERS_CATALOG_CLICK).click()

    @allure.step('Catalog flowers result')
    def result_catalog_flowers(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers all')
    def catalog_flowers_all(self):
        self.element_is_visible(Locators.ALL_FLOWERS).click()

    @allure.step('Catalog flowers all result')
    def result_catalog_flowers_all(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers gladiolus')
    def catalog_flowers_gladiolus(self):
        self.element_is_visible(Locators.FLOWERS_GLADIOLUS).click()

    @allure.step('Catalog flowers gladiolus result')
    def result_flowers_gladiolus(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers alstromeria')
    def catalog_flowers_alstromeria(self):
        self.element_is_visible(Locators.FLOWERS_ALSTROMERIA).click()

    @allure.step('Catalog flowers alstromeria result')
    def result_flowers_alstromeria(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers gvozdika')
    def catalog_flowers_gvozdika(self):
        self.element_is_visible(Locators.FLOWERS_GVOZDIKA).click()

    @allure.step('Catalog flowers gvozdika result')
    def result_flowers_gvozdika(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers hypsophila')
    def catalog_flowers_hypsophila(self):
        self.element_is_visible(Locators.FLOWERS_HYPSOPHILA).click()

    @allure.step('Catalog flowers hypsophila result')
    def result_flowers_hypsophila(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers gortenzy')
    def catalog_flowers_gortenzy(self):
        self.element_is_visible(Locators.FLOWERS_GORTENZY).click()

    @allure.step('Catalog flowers gortenzy result')
    def result_flowers_gortenzy(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers redrose')
    def catalog_flowers_redrose(self):
        self.element_is_visible(Locators.FLOWERS_REDROSE).click()

    @allure.step('Catalog flowers redrose result')
    def result_flowers_redrose(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers customrose')
    def catalog_flowers_customrose(self):
        self.element_is_visible(Locators.FLOWERS_CUSTOMROSE).click()

    @allure.step('Catalog flowers customrose result')
    def result_flowers_customrose(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers lilya')
    def catalog_flowers_lilya(self):
        self.element_is_visible(Locators.FLOWERS_LILYA).click()

    @allure.step('Catalog flowers lilya result')
    def result_flowers_lilya(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers orkhideya')
    def catalog_flowers_orkhideya(self):
        self.element_is_visible(Locators.FLOWERS_ORKHIDEYA).click()

    @allure.step('Catalog flowers orkhideya result')
    def result_flowers_orkhideya(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers pion')
    def catalog_flowers_pion(self):
        self.element_is_visible(Locators.FLOWERS_PION).click()

    @allure.step('Catalog flowers pion result')
    def result_flowers_pion(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers podsoln')
    def catalog_flowers_podsoln(self):
        self.element_is_visible(Locators.FLOWERS_PODSOLN).click()

    @allure.step('Catalog flowers podsoln result')
    def result_flowers_podsoln(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers rose')
    def catalog_flowers_rose(self):
        self.element_is_visible(Locators.FLOWERS_ROSE).click()

    @allure.step('Catalog flowers rose result')
    def result_flowers_rose(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers romashki')
    def catalog_flowers_romashki(self):
        self.element_is_visible(Locators.FLOWERS_ROMASHKI).click()

    @allure.step('Catalog flowers romashki result')
    def result_flowers_romashki(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers tulpan')
    def catalog_flowers_tulpan(self):
        self.element_is_visible(Locators.FLOWERS_TULPAN).click()

    @allure.step('Catalog flowers tulpan result')
    def result_flowers_tulpan(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    @allure.step('Click catalog flowers exotic')
    def catalog_flowers_exotic(self):
        self.element_is_visible(Locators.FLOWERS_EXOTIC).click()

    @allure.step('Catalog flowers exotic result')
    def result_flowers_exotic(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result