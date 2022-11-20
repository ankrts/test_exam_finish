from base.base_class import Base
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):

    url = 'https://www.technopark.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_catalog = '//span[@class="header-catalog-button__label tp-typography tp-typography--v-body-3 tp-typography--w-medium tp-typography--align-left header-catalog-button__label"]'
    select_telec = '/html/body/div[1]/div/div/header/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/nav/div[3]/a'
    select_telec_4k = '/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/aside/div/div[1]/nav/ul/li[3]/a/span'

    # Getters

    def get_select_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_catalog)))

    def get_select_telec(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_telec)))

    def get_select_telec_4k(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_telec_4k)))

    # Actions

    def click_select_catalog(self):
        self.get_select_catalog().click()
        print('Select catalog menu')

    def click_select_telec(self):
        self.get_select_telec().click()
        print('Select televisions, audio, hi-fi')

    def click_select_telec_4k(self):
        self.get_select_telec_4k().click()
        print('Select 4K UHD televisions')

    # Methods

    def m_enter_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

    def m_select_televisions(self):
        self.click_select_catalog()
        self.click_select_telec()
        self.click_select_telec_4k()

