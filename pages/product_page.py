import time

from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_add_to_cart = '/html/body/div[1]/div/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/span'
    select_go_to_cart = '/html/body/div[1]/div/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/span/a'
    price_product_1_in_product_page = '/html/body/div[1]/div/div/div[1]/div[1]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div'



    # Getters

    def get_select_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_add_to_cart)))

    def get_select_go_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_go_to_cart)))

    # Actions

    def click_select_add_to_cart(self):
        self.get_select_add_to_cart().click()
        print('Click "add to cart" button')

    def click_select_go_to_cart(self):
        self.get_select_go_to_cart().click()
        print('Click "go to cart" button')

    def check_price_product_page(self, price_element_product_page):
        price_for = self.driver.find_element(By.XPATH, price_element_product_page)
        value_price_personal_page = price_for.text
        print(f'Product price on product page - {value_price_personal_page}')
        self.assert_word(price_for, '99 990 ₽')
        print('Assertion price in product page OK')

    # Methods

    def m_get_product(self):
        self.check_price_product_page(self.price_product_1_in_product_page)
        time.sleep(2)
        self.click_select_add_to_cart()
        time.sleep(1)
        self.click_select_go_to_cart()


