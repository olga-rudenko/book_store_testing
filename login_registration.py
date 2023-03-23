
# import time
# from selenium import webdriver
# driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
# driver.maximize_window()
# from selenium.webdriver.support.select import Select
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# email_reg = driver.find_element_by_id("reg_email")
# email_reg.send_keys("olya.rdnk@mail.ru")
# password_reg = driver.find_element_by_id("reg_password")
# password_reg.send_keys("Strong007^!")
# register = driver.find_element_by_name("register").click()
# driver.quit()

# import time
# from selenium import webdriver
# driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
# driver.maximize_window()
# from selenium.webdriver.support.select import Select
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# email_log = driver.find_element_by_id("username")
# email_log.send_keys("olya.rdnk@mail.ru")
# password_log = driver.find_element_by_id("password")
# password_log.send_keys("Strong007^!")
# #rememberme_checkbox = driver.find_element_by_id("rememberme").click()
# login_btn = driver.find_element_by_name("login").click()
# logout = driver.find_element_by_link_text("Logout")
# logout_text = logout.text
# assert logout_text == "Logout"
#driver.quit()