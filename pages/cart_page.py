import time

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = '/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[4]/div/button'
    price_product_1_in_product_cart = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/span/div[1]/div[2]/div/div/div[1]/div/div[4]/div'
    total_price = '/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[3]/div[3]/div[2]'

    phone_number = '//input[@type="tel"]'
    name = '//*[@id="__layout"]/div/div[2]/div/div/div[1]/span/form/div[1]/div[1]/div/div[2]/input'
    email = '//*[@id="__layout"]/div/div[2]/div/div/div[1]/span/form/div[1]/div[1]/div/div[3]/input'
    checkout_button_finish = '//*[@id="__layout"]/div/div[2]/div/div/div[1]/span/form/div[1]/div[2]/div/button'

    finish_test = '//h3[@class="checkout-logistics__title"]'

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_checkout_button_finish(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button_finish)))

    def get_finish_test(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.finish_test)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout button')

    def input_phone_number(self, phone_number):
        self.get_phone_number().click()
        self.get_phone_number().send_keys(phone_number)
        print('Input phone number')

    def input_name(self, name):
        self.get_name().click()
        self.get_name().send_keys(name)
        print('Input name')

    def input_email(self, email):
        self.get_email()
        self.get_email().send_keys(email)
        print('Input email')

    def click_checkout_button_finish(self):
        self.get_checkout_button_finish().click()
        print('Click checkout button finish')

    def check_price_cart_page(self, price_element_cart_page):
        price_for = self.driver.find_element(By.XPATH, price_element_cart_page)
        value_price_cart_page = price_for.text
        print(f'Product price on cart page - {value_price_cart_page}')
        self.assert_word(price_for, '99 990 ₽')
        print('Assertion price in cart page OK')

    def check_total_price(self, price_element_total):
        price_for = self.driver.find_element(By.XPATH, price_element_total)
        value_total_price = price_for.text
        print(f'Total price - {value_total_price}')
        self.assert_word(price_for, '99 990 ₽')
        print('Assertion total price OK')

    # Methods

    def m_product_confirmation(self):
        self.check_price_cart_page(self.price_product_1_in_product_cart)
        self.check_total_price(self.total_price)
        time.sleep(3)
        self.click_checkout_button()
        time.sleep(2)
        self.input_phone_number('89185554433')
        self.input_name('Anton')
        self.input_email('test@mail.ru')
        self.click_checkout_button_finish()
        self.assert_word(self.get_finish_test(), '1. Способ доставки')
