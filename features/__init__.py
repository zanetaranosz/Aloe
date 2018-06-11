from aloe import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


@before.all
def say_hello():
    print "Hello there!"
    print "ALOE will start to run tests right now..."

@after.all
def say_goodbye():
    print "Congratulations, I hope that all scenarios passed!"
    print "Goodbye!"

@before.each_example
def setup_browser(self,scenario, outline):
    world.driver = webdriver.Chrome("/usr/bin/chromedriver")
    world.driver.maximize_window()
    print "I open browser specially for you!"

@after.each_example
def tear_down(self, scenario, outline):
    world.driver.quit()
    print "I close browser specially for you!"

@step(r'I open "([^"]*)" webside')
def open_webside(self, address):
    world.driver.get(address)
    world.driver.maximize_window()


@step(r'I type "([^"]*)"')
def type_in_search_box(self, phrase):
    world.search_box = world.driver.find_element_by_id("lst-ib")
    world.search_box.send_keys(phrase)


@step(r'I click on search')
def click_search(self):
    world.search_box.send_keys(Keys.ENTER)
    world.driver.implicitly_wait(20)


@step(r'I should see "([^"]*)"')
def find_phrase(self, phrase):
    world.driver.find_element_by_xpath("//a[contains(.,'"+phrase+"')]")

