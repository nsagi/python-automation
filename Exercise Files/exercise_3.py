from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Bhoomika/python-automation/Exercise%20Files/html_code_01.html")
login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
login_form_relative = driver.find_element_by_xpath("//form[1]")
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']")
print("My login form is:")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)
driver.close()
