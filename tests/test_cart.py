from pages.page_cart import FormPageCart
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure


@allure.suite('Elements #3')
@allure.feature('Cart')
class TestFormPage:

    @allure.title('Check Cart')
    def test_cart(self, driver):
        form_page = FormPageCart(driver, SERVICE_URL + 'catalog/vse-bukety/')
        form_page.open()
        driver.execute_script("window.scrollTo(0, 250)")
        form_page.fields_cart()
        form_page = FormPageCart(driver, SERVICE_URL + 'personal/cart/')
        form_page.open()
        result = form_page.result_cart()
        assert result == "БУКЕТ 'GOOD NEWS'", GlobalErrorMessages.WRONG_STATUS

