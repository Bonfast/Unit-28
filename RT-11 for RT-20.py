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
    registration_button = driver.find_element_by_xpath("//button[contains(text(),'Зарегистрироваться')]")
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

-----------------------------------------------------------------------------------------------

# Тест-кейс 15: Проверка отображения элементов на странице
from selenium import webdriver

def test_case_15():
    try:
        driver = webdriver.Chrome(executable_path="путь_к_вашему_драйверу")
        
        driver.get("https://b2c.passport.rt.ru")
        
        mobile_input = driver.find_element_by_id("username")
        assert mobile_input.is_displayed(), "Поле ввода мобильного телефона не отображается"
        
        password_input = driver.find_element_by_id("password")
        assert password_input.is_displayed(), "Поле ввода пароля не отображается"
   
        login_button = driver.find_element_by_id("kc-login")
        assert login_button.is_displayed(), "Кнопка 'Войти' не отображается"
        
        agreement_link = driver.find_element_by_link_text("пользовательского соглашения")
        assert agreement_link.is_displayed(), "Ссылка 'ознакомиться с пользовательским соглашением' не отображается"
        
        registration_button = driver.find_element_by_id("kc-register")
        assert registration_button.is_displayed(), "Ссылка 'Зарегистрироваться' не отображается"
        
        print("Все необходимые элементы отображаются на странице.")
        
    finally:
        driver.quit()
        
test_case_15()

-----------------------------------------------------------------------------------------------

# Тест-кейс 16: Проверка переходов по ссылкам (авторизация через соц. сети)
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
def test_case_16():
    try:
        driver.get("https://b2c.passport.rt.ru")
        links = driver.find_elements(By.TAG_NAME, "a")
        errors = []

        for link in links:
            link_url = link.get_attribute("href")
            if link_url and link_url.startswith("http"):
                try:
                    link.click()

                except WebDriverException as e:
                    errors.append(f"Ошибка при переходе по ссылке: {link_url} - {str(e)}")

        if not errors:
            print("Все переходы по ссылкам прошли успешно.")
        else:
            print("Ошибки при переходе по следующим ссылкам:")
            for error in errors:
                print(error)

    finally:
        driver.quit()

test_case_16()

-----------------------------------------------------------------------------------------------

# Тест-кейс 17: Проверка работоспособности кнопок
from selenium import webdriver

def test_case_17():
    try:
        driver = webdriver.Chrome()
        driver.get("https://b2c.passport.rt.ru")

        buttons = driver.find_elements_by_tag_name("button")

        for button in buttons:
            button.click()

        # Кнопка 1 - Телефон
        phone_button = driver.find_element_by_id("t-btn-tab-phone")
        phone_button.click()
        
        # Кнопка 2 - Почта
        mail_button = driver.find_element_by_id("t-btn-tab-mail")
        mail_button.click()
        
        # Кнопка 3 - Логин (активная)
        login_button_active = driver.find_element_by_xpath("//div[@id='t-btn-tab-login' and not(contains(@class, 'rt-tab--active'))]")
        login_button_active.click()
        
        # Кнопка 4 - Логин (неактивная)
        login_button_inactive = driver.find_element_by_xpath("//div[@id='t-btn-tab-login' and contains(@class, 'rt-tab--active')]")
        login_button_inactive.click()
        
        # Кнопка 5 - Войти
        login_button = driver.find_element_by_id("kc-login")
        login_button.click()

    finally:
        driver.quit()

test_case_17()

-----------------------------------------------------------------------------------------------

# Тест-кейс 18: Проверка обязательных полей на пустое значение
from selenium import webdriver

def test_case_18():
    try:
        driver = webdriver.Chrome()
        driver.get("https://b2c.passport.rt.ru")
        
        username_input = driver.find_element_by_id("username")
        username_input.clear()
        password_input = driver.find_element_by_id("password")
        password_input.clear()
        
        login_button = driver.find_element_by_id("kc-login")
        login_button.click()
        
        error_messages = driver.find_elements_by_class_name("error-message")
        assert len(error_messages) > 0, "Сообщения об ошибках валидации не появились"

    finally:
        driver.quit()

test_case_18()

-----------------------------------------------------------------------------------------------

# Тест-кейс 19: Попытка авторизации с неверными учетными данными
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_case_19():
    try:
        driver = webdriver.Chrome()
        driver.get("https://b2c.passport.rt.ru")

        username_input = driver.find_element_by_id("username")
        username_input.clear()
        username_input.send_keys("неправильный_формат_телефона")
        
        password_input = driver.find_element_by_id("password")
        password_input.clear()
        password_input.send_keys("пароль")
        
        login_button = driver.find_element_by_id("kc-login")
        login_button.click()

        error_messages = driver.find_elements_by_class_name("error-message")
        assert len(error_messages) > 0, "Сообщения об ошибках валидации не появились"

    finally:
        driver.quit()

test_case_19()

-----------------------------------------------------------------------------------------------

# Тест-кейс 20: Проверка длины и формата пароля при регистрации
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_case_20():
    try:
        driver = webdriver.Chrome()
        driver.get("https://b2c.passport.rt.ru")

        registration_button = driver.find_element_by_link_text("Зарегистрироваться")
        registration_button.click()

        first_name_input = driver.find_element_by_name("firstName")
        first_name_input.send_keys("Имя")

        last_name_input = driver.find_element_by_name("lastName")
        last_name_input.send_keys("Фамилия")

        mobile_input = driver.find_element_by_id("reg-phone")
        mobile_input.send_keys("номер_телефона")

        password_input = driver.find_element_by_id("reg-password")
        password_input.send_keys("короткий_пароль")

        password_confirm_input = driver.find_element_by_id("reg-password-confirm")
        password_confirm_input.send_keys("короткий_пароль")

        register_button = driver.find_element_by_xpath("//button[text()='Зарегистрироваться']")
        register_button.click()

        error_message = driver.find_element_by_xpath("//span[contains(text(), 'Длина пароля должны быть не менее 8 символов')]")
        assert error_message.is_displayed(), "Сообщение об ошибке не появилось"

    finally:
        driver.quit()

test_case_20()
