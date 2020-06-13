# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

driver.get("http://www.google.com")

# el is for element

el = driver.find_element_by_id("passwd-id")
el = driver.find_element_by_name("passwd")
el = driver.find_element_by_xpath("//input[@id='passwd-id']")

 # testing keyboard shortcuts is also possible

el.send_keys(" and some", Keys.ARROW_DOWN)

el.clear()

# Filling in forms

el = driver.find_element_by_xpath("//select[@name='name']")
all_options = el.find_elements_by_tag_name("option")
for option in all_options:
  print("Value is: %s" % option.get_attribute("value"))

# more efficient way to interract with SELECT

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

# deselect all the selected options

select = Select(driver.find_element_by_id('id'))
select.deselect_all()

# list all default selected options with Select class

select = Select(driver.find_element_by_xpath("//selec[@name='name']"))
all_selected_options = select.all_selected_options

# get all available options

options = select.options

# form submission assuming the button as the ID "submit"

driver.find_element_by_id("submit").click()

# alternative : the submit() method will scan the DOM and click on submit

el.submit()



# Drag and drop

el = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()




# Moving between windows and frames

# to know the windowName, take a look at the js or link that opened it
# it may contains ' target="windowName" '

driver.switch_to_window("windowName")

# window handle alternative

for handle in driver.window_handles:
  driver.switch_to_window(handle)

# swing frame to frame (or into iframes)

driver.switch_to_frame("frameName")

# access subframes

driver.switch_to_frame("frameName.0.child")

# come back to the parent frame

driver.switch_to_default_content()




# Popup dialogs

alert = driver.switch_to_alert()




# Navigation : history and location

driver.forward()
driver.back()


# Cookies

cookie = {'name' : 'foo', 'value' : 'bar'}

# set the cookie (valid for the entire domain)

driver.add_cookie(cookie)

# Output all available cookies for the current URL

driver.get_cookies()





