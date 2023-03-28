#  проверка входа
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# ожидание появления кнопки Войти в аккаунт
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0")))

driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

# ожидание появления поля Email
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, ".//div[class='input pr-6 pl-6 input_type_text input_size_default']/input[name='name']")))

# ввести Email
name = driver.find_element(By.XPATH, ".//div[class='input pr-6 pl-6 input_type_text input_size_default']/input[name='name']")
name.send_keys('Zanna_Shuvalova_8777@yandex.ru')
#  ввести пароль
password = driver.find_element(By.XPATH, ".//div[class='input pr-6 pl-6 input_type_password input_size_default']/input[name='Пароль']")
password.send_keys('123456')
