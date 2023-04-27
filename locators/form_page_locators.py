from selenium.webdriver.common.by import By


class FormPageLocators:
    # test_authorization
    LOG_IN = (By.XPATH, "//a[@class='lk_user_bt']")
    USER_LOGIN = (By.XPATH, "//input[@name='USER_LOGIN']")
    PASSWORD = (By.XPATH, "//input[@name='USER_PASSWORD']")
    ENTER = (By.XPATH, "//input[@name='AUTH_ACTION']")
    PERSONAL_CABINET = (By.XPATH, "//a[@class='lk_user_bt exit']")
    PERSONAL_CABINET_ERROR = (By.XPATH, "//div[@class='alert alert-danger']")
    # test_cart
    FLOWERS = (By.XPATH, "//div[@id='bx_3966226736_981']")
    FLOWERS_TWO = (By.XPATH, "//div[@id='bx_3966226736_587']")
    FLOWERS_CLICK = (By.XPATH, "//a[@href='/catalog/vse-bukety/?action=ADD2BASKET&id=981']")
    FLOWERS_CLICK_SEVERAL = (By.XPATH, "//a[@href='/catalog/vse-bukety/?action=ADD2BASKET&id=587']")
    FLOWERS_SEVERAL_CLICK = (By.XPATH, "//a[@class='plus']")
    BASKET_TEXT = (By.XPATH, "//span[@data-entity='basket-item-name']")
    BASKET_TEXT_NUMBER = (By.XPATH, "//td[@class='basket-items-list-item-price']")
    # test_catalog_flowers
    FLOWERS_CATALOG = (By.XPATH, "//ul[@class='head_menu']//li[2]")
    FLOWERS_CATALOG_CLICK = (By.XPATH, "//ul[@class='head_menu']//li//a")
    ALL_FLOWERS = (By.XPATH, "//div[@class='l_menu_lvl2_el'][1]")
    FLOWERS_GLADIOLUS = (By.XPATH, "//div[@class='l_menu_lvl2_el'][2]")
    FLOWERS_ALSTROMERIA = (By.XPATH, "//div[@class='l_menu_lvl2_el'][3]")
    FLOWERS_GVOZDIKA = (By.XPATH, "//div[@class='l_menu_lvl2_el'][4]")
    FLOWERS_HYPSOPHILA = (By.XPATH, "//div[@class='l_menu_lvl2_el'][5]")
    FLOWERS_GORTENZY = (By.XPATH, "//div[@class='l_menu_lvl2_el'][6]")
    FLOWERS_REDROSE = (By.XPATH, "//div[@class='l_menu_lvl2_el'][7]")
    FLOWERS_CUSTOMROSE = (By.XPATH, "//div[@class='l_menu_lvl2_el'][8]")
    FLOWERS_LILYA = (By.XPATH, "//div[@class='l_menu_lvl2_el'][9]")
    FLOWERS_ORKHIDEYA = (By.XPATH, "//div[@class='l_menu_lvl2_el'][10]")
    FLOWERS_PION = (By.XPATH, "//div[@class='l_menu_lvl2_el'][11]")
    FLOWERS_PODSOLN = (By.XPATH, "//div[@class='l_menu_lvl2_el'][12]")
    FLOWERS_ROSE = (By.XPATH, "//div[@class='l_menu_lvl2_el'][13]")
    FLOWERS_ROMASHKI = (By.XPATH, "//div[@class='l_menu_lvl2_el'][14]")
    FLOWERS_TULPAN = (By.XPATH, "//div[@class='l_menu_lvl2_el'][15]")
    FLOWERS_EXOTIC = (By.XPATH, "//div[@class='l_menu_lvl2_el'][16]")
    FLOWERS_CHECK_NAME = (By.XPATH, "//div[@class='standart_width']//h1")
    # test_parameter_selection
    PRICE_MIN = (By.XPATH, "//input[@id='arrFilter_P1_MIN']")
    PRICE_MAX = (By.XPATH, "//input[@id='arrFilter_P1_MAX']")
    PRICE_ENTER = (By.XPATH, "//div[@id='modef']//a")
    # test_catalog_compositions
    COMPOSITIONS_CATALOG = (By.XPATH, "//ul[@class='mob_head_menu']/li[2]//a")
    COMPOSITIONS_CATALOG_CLICK = (By.XPATH, "//ul[@class='mob_head_menu']/li[2]//a")


