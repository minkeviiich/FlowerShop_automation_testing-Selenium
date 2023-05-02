from pages.page_cart import FormPageCart
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure


@allure.suite('Elements #4')
@allure.feature('Authorization Cart Several')
class TestFormPage:

    @allure.title('Check Cart Several')
    def test_cart_several(self, driver):
        form_page = FormPageCart(driver, SERVICE_URL + 'catalog/vse-bukety/')
        form_page.open()
        driver.execute_script("window.scrollTo(0, 250)")
        form_page.fields_cart_several()
        form_page = FormPageCart(driver, SERVICE_URL + 'personal/cart/')
        form_page.open()
        result = form_page.result_cart()
        assert result == "БУКЕТ ОБЛАКО", GlobalErrorMessages.WRONG_STATUS
        result = form_page.result_cart_several()
        assert result == "180.00 руб.", GlobalErrorMessages.WRONG_STATUS

    def test_cart_several_two(self, driver):
        form_page = FormPageCart(driver, SERVICE_URL + 'catalog/vse-bukety/')
        form_page.open()
        driver.execute_script("window.scrollTo(0, 250)")
        form_page.fields_cart_several_two()
        form_page = FormPageCart(driver, SERVICE_URL + 'personal/cart/')
        form_page.open()
        result = form_page.result_cart()
        assert result == "БУКЕТ ОБЛАКО", GlobalErrorMessages.WRONG_STATUS
        result = form_page.result_cart_several()
        assert result == "240.00 руб.", GlobalErrorMessages.WRONG_STATUS
