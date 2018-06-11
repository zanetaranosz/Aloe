Feature: Adding to basket

  As a customer
  I want to add chosen chlothes to cart
  To make shopping

  Scenario: Adding one thing to basket
    Given webside "http://automationpractice.com/index.php" is open
      And page "women" is open
      And products are present
    When user set focus on product
      And Add to cart button is clicked
    Then Screen with "Product successfully added to your shopping cart" is present
