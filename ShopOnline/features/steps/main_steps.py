from aloe import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from page import *


@before.all
def say_hello():
    print "Hello there!"
    print "ALOE will start to run tests right now..."


@after.all
def say_goodbye():
    print "Congratulations, I hope that all scenarios passed!"
    print "Goodbye!"


@before.each_example
def setup_browser(self, scenario, outline):
    world.driver = webdriver.Chrome("/usr/bin/chromedriver")
    world.driver.maximize_window()
    print "I open browser specially for you!"


@after.each_example
def tear_down(self, scenario, outline):
    world.driver.quit()
    print "I close browser specially for you!"


@step(r'webside "([^"]*)" is open')
def open_webside(self, address):
    world.driver.get(address)
    world.driver.maximize_window()


@step(r'page "([^"]*)" is open')
def open_page(self, pageName):
   page = MainPage(world.driver)
   page.women_button_click(pageName.lower())


@step(r'products are present')
def if_products_are_present(self):
    CategoryPage(world.driver).is_product_list_present()


@step(r'user set focus on product')
def set_focus_on_product(self, product_number = 0):
        CategoryPage(world.driver).focus_on_product(product_number)
        CategoryPage(world.driver).more_info_of_product_is_visible(product_number)
        CategoryPage(world.driver).price_of_product_is_visible(product_number)


@step(r'Add to cart button is clicked')
def add_to_cart_button_click(self, product_number=0):
    CategoryPage(world.driver).add_to_cart_button_click(product_number)
    return True


@step(r'Screen with "([^"]*)" is present')
def screen_with_messages_is_present(self, message):
    page = ProductSummaryPage(world.driver)
    page.is_product_summary_present()
    visible_message = page.get_message()
    assert visible_message == message