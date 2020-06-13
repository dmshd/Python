# a test for python.org search functionnality

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 

class PythonOrgSearch(unittest.TestCase):

  # initialization, seUp will get called before every test
  # function written with this test class.

  def setUp(self):
    self.driver = webdriver.Firefox()

  # test case method should always start with "test"
  # the first line inside this method cireate a local
  # reerence to the driver object created in setUp()

  def test_search_in_python_org(self):
    driver = self.driver
    driver.get("http://www.python.org")
    self.assertIn("Python", driver.title)
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()
