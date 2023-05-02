from pages.page_authorization import FormPageAuthorization
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure


@allure.suite('Elements #2')
@allure.feature('Authorization Error')
class TestFormPage:

    @allure.title('Check Autorization Errorpassword')
    def test_authorization_errorpassword(self, driver):
        form_page = FormPageAuthorization(driver, SERVICE_URL)
        form_page.open()
        form_page.fill_fields_authorization_errorpassword()
        result = form_page.result_authorization_errorpassword()
        assert result == 'Неверный логин или пароль.', GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Autorization Errorname')
    def test_authorization_errorname(self, driver):
        form_page = FormPageAuthorization(driver, SERVICE_URL)
        form_page.open()
        form_page.fill_fields_authorization_errorname()
        result = form_page.result_authorization_errorname()
        assert result == 'Неверный логин или пароль.', GlobalErrorMessages.WRONG_STATUS

