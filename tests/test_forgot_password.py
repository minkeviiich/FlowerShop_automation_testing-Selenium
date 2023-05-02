from pages.page_authorization import FormPageAuthorization
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure


@allure.suite('Elements #6')
@allure.feature('Forgot Password')
class TestFormPage:

    @allure.title('Check Forgot Password')
    def test_forgot_password(self, driver):
        form_page = FormPageAuthorization(driver, SERVICE_URL)
        form_page.open()
        form_page.forgot_password()
        result = form_page.result_forgot_password()
        assert result == 'Запрос пароля', GlobalErrorMessages.WRONG_STATUS

