import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from configuration import USER_LOGIN, PASSWORD, PASSWORD_ERROR, USER_LOGIN_ERROR


class FormPageAuthorization(BasePage):

    def fill_fields_authorization(self):
        self.element_is_visible(Locators.LOG_IN).click()
        self.element_is_visible(Locators.USER_LOGIN).send_keys(USER_LOGIN)
        self.element_is_visible(Locators.PASSWORD).send_keys(PASSWORD)
        self.element_is_visible(Locators.ENTER).click()

    def fill_fields_authorization_errorpassword(self):
        self.element_is_visible(Locators.LOG_IN).click()
        self.element_is_visible(Locators.USER_LOGIN).send_keys(USER_LOGIN)
        self.element_is_visible(Locators.PASSWORD).send_keys(PASSWORD_ERROR)
        self.element_is_visible(Locators.ENTER).click()

    def fill_fields_authorization_errorname(self):
        self.element_is_visible(Locators.LOG_IN).click()
        self.element_is_visible(Locators.USER_LOGIN).send_keys(USER_LOGIN_ERROR)
        self.element_is_visible(Locators.PASSWORD).send_keys(PASSWORD)
        self.element_is_visible(Locators.ENTER).click()

    def result_authorization(self):
        result = self.element_is_visible(Locators.PERSONAL_CABINET)
        result = result.text
        return result

    def result_authorization_errorpassword(self):
        result = self.element_is_visible(Locators.PERSONAL_CABINET_ERROR)
        result = result.text
        return result

    def result_authorization_errorname(self):
        result = self.element_is_visible(Locators.PERSONAL_CABINET_ERROR)
        result = result.text
        return result