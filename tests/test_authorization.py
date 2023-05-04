import allure
from pages.page_authorization import FormPageAuthorization
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
from locators.form_page_locators import FormPageLocators as Locators


@allure.suite('Elements #1')
@allure.feature('Authorization')
class TestFormPage:

    @allure.title('Check Autorization')
    def test_authorization(self, driver):
        with allure.step('Go to the login page'):
            form_page = FormPageAuthorization(driver, SERVICE_URL)
            form_page.open()
        with allure.step('Filling out authorization fields'):
            form_page.fill_fields_authorization()
        with allure.step('Getting a result'):
            result = form_page.get_text(Locators.PERSONAL_CABINET)
        with allure.step('Checking Authorization'):
            assert result == 'Личный кабинет', GlobalErrorMessages.WRONG_STATUS
