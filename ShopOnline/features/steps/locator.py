from selenium.webdriver.common.by import By

class MainPageLocators(object):
    logo =  (By.CLASS_NAME, "logo img-responsive")
    women_button = (By.PARTIAL_LINK_TEXT, "Women")
    dresses_button = (By.PARTIAL_LINK_TEXT, "Dresses")
    search_box = (By.ID, "search_query_top")
    cart_button = (By.LINK_TEXT, "View my shopping cart")
    cart_quantity = (By.CLASS_NAME, "ajax_cart_quantity")

class CategoryPageLocators(object):
    list_of_products = (By.XPATH, "//ul[contains(@class,'product_list')]/li")
    add_to_cart_button = (By.XPATH, ".//a[contains(@title, 'Add to cart')]")
    price = (By.XPATH,"//span[contains(@class, 'price product-price')]")
    more_button = (By.XPATH, "//a[contains(@title, 'View') and contains(@itemprop,'url')]")


