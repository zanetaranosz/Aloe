from time import sleep

from features.steps.locator import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_for_secounds(self, element, secound):
        wait = WebDriverWait(self.driver, secound)
        wait.until(EC.visibility_of(element))

class MainPage(BasePage):

 def women_button_click(self, button_name):

    element = self.driver.find_element(*MainPageLocators.women_button)
    element.click()

def cart_button_click(self):
    element = self.driver.find_element(*MainPageLocators.cart_button)
    element.click()

def cart_quantity(self):
    element = self.driver.find_element(*MainPageLocators.cart_quantity)
    quantity = element.get_value()
    return quantity


class CategoryPage(BasePage):

 def is_product_list_present(self):
    element = self.driver.find_elements(*CategoryPageLocators.list_of_products)
    return True if len(element)>=1 else False

 def focus_on_product(self, product_number=0):
     list_of_products = self.driver.find_elements(*CategoryPageLocators.list_of_products)
     product = list_of_products[product_number]
     ActionChains(self.driver).move_to_element(product).perform()

 def add_to_cart_button_click(self, product_number=0):
     list_of_products = self.driver.find_elements(*CategoryPageLocators.list_of_products)
     product = list_of_products[product_number]
     element = product.find_element(*CategoryPageLocators.add_to_cart_button)
     self.wait_for_element_for_secounds(element, 5)
     element.click()

 def price_of_product_is_visible(self, product_number=1):
     list_of_products = self.driver.find_elements(*CategoryPageLocators.list_of_products)
     product = list_of_products[product_number]
     element = product.find_element(*CategoryPageLocators.price)
     element.is_displayed()

 def more_info_of_product_is_visible(self, product_number=1):
     list_of_products = self.driver.find_elements(*CategoryPageLocators.list_of_products)
     product = list_of_products[product_number]
     element = product.find_element(*CategoryPageLocators.more_button)
     element.is_displayed()


class ProductSummaryPage(BasePage):

 def is_product_summary_present(self):
     element = self.driver.find_element(*SummaryProductPageLocators.product_summary)
     self.wait_for_element_for_secounds(element, 5)
     element.is_displayed()

 def get_message(self):
     element = self.driver.find_element(*SummaryProductPageLocators.message)
     return element.text

 def get_value_items_in_cart(self):
     element = self.driver.find_element(*SummaryProductPageLocators.items_in_cart)
     return element.text
