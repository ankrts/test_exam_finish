import time

from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_make_samsung = '/html/body/div[1]/div/div/div[1]/div/div[1]/div/aside/div/div/div/div[2]/div[3]/div[2]/div/div[1]/label/span[2]'
    select_in_stock_button = '/html/body/div[1]/div/div/div[1]/div/div[1]/div/aside/div/div/div/div[2]/div[2]/div[2]/div/div[1]/label/span[2]'
    enter_price_low = '/html/body/div[1]/div/div/div[1]/div/div[1]/div/aside/div/div/div/div[2]/div[4]/div[1]/div[2]/div[1]/input'
    enter_price_high = '/html/body/div[1]/div/div/div[1]/div/div[1]/div/aside/div/div/div/div[2]/div[4]/div[1]/div[2]/div[2]/input'
    show_button = '//div[@class="listing-filters-apply-bubble__inner"]'
    select_product_1 = '//a[@title="Телевизор Samsung UE55AU9000UXCE (2021)"]'
    price_product_1_in_catalog_page = '/html/body/div[1]/div/div/div[1]/div/div[1]/div/main/div/div/div[3]/div/article[6]/div/div[1]/div[2]/div[3]/div[2]/div[1]/div'


    # Getters

    def get_select_make_samsung(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_make_samsung)))

    def get_select_in_stock_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_in_stock_button)))

    def get_enter_price_low(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_price_low)))

    def get_enter_price_high(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_price_high)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))

    def get_select_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    # Actions

    def click_select_make_samsung(self):
        self.get_select_make_samsung().click()
        print('Click on make Samsung')

    def click_select_in_stock_button(self):
        self.get_select_in_stock_button().click()
        print('Click "in stock" button')

    def input_get_enter_price_low(self, low_price):
        self.get_enter_price_low().click()
        self.get_enter_price_low().send_keys(Keys.CONTROL + "a")
        self.get_enter_price_low().send_keys(Keys.DELETE)
        self.get_enter_price_low().send_keys(low_price)
        print('Input low price = 50000')

    def input_get_enter_price_high(self, high_price):
        self.get_enter_price_high().click()
        self.get_enter_price_high().send_keys(Keys.CONTROL + "a")
        self.get_enter_price_high().send_keys(Keys.DELETE)
        self.get_enter_price_high().send_keys(high_price)
        print('Input high price = 100000')

    def click_show_button(self):
        self.get_show_button().click()
        print('Click "show" button')

    def click_select_product(self):
        self.get_select_product().click()
        print('Click on product')

    def move_to(self, element):
        self.action = ActionChains(self.driver)
        el = self.driver.find_element(By.XPATH, element)
        self.action.move_to_element(el).perform()
        print('Move to element')

    def check_price_catalog_page(self, price_element_catalog_page):
        price_for = self.driver.find_element(By.XPATH, price_element_catalog_page)
        value_price_catalog_page = price_for.text
        print(f'Product price on catalog page - {value_price_catalog_page}')
        self.assert_word(price_for, '99 990 ₽')
        print('Assertion price in catalog page OK')

    # Methods

    def m_filtration(self):
        self.driver.execute_script('window.scrollTo(0, 500)')
        # time.sleep(1)
        self.click_select_make_samsung()
        # time.sleep(1)
        self.click_select_in_stock_button()
        # time.sleep(1)
        self.input_get_enter_price_low('50000')
        # time.sleep(1)
        self.input_get_enter_price_high('100000')
        # time.sleep(1)
        self.click_show_button()
        time.sleep(2)
        self.move_to(self.select_product_1)
        time.sleep(1)
        self.check_price_catalog_page(self.price_product_1_in_catalog_page)
        # time.sleep(1)
        self.click_select_product()
        # time.sleep(1)


