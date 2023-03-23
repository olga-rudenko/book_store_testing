## 97
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
# rememberme_checkbox = driver.find_element_by_id("rememberme").click()
# login_btn = driver.find_element_by_name("login").click()
# shop_tab = driver.find_element_by_link_text("Shop").click()
# book_mastering_forms = driver.find_element_by_class_name("post-181").click()
# book_title = driver.find_element_by_css_selector(".entry-title")
# book_title_text = book_title.text
# assert book_title_text == "HTML5 Forms"
# driver.quit()

## 98
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
# login_btn = driver.find_element_by_name("login").click()
# shop_tab = driver.find_element_by_link_text("Shop").click()
# html_tab = driver.find_element_by_link_text("HTML").click()
# html_books = driver.find_elements_by_css_selector(".attachment-shop_catalog.size-shop_catalog.wp-post-image")
# if len(html_books) == 3:
#     print("В каталоге три книги по HTML")
# else:
#     print("В каталоге другое количество книг")
    ## Второй способ проверки количества товара
# HTML_books = driver.find_elements_by_css_selector(".cat-item-19.current-cat >.count")
# HTML_books_text = books.text
# assert HTML_books_text == "(3)"

# 99
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
# login_btn = driver.find_element_by_name("login").click()
# shop_tab = driver.find_element_by_link_text("Shop").click()
# select = driver.find_element_by_class_name("orderby")
# ## Первый вариант ортировки по умолчанию
# #default = driver.find_element_by_css_selector("[value='menu_order']").click()
# ## Второй вариант сортировки по умолчанию
# #default_sorting = Select(select)
# #default_sorting.select_by_value("menu_order")
# ## Сортировка по цене от большей к меньшей
# price_high_to_low = Select(select)
# price_high_to_low.select_by_value("price-desc")
# select = driver.find_element_by_class_name("orderby")
# high_to_low = driver.find_element_by_css_selector('[value="price-desc"]')
# driver.quit()

## 100
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account").click()
# email_log = driver.find_element_by_id("username")
# email_log.send_keys("olya.rdnk@mail.ru")
# password_log = driver.find_element_by_id("password")
# password_log.send_keys("Strong007^!")
# login_btn = driver.find_element_by_name("login").click()
# shop_tab = driver.find_element_by_link_text("Shop").click()
# android_quick_book = driver.find_element_by_css_selector(".post-169").click()
# price_book_first = driver.find_element_by_css_selector("p > del > span")
# price_book_first_text = price_book_first.text
# assert price_book_first_text == "₹600.00"
# price_book_second = driver.find_element_by_css_selector("p > ins > span")
# price_book_second_text = price_book_second.text
# assert price_book_second_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".images"))).click()
# book_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".pp_close"))).click()
# driver.quit()

## 101
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# tab_shop = driver.find_element_by_id("menu-item-40").click()
# book_java_script = driver.find_element_by_css_selector('[data-product_id="165"]').click()
# # cart_book = driver.find_element_by_css_selector(".cartcontents")
# # cart_book_text = cart_book.text
# # assert cart_book_text == "1 item"
# # cart_book_price = driver.find_element_by_css_selector(".wpmenucart-contents >.amount")
# # cart_book_price_text = cart_book_price.text
# # assert cart_book_price_text == "₹350.00"
# time.sleep(5)
# cart = driver.find_element_by_class_name("wpmenucart-contents").click()
# subtotal = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal']"), "₹350.00"))
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total"), "₹357.00"))
#driver.quit()

## 102
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# tab_shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_java_script = driver.find_element_by_css_selector('[data-product_id="165"]').click()
# time.sleep(5)
# book_java_script = driver.find_element_by_css_selector('[data-product_id="165"]').click()
# cart = driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(3)
# remove = driver.find_element_by_class_name("remove").click()
# undo = driver.find_element_by_link_text("Undo?").click()
# quantity = driver.find_element_by_css_selector('[title="Qty"]')
# quantity.clear()
# time.sleep(3)
# quantity.send_keys("3")
# update_basket = driver.find_element_by_css_selector('[value="Update Basket"]').click()
# quan_tity = driver.find_element_by_css_selector('[type="number"]')
# # quan_tity_text = quan_tity.text
# # assert quan_tity_text == "3"
# time.sleep(3)
# apply_coupon = driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# error_code = driver.find_element_by_class_name("woocommerce-error")
# error_code_text = error_code.text
# assert error_code_text == "Please enter a coupon code."
# driver.quit()

## 103

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://practice.automationtesting.in/")
# tab_shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_java_script = driver.find_element_by_css_selector('[data-product_id="165"]').click()
# time.sleep(3)
# cart = driver.find_element_by_class_name("wpmenucart-contents").click()
# checkout_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button"))).click()
# first_name = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '[for="billing_first_name"]')))
# first_name.click()
# first_name_value = driver.find_element_by_id("billing_first_name")
# first_name_value.send_keys("Olga")
# last_name = driver.find_element_by_id("billing_last_name").click()
# last_name_value = driver.find_element_by_id("billing_last_name")
# last_name_value.send_keys("Rudenko")
# email = driver.find_element_by_css_selector('[for="billing_email"]').click()
# email_value = driver.find_element_by_id("billing_email")
# email_value.send_keys("rdnk@mail.ru")
# phone = driver.find_element_by_css_selector('[for="billing_phone"]').click()
# phone_value = driver.find_element_by_id("billing_phone")
# phone_value.send_keys("034578933")
# country = driver.find_element_by_id("s2id_billing_country").click()
# country_value = driver.find_element_by_id("s2id_autogen1_search")
# country_value.send_keys("Argentina")
# country_argentina = driver.find_element_by_class_name("select2-match").click()
# address = driver.find_element_by_css_selector('[for="billing_address_1"]').click()
# address_value = driver.find_element_by_id("billing_address_1")
# address_value.send_keys("Buenos Aires, Capital Federal, 145/98")
# city = driver.find_element_by_css_selector('[for="billing_city"]').click()
# city_value = driver.find_element_by_id("billing_city")
# city_value.send_keys("Buenos Aires")
#
# billing_state_value = driver.find_element_by_id("select2-chosen-2").click()
# billing_state_ba = driver.find_element_by_id("s2id_autogen2_search")
# billing_state_ba.send_keys("Buenos Aires")
# billing_state = driver.find_element_by_css_selector("[value='B']")#.click()
# #billing_check = WebDriverWait(driver, 10).until(
#     #EC.element_to_be_clickable((By.ID, "createaccount")))
# # billing_check = driver.find_elements_by_css_selector('[name="createaccount"]')
# # #billing_check.click() #Не удается нажать на строчку, чтобы определить код строки (получается наложение) не смогла справится
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys("657890")
# ## 7 шаг
# driver.execute_script("window.scrollBy(0, 600);")
# # payment_cheque = WebDriverWait(driver, 20).until(
# #     EC.element_to_be_clickable((By.CSS_SELECTOR, '[value="cheque"]')))
# payment_check = driver.find_element_by_id("payment_method_cheque")
# #payment_check.click()
# ## 8 шаг
# place_order = driver.find_element_by_id("place_order").click()
#
# ## 9 шаг
#
# thank_you = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
#
# ## 10 шаг
#
# payment_method = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.LINK_TEXT, "Payment Method:"), 'Check Payments'))





























