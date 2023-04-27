import allure
from pages.page_catalog_flowers import FormPageFlowers
from configuration import SERVICE_URL
from enums.global_exception import GlobalErrorMessages


class TestFormPage:

    def test_catalog_flowers(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL)
        form_page.open()
        form_page.fields_catalog_flowers()
        result = form_page.result_catalog_flowers()
        assert result == "Букеты букеты", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_all(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_all()
        result = form_page.result_catalog_flowers_all()
        assert result == "Все букеты", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_gladiolus(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_gladiolus()
        result = form_page.result_flowers_gladiolus()
        assert result == "Букеты букеты с гладиолусами", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_alstromeria(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_alstromeria()
        result = form_page.result_flowers_alstromeria()
        assert result == "Букеты с альстромерией", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_gvozdika(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_gvozdika()
        result = form_page.result_flowers_gvozdika()
        assert result == "Букеты с гвоздикой", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_hypsophila(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_hypsophila()
        result = form_page.result_flowers_hypsophila()
        assert result == "Букеты с гипсофилой", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_gortenzy(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_gortenzy()
        result = form_page.result_flowers_gortenzy()
        assert result == "Букеты с гортензией", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_redrose(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_redrose()
        result = form_page.result_flowers_redrose()
        assert result == "Букеты с красной розой", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_customrose(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_customrose()
        result = form_page.result_flowers_customrose()
        assert result == "Букеты с кустовой розой", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_lilya(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_lilya()
        result = form_page.result_flowers_lilya()
        assert result == "Букеты с лилиями", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_orkhideya(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_orkhideya()
        result = form_page.result_flowers_orkhideya()
        assert result == "Букеты с орхидеями", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_pion(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_pion()
        result = form_page.result_flowers_pion()
        assert result == "Букеты с пионами", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_podsoln(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_podsoln()
        result = form_page.result_flowers_podsoln()
        assert result == "Букеты с подсолнухами", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_rose(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_rose()
        result = form_page.result_flowers_rose()
        assert result == "Букеты с розой", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_romashki(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_romashki()
        result = form_page.result_flowers_romashki()
        assert result == "Букеты с ромашками", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_tulpan(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_tulpan()
        result = form_page.result_flowers_tulpan()
        assert result == "Букеты с тюльпанами", GlobalErrorMessages.WRONG_STATUS

    def test_flowers_exotic(self, driver):
        form_page = FormPageFlowers(driver, SERVICE_URL + 'catalog/bukety/')
        form_page.open()
        form_page.catalog_flowers_exotic()
        result = form_page.result_flowers_exotic()
        assert result == "Букеты с экзотическими цветами", GlobalErrorMessages.WRONG_STATUS





