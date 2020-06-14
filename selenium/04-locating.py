# Locating elements
# https://selenium-python.readthedocs.io/locating-elements.html

from selenium import webdriver
from selenium.webdriver.common.by import By

"""

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

find_elements_by_name
find_elements_by_xpath
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

"""

# apart from the the public methodes given above

driver.find_elements(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')

# attributes available for By class:

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "tag name"
CSS_SELECTOR = "css selector"

# Locating by Id

# for example : 

"""

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>

"""

# form element can be located like this :

login_form = driver.find_element_by_id('loginForm')




# Locating by Name

# for example : 

"""

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>

"""

# username & pw el can be located like this :

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

continue = driver.find_element_by_name('continue')




# Locating by XPath
# XPath is the language used for locatin nodes in a XML document
# usage of XPath is when you don't have a suitable id or name attribute
# for the el is absolute terms or relatve to an element that does have
# name or attribute.

# for example :

"""

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>

"""

# the form el can be located like this :

# 1. absolute path (would break if the HTML was changed only slightly)

login_form = driver.find_element_by_xpath("/html/body/form[1]")

# 2. First form element in the HTML

login_form = driver.find_element_by_xpath("//form[1]")

# 3. The form el with attribute named id and the value loginForm

login_form = driver.find_element_by_xpath("//form[@id='loginForm']")

# the username el can be located like this :

# 1. First form element with an input child element with attribute named 
# name and the value username

username = driver.find_element_by_xpath("//form[input/@name='username']")

# 2. First input child element of the form element with attribute named id
# and the value loginform

username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")

# 3. First input element with attribute named 'name' and the value user-name

username = driver.find_element_by_xpath("//input[@name='username']")

# the "Clear" button el can be located like this :

# 1. Input with attribute named name and the value continue and
# attribute named type the value button

clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")

# 2. Fouth input child element of the form element with attribute named id 
# and value loginForm

clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")





# Locating Hyperlinks by Link Text

# for example :

"""

<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
<html>

"""

# continue.html link can be located like this :

continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')




# Locating el by Tag Name

# for example :

"""

<h1>Welcome</h1>

"""

heading1 = driver.find_element_by_tag_name('h1')




# Locating el by Class Name

# for example :

"""

<p class="content">Site content goes here.</p>

"""

content = driver.find_element_by_css_selector('p.content')

# Selenium tips : cess selector (doc by saucelabs) :
# https://saucelabs.com/resources/articles/selenium-tips-css-selectors
