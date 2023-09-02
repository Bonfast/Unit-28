def test_case_11():
    driver.get("https://b2c.passport.rt.ru")
    registration_button = driver.find_element_by_link_text("Зарегистрироваться")
    registration_button.click()
    
    # Ввод имени
    first_name_input = driver.find_element_by_name("firstName")
    first_name_input.send_keys("Имя")
    
    # Ввод фамилии
    last_name_input = driver.find_element_by_name("lastName")
    last_name_input.send_keys("Фамилия")
    
    # Ввод номера мобильного телефона для регистрации
    mobile_input = driver.find_element_by_id("address")
    mobile_input.send_keys("номер_телефона")
    
    # Ввод пароля для регистрации
    password_input = driver.find_element_by_id("password")
    password_input.send_keys("пароль")
    
    # Ввод подтверждения пароля
    password_confirm_input = driver.find_element_by_id("password-confirm")
    password_confirm_input.send_keys("пароль")
    
    # Нажатие на кнопку "Зарегистрироваться"
    register_button = driver.find_element_by_xpath("//button[text()='Зарегистрироваться']")
    register_button.click()

