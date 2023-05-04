from pages.page_cart import FormPageCart
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure
from locators.form_page_locators import FormPageLocators as Locators


@allure.suite('Elements #3')
@allure.feature('Cart')
class TestFormPage:

    @allure.title('Check Cart')
    def test_cart(self, driver):
        with allure.step('Going to the catalog'):
            form_page = FormPageCart(driver, SERVICE_URL + 'catalog/vse-bukety/')
            form_page.open()
            driver.execute_script("window.scrollTo(0, 250)")
        with allure.step('Adding a product to the catalog'):
            form_page.fields_cart()
        with allure.step('Go to the cart page'):
            form_page = FormPageCart(driver, SERVICE_URL + 'personal/cart/')
            form_page.open()
            result = form_page.get_text(Locators.BASKET_TEXT)
        with allure.step('Matching items in the cart'):
            assert result == "БУКЕТ 'GOOD NEWS'", GlobalErrorMessages.WRONG_STATUS

