import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from configuration import USER_LOGIN, PASSWORD, PASSWORD_ERROR, USER_LOGIN_ERROR
import allure


class FormPageAuthorization(BasePage):

    @allure.step('Fill Fields Authorization')
    def fill_fields_authorization(self):
        with allure.step('Click "LOGIN"'):
            self.element_is_visible(Locators.LOG_IN).click()
        with allure.step('Field completion'):
            self.element_is_visible(Locators.USER_LOGIN).send_keys(USER_LOGIN)
            self.element_is_visible(Locators.PASSWORD).send_keys(PASSWORD)
        with allure.step('Click "ENTER"'):
            self.element_is_visible(Locators.ENTER).click()

    @allure.step('Authorization Errorpassword')
    def fill_fields_authorization_errorpassword(self):
        with allure.step('Click "LOGIN" (errorpassword)'):
            self.element_is_visible(Locators.LOG_IN).click()
        with allure.step('Field completion (errorpassword)'):
            self.element_is_visible(Locators.USER_LOGIN).send_keys(USER_LOGIN)
            self.element_is_visible(Locators.PASSWORD).send_keys(PASSWORD_ERROR)
        with allure.step('Click "ENTER" (errorpassword)'):
            self.element_is_visible(Locators.ENTER).click()

    @allure.step('Authorization Errorname')
    def fill_fields_authorization_errorname(self):
        with allure.step('Click "LOGIN" (errorname)'):
            self.element_is_visible(Locators.LOG_IN).click()
        with allure.step('Field completion (errorname)'):
            self.element_is_visible(Locators.USER_LOGIN).send_keys(USER_LOGIN_ERROR)
            self.element_is_visible(Locators.PASSWORD).send_keys(PASSWORD)
        with allure.step('Click "ENTER" (errorname)'):
            self.element_is_visible(Locators.ENTER).click()

    @allure.step('Forgot Password')
    def forgot_password(self):
        self.element_is_visible(Locators.LOG_IN).click()
        self.element_is_visible(Locators.FORGOT_PASSWORD).click()

    @allure.step('Result Autorization')
    def result_authorization(self):
        result = self.element_is_visible(Locators.PERSONAL_CABINET)
        result = result.text
        return result

    @allure.step('Result Autorization Errorpassword')
    def result_authorization_errorpassword(self):
        result = self.element_is_visible(Locators.PERSONAL_CABINET_ERROR)
        result = result.text
        return result

    @allure.step('Result Autorization Errorname')
    def result_authorization_errorname(self):
        result = self.element_is_visible(Locators.PERSONAL_CABINET_ERROR)
        result = result.text
        return result

    @allure.step('Result Forgot Password')
    def result_forgot_password(self):
        result = self.element_is_visible(Locators.RESULT_FORGOT_PASSWORD)
        result = result.text
        return result
