import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageFlowers(BasePage):

    def fields_catalog_flowers(self):
        button = self.element_is_visible(Locators.FLOWERS_CATALOG)
        self.element_is_not_visible(button)
        self.element_is_visible(Locators.FLOWERS_CATALOG_CLICK).click()

    def result_catalog_flowers(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_all(self):
        self.element_is_visible(Locators.ALL_FLOWERS).click()

    def result_catalog_flowers_all(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_gladiolus(self):
        self.element_is_visible(Locators.FLOWERS_GLADIOLUS).click()

    def result_flowers_gladiolus(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_alstromeria(self):
        self.element_is_visible(Locators.FLOWERS_ALSTROMERIA).click()

    def result_flowers_alstromeria(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_gvozdika(self):
        self.element_is_visible(Locators.FLOWERS_GVOZDIKA).click()

    def result_flowers_gvozdika(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_hypsophila(self):
        self.element_is_visible(Locators.FLOWERS_HYPSOPHILA).click()

    def result_flowers_hypsophila(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_gortenzy(self):
        self.element_is_visible(Locators.FLOWERS_GORTENZY).click()

    def result_flowers_gortenzy(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_redrose(self):
        self.element_is_visible(Locators.FLOWERS_REDROSE).click()

    def result_flowers_redrose(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_customrose(self):
        self.element_is_visible(Locators.FLOWERS_CUSTOMROSE).click()

    def result_flowers_customrose(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_lilya(self):
        self.element_is_visible(Locators.FLOWERS_LILYA).click()

    def result_flowers_lilya(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_orkhideya(self):
        self.element_is_visible(Locators.FLOWERS_ORKHIDEYA).click()

    def result_flowers_orkhideya(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_pion(self):
        self.element_is_visible(Locators.FLOWERS_PION).click()

    def result_flowers_pion(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_podsoln(self):
        self.element_is_visible(Locators.FLOWERS_PODSOLN).click()

    def result_flowers_podsoln(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_rose(self):
        self.element_is_visible(Locators.FLOWERS_ROSE).click()

    def result_flowers_rose(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_romashki(self):
        self.element_is_visible(Locators.FLOWERS_ROMASHKI).click()

    def result_flowers_romashki(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_tulpan(self):
        self.element_is_visible(Locators.FLOWERS_TULPAN).click()

    def result_flowers_tulpan(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result

    def catalog_flowers_exotic(self):
        self.element_is_visible(Locators.FLOWERS_EXOTIC).click()

    def result_flowers_exotic(self):
        result = self.element_is_visible(Locators.FLOWERS_CHECK_NAME)
        result = result.text
        return result