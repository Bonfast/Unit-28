# Тест-кейс 11: Просмотр пользовательского соглашения
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_11():
    driver.get("https://b2c.passport.rt.ru")
    agreement_link = driver.find_element_by_link_text("пользовательского соглашения")
    agreement_link.click()

test_case_11()
driver.quit()
        
-----------------------------------------------------------------------------------------------
# Тест-кейс 12: Регистрация нового аккаунта
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_12():
    driver.get("https://b2c.passport.rt.ru")
    registration_button = driver.find_element_by_link_text("Зарегистрироваться")
    registration_button.click()
   
    first_name_input = driver.find_element_by_name("firstName")
    first_name_input.send_keys("Имя")

    last_name_input = driver.find_element_by_name("lastName")
    last_name_input.send_keys("Фамилия")
    
    mobile_input = driver.find_element_by_id("address")
    mobile_input.send_keys("номер_телефона")

    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    password_confirm_input = driver.find_element_by_id("password-confirm")
    password_confirm_input.send_keys("пароль")
    
    register_button = driver.find_element_by_xpath("//button[text()='Зарегистрироваться']")
    register_button.click()

test_case_12()
driver.quit()

-----------------------------------------------------------------------------------------------
# Тест-кейс 13: Попытка регистрации с уже существующим адресом электронной почты
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_13():
    driver.get("https://b2c.passport.rt.ru")
    registration_button = driver.find_element_by_link_text("Зарегистрироваться")
    registration_button.click()
   
    first_name_input = driver.find_element_by_name("firstName")
    first_name_input.send_keys("Имя")

    last_name_input = driver.find_element_by_name("lastName")
    last_name_input.send_keys("Фамилия")
    
    mobile_input = driver.find_element_by_id("address")
    mobile_input.send_keys("уже_зарегестрированный_адрес_электронной_почты")

    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    password_confirm_input = driver.find_element_by_id("password-confirm")
    password_confirm_input.send_keys("пароль")
    
    register_button = driver.find_element_by_xpath("//button[text()='Зарегистрироваться']")
    register_button.click()

test_case_13()
driver.quit()

-----------------------------------------------------------------------------------------------
# Тест-кейс 14: Попытка регистрации с недостоверной информацией
from selenium import webdriver
driver = webdriver.Chrome()

def test_case_14():
    driver.get("https://b2c.passport.rt.ru")
    registration_button = driver.find_element_by_link_text("Зарегистрироваться")
    registration_button.click()
   
    first_name_input = driver.find_element_by_name("firstName")
    first_name_input.send_keys("ввод_цифр_в_поле_имя")

    last_name_input = driver.find_element_by_name("lastName")
    last_name_input.send_keys("ввод_цифр_в_поле_фамилия")
    
    mobile_input = driver.find_element_by_id("address")
    mobile_input.send_keys("номер_телефона")

    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    password_confirm_input = driver.find_element_by_id("password-confirm")
    password_confirm_input.send_keys("пароль")
    
    register_button = driver.find_element_by_xpath("//button[text()='Зарегистрироваться']")
    register_button.click()

test_case_14()
driver.quit()
