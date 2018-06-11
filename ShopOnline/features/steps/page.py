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
        WebDriverWait(self.driver, secound).until(EC.element_to_be_clickable(By.XPATH, '//a[@title="Add to cart"]'))

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


 def focus_on_product(self, product_number):
     list_of_products = self.driver.find_elements(*CategoryPageLocators.list_of_products)
     product = list_of_products[product_number]
     ActionChains(self.driver).move_to_element(product)

 def add_to_cart_button_click(self, product_number=1):
     list_of_products = self.driver.find_elements(*CategoryPageLocators.list_of_products)
     product = list_of_products[product_number]
     element = product.find_element(*CategoryPageLocators.add_to_cart_button)
     pdb.set_trace()
     #BasePage(self.driver).wait_for_element_for_secounds(element, 5)
     #sleep(5)
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