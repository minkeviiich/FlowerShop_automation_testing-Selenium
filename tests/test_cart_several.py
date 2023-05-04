from pages.page_cart import FormPageCart
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure
from locators.form_page_locators import FormPageLocators as Locators


@allure.suite('Elements #4')
@allure.feature('Authorization Cart Several')
class TestFormPage:

    @allure.title('Check Cart Several')
    def test_cart_several(self, driver):
        with allure.step('Going to the catalog'):
            form_page = FormPageCart(driver, SERVICE_URL + 'catalog/vse-bukety/')
            form_page.open()
            driver.execute_script("window.scrollTo(0, 250)")
        with allure.step('Adding a product to the catalog'):
            form_page.fields_cart_several()
        with allure.step('Go to the cart page'):
            form_page = FormPageCart(driver, SERVICE_URL + 'personal/cart/')
            form_page.open()
        with allure.step('Product and price matches in the cart'):
            result = form_page.get_text(Locators.BASKET_TEXT)
            assert result == "БУКЕТ ОБЛАКО", GlobalErrorMessages.WRONG_STATUS
            result = form_page.get_text(Locators.BASKET_TEXT_NUMBER)
            assert result == "180.00 руб.", GlobalErrorMessages.WRONG_STATUS

    def test_cart_several_two(self, driver):
        with allure.step('Going to the catalog'):
            form_page = FormPageCart(driver, SERVICE_URL + 'catalog/vse-bukety/')
            form_page.open()
            driver.execute_script("window.scrollTo(0, 250)")
        with allure.step('Adding a product to the catalog'):
            form_page.fields_cart_several_two()
        with allure.step('Go to the cart page'):
            form_page = FormPageCart(driver, SERVICE_URL + 'personal/cart/')
            form_page.open()
        with allure.step('Product and price matches in the cart'):
            result = form_page.get_text(Locators.BASKET_TEXT)
            assert result == "БУКЕТ ОБЛАКО", GlobalErrorMessages.WRONG_STATUS
            result = form_page.get_text(Locators.BASKET_TEXT_NUMBER)
            assert result == "240.00 руб.", GlobalErrorMessages.WRONG_STATUS
