import time

from pages.cart_page import Cart_page
from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.product_page import Product_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains


def test_buy():

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\akartashev\\PycharmProjects\\resourse\\chromedriver.exe', chrome_options=options)
    action = ActionChains(driver)

    print('Start exam test')

    mp = Main_page(driver)
    mp.m_enter_site()
    mp.m_select_televisions()

    cp = Catalog_page(driver)
    cp.m_filtration()

    pp = Product_page(driver)
    pp.m_get_product()

    ctp = Cart_page(driver)
    ctp.m_product_confirmation()

    print('Finish exam test')