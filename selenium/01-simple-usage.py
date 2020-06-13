# I'm reading the official doc
# https://selenium-python.readthedocs.io/getting-started.html

# webdriver module provides all the WebDriver implementations.
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

# create instance of Firefox WebDriver
driver = webdriver.Firefox()

# get() is used to navigate
driver.get("http://www.python.org")

# Assertion to confirm that title has "Python" word in it
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
# clear() is used to clear any prepopulated text
elem.clear()
# send_keys is like typing something using the keyboard
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

