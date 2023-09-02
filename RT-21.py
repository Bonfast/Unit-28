# Тест-кейс 21: Попытка восстановления пароля с неверными данными
from selenium import webdriver

def test_case_21():
    try:
        driver = webdriver.Chrome()
        driver.get("https://b2c.passport.rt.ru")

        forgot_password_link = driver.find_element_by_link_text("Забыл пароль")
        forgot_password_link.click()

        mobile_input = driver.find_element_by_id("username")
        mobile_input.send_keys("неверный_номер_телефона")

        captcha_input = driver.find_element_by_id("captcha")
        captcha_input.send_keys("код_капчи")

        continue_button = driver.find_element_by_xpath("//button[text()='Продолжить']")
        continue_button.click()

        error_message = driver.find_element_by_class_name("error-message")
        assert error_message.is_displayed(), "Сообщение об ошибке не появилось"

    finally:
        driver.quit()

test_case_21()
