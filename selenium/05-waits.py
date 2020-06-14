# Most of the web apps are using AJAX techniques.
# When a page is loaded by the browser, the elements
# may load at different time intervals.
# Not yet present element in the DOM will cause
# ElementNotVisibleException
# Using waits can solve this

# Two types of waits : implicit / explicit 

# Explicit Waits

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delays_loading")
try:
  element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myDynamicElement"))
  )
finally:
  driver.quit()

# This waits up to 10 sec before throwing a TimeoutException 
# unless it finds the element to return within 10 seconds.

# Selenium Python binding provides some convenience methods
# see: https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

"""

title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

"""

wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))





# Custom Wait Conditions

# when none of the previous convenience methods fit your requirements
# created using a class with __call__ method which returns
# False when the condition doesn't match.

class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class
  
  def __call__(self, driver):
    el = driver.find_element(*self.locator) # Finding the referenced element
    if self.css_class in el.get_attribute("class"):
      return el
    else:
      return False
  
# Wait until an elment with id='myNewInput' has class 'myCSSClass'
wait = WebDriverWait(driver, 10)
el = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))





# Implicit Waits
# tells WebDriver to poll the DOM for a certain amout of time
# when trying to find any element (or elements) not immediately available.

driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id("myDynamicElement")

