from pages.page_authorization import FormPageAuthorization
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure
from locators.form_page_locators import FormPageLocators as Locators


@allure.suite('Elements #2')
@allure.feature('Authorization Error')
class TestFormPage:

    @allure.title('Check Autorization Errorpassword')
    def test_authorization_errorpassword(self, driver):
        with allure.step('Go to the login page'):
            form_page = FormPageAuthorization(driver, SERVICE_URL)
            form_page.open()
        with allure.step('Filling out authorization fields'):
            form_page.fill_fields_authorization_errorpassword()
        with allure.step('Getting a result'):
            result = form_page.get_text(Locators.PERSONAL_CABINET_ERROR)
        with allure.step('Authorization check (errorpassword)'):
            assert result == 'Неверный логин или пароль.', GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Autorization Errorname')
    def test_authorization_errorname(self, driver):
        with allure.step('Go to the login page'):
            form_page = FormPageAuthorization(driver, SERVICE_URL)
            form_page.open()
        with allure.step('Filling out authorization fields'):
            form_page.fill_fields_authorization_errorname()
        with allure.step('Getting a result'):
            result = form_page.get_text(Locators.PERSONAL_CABINET_ERROR)
        with allure.step('Authorization check (errorname)'):
            assert result == 'Неверный логин или пароль.', GlobalErrorMessages.WRONG_STATUS

