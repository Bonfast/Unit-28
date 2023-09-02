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
