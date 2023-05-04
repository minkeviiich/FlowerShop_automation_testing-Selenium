from pages.page_authorization import FormPageAuthorization
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure
from locators.form_page_locators import FormPageLocators as Locators


@allure.suite('Elements #6')
@allure.feature('Forgot Password')
class TestFormPage:

    @allure.title('Check Forgot Password')
    def test_forgot_password(self, driver):
        with allure.step('Go to the login page'):
            form_page = FormPageAuthorization(driver, SERVICE_URL)
            form_page.open()
        with allure.step('Go to the password request page'):
            form_page.forgot_password()
            result = form_page.get_text(Locators.RESULT_FORGOT_PASSWORD)
        with allure.step('Checking the result'):
            assert result == 'Запрос пароля', GlobalErrorMessages.WRONG_STATUS

