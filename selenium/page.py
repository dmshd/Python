# used in 06-page_objects.py
# example from the selenium doc

from elements import BasePageElement
from locators import MainPageLocators

class SearchTextElement(BasePageElement):
  """ This class gets the search text from the specified locator """

  # The locator for search box where search string is entered
  locator = 'q'


class BasePage(object):
  """ Base class to init the base page that will be called from all pages """
  
  def __init__(self, driver):
    self.driver = driver

class MainPage(BasePage):
  """ Home page action methods come here. I.e python.org """
  # Declares a variable that will contain the retrieved text
  search_text_element = SearchTextElement()

  def is_title_matches(self):
    """ Verifies that the hardcoded text "Python" appears in page title """
    return "Python" in self.driver.title

  def click_go_button(self):
    """ Triggers the search """
    el = self.driver.find_element(*MainPageLocators.GO_BUTTON)
    el.click()

class SearchResultsPage(BasePage):
  """ Search results page action methods come here """

  def is_results_found(self):
    # Probably should search for this text in the specific page
    # element, but as for now it works fine
    return "No results found." not in self.driver.page_source
