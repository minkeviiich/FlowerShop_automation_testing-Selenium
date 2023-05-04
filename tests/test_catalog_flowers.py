from pages.page_catalog_flowers import FormPageFlowers
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages
import allure
from locators.form_page_locators import FormPageLocators as Locators


@allure.suite('Elements #5')
@allure.feature('Catalog Flowers')
class TestFormPage:

    @allure.title('Check Catalog Flawers')
    def test_catalog_flowers(self, driver):
        with allure.step('Going to the catalog'):
            form_page = FormPageFlowers(driver, SERVICE_URL)
            form_page.open()
            form_page.fields_catalog_flowers()
        with allure.step('Checking the directory'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты букеты", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers All')
    def test_flowers_all(self, driver):
        with allure.step('Going to the catalog (All'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
            form_page.catalog_flowers_all()
        with allure.step('Checking the directory (All)'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Все букеты", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Gladiolus')
    def test_flowers_gladiolus(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Glad.)'):
            form_page.catalog_flowers_gladiolus()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты букеты с гладиолусами", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Alstromeria')
    def test_flowers_alstromeria(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Alstr.)'):
            form_page.catalog_flowers_alstromeria()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с альстромерией", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Gvozdika')
    def test_flowers_gvozdika(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Alstr.)'):
            form_page.catalog_flowers_gvozdika()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с гвоздикой", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Hypsophila')
    def test_flowers_hypsophila(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Alstr.)'):
            form_page.catalog_flowers_hypsophila()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с гипсофилой", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Gortenzy')
    def test_flowers_gortenzy(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Gort.)'):
            form_page.catalog_flowers_gortenzy()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с гортензией", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Redrose')
    def test_flowers_redrose(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Redrose.)'):
            form_page.catalog_flowers_redrose()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с красной розой", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Customrose')
    def test_flowers_customrose(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Custom.)'):
            form_page.catalog_flowers_customrose()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с кустовой розой", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Lilya')
    def test_flowers_lilya(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Lil.)'):
            form_page.catalog_flowers_lilya()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с лилиями", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Orkhideya')
    def test_flowers_orkhideya(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Orkhi.)'):
            form_page.catalog_flowers_orkhideya()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с орхидеями", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Pion')
    def test_flowers_pion(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Pion.)'):
            form_page.catalog_flowers_pion()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с пионами", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Posoln')
    def test_flowers_podsoln(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Podsoln.)'):
            form_page.catalog_flowers_podsoln()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с подсолнухами", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Rose')
    def test_flowers_rose(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Rose.)'):
            form_page.catalog_flowers_rose()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с розой", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Romashki')
    def test_flowers_romashki(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Romashki.)'):
            form_page.catalog_flowers_romashki()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с ромашками", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Tulpan')
    def test_flowers_tulpan(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Tulpan.)'):
            form_page.catalog_flowers_tulpan()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с тюльпанами", GlobalErrorMessages.WRONG_STATUS

    @allure.title('Check Flawers Exotic')
    def test_flowers_exotic(self, driver):
        with allure.step('Checking the directory'):
            form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
            form_page.open()
        with allure.step('Checking the directory (Exotic.)'):
            form_page.catalog_flowers_exotic()
        with allure.step('Result'):
            result = form_page.get_text(Locators.FLOWERS_CHECK_NAME)
            assert result == "Букеты с экзотическими цветами", GlobalErrorMessages.WRONG_STATUS





