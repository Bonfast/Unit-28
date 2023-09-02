# Тест-кейса 1: Авторизация через мобильный телефон и пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_1():
    driver.get("https://b2c.passport.rt.ru")
    
    phone_tab = driver.find_element_by_id("t-btn-tab-phone")
    phone_tab.click()
    
    mobile_input = driver.find_element_by_id("username")
    mobile_input.send_keys("номер_телефона")
    
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_1()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 2: Авторизация через мобильный телефон и неправильный пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_2():
    driver.get("https://b2c.passport.rt.ru")
    
    phone_tab = driver.find_element_by_id("t-btn-tab-phone")
    phone_tab.click()
    
    mobile_input = driver.find_element_by_id("username")
    mobile_input.send_keys("номер_телефона")
    
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("неправильный_пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_2()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 3: Авторизация через электронную почту и пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_3():
    driver.get("https://b2c.passport.rt.ru")
    
    email_tab = driver.find_element_by_id("t-btn-tab-mail")
    email_tab.click()
 
    email_input = driver.find_element_by_id("username")
    email_input.send_keys("адрес_почты")
  
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_3()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 4: Авторизация через электронную почту и неправильный пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_4():
    driver.get("https://b2c.passport.rt.ru")
    
    email_tab = driver.find_element_by_id("t-btn-tab-mail")
    email_tab.click()
 
    email_input = driver.find_element_by_id("username")
    email_input.send_keys("адрес_почты")
  
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("неправильный_пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_4()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 5: Авторизация через логин и пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_5():
    driver.get("https://b2c.passport.rt.ru")
    
    login_tab = driver.find_element_by_id("t-btn-tab-login")
    login_tab.click()

    login_input = driver.find_element_by_id("username")
    login_input.send_keys("логин")
  
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_5()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 6: Авторизация через логин и неправильный пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_6():
    driver.get("https://b2c.passport.rt.ru")
    
    login_tab = driver.find_element_by_id("t-btn-tab-login")
    login_tab.click()

    login_input = driver.find_element_by_id("username")
    login_input.send_keys("логин")
  
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("неправильный_пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_6()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 7: Авторизация через лицевой счет и пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_7():
    driver.get("https://b2c.passport.rt.ru")
    
    account_tab = driver.find_element_by_id("t-btn-tab-ls")
    account_tab.click()
 
    account_input = driver.find_element_by_id("username")
    account_input.send_keys("лицевой_счет")
    
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_7()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 8: Авторизация через лицевой счет и неправильный пароль
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_8():
    driver.get("https://b2c.passport.rt.ru")
    
    account_tab = driver.find_element_by_id("t-btn-tab-ls")
    account_tab.click()
 
    account_input = driver.find_element_by_id("username")
    account_input.send_keys("лицевой_счет")
    
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("неправильный_пароль")
    
    login_button = driver.find_element_by_id("kc-login")
    login_button.click()

test_case_8()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 9: Восстановление пароля через кнопку "Забыл пароль"
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_9():
    driver.get("https://b2c.passport.rt.ru")
    forgot_password_link = driver.find_element_by_id("forgot_password")
    forgot_password_link.click()
    
    phone_input = driver.find_element_by_id("username")
    phone_input.send_keys("номер_телефона")
    
    captcha_input = driver.find_element_by_id("captcha")
    captcha_input.send_keys("код_капчи")
    
    continue_button = driver.find_element_by_id("reset")
    continue_button.click()

test_case_9()
driver.quit()

-----------------------------------------------------------------------------------------------

# Тест-кейс 10: Восстановление пароля через настройки, уже авторизованным пользователем
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_10():
    driver.get("https://b2c.passport.rt.ru")
    
    lk_button = driver.find_element_by_id("lk-btn")
    lk_button.click()
  
    edit_button = driver.find_element_by_id("user_contacts_edit")
    edit_button.click()
    
    current_password_input = driver.find_element_by_id("current_password")
    current_password_input.send_keys("текущий_пароль")
    
    new_password_input = driver.find_element_by_id("new_password")
    new_password_input.send_keys("новый_пароль")

    confirm_password_input = driver.find_element_by_id("confirm_password")
    confirm_password_input.send_keys("новый_пароль")
    
    save_button = driver.find_element_by_id("password_save")
    save_button.click()

test_case_10()
driver.quit()
