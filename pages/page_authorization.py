import time
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from configuration import USER_LOGIN, PASSWORD, PASSWORD_ERROR, USER_LOGIN_ERROR
import allure


class FormPageAuthorization(BasePage):

    @allure.step('Fill Fields Authorization')
    def fill_fields_authorization(self):
        with allure.step('Click "LOGIN"'):
            self.click_element(Locators.LOG_IN)
        with allure.step('Field completion'):
            self.send_text(Locators.USER_LOGIN, USER_LOGIN)
            self.send_text(Locators.PASSWORD, PASSWORD)
        with allure.step('Click "ENTER"'):
            self.click_element(Locators.ENTER)

    @allure.step('Authorization Errorpassword')
    def fill_fields_authorization_errorpassword(self):
        with allure.step('Click "LOGIN" (errorpassword)'):
            self.click_element(Locators.LOG_IN)
        with allure.step('Field completion (errorpassword)'):
            self.send_text(Locators.USER_LOGIN, USER_LOGIN)
            self.send_text(Locators.PASSWORD, PASSWORD_ERROR)
        with allure.step('Click "ENTER" (errorpassword)'):
            self.click_element(Locators.ENTER)

    @allure.step('Authorization Errorname')
    def fill_fields_authorization_errorname(self):
        with allure.step('Click "LOGIN" (errorname)'):
            self.click_element(Locators.LOG_IN)
        with allure.step('Field completion (errorname)'):
            self.send_text(Locators.USER_LOGIN, USER_LOGIN_ERROR)
            self.send_text(Locators.PASSWORD, PASSWORD)
        with allure.step('Click "ENTER" (errorname)'):
            self.click_element(Locators.ENTER)

    @allure.step('Forgot Password')
    def forgot_password(self):
        self.click_element(Locators.LOG_IN)
        self.click_element(Locators.FORGOT_PASSWORD)
