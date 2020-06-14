# A page object is an area in the web app UI that
# your test is interacting

import unittest
from selenium import webdriver
import page
import elements
import locators

class PythonOrgSearch(unittest.TestCase):
  """ a sample test class to show how page object works """

  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://www.python.org")

  def test_search_in_python_org(self):
    """
    Tests python.org search feature.
    Searches for the word "pycon" then verifies that 
    some results show up.
    """

    # Load the main page.
    main_page = page.MainPage(self.driver)
    # Checks if the word "Python" is in title
    assert main_page.is_title_matches(), "python.org doesn't match."
    # Sets the text of search textbox to "pycon"
    main_page.search_text_element = "pycon"
    main_page.click_go_button()
    search_results_page = page.SearchResultsPage(self.driver)
    # Verifies that the results page is not empty
    assert search_results_page.is_results_found(), "No results found."

  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
  unittest.main()



"""

Python/selenium on  master [!?] via 🐍 3.7.5 took 7s 
➜ python3 06-page_ojects.py
.
----------------------------------------------------------------------
Ran 1 test in 5.331s

OK


"""