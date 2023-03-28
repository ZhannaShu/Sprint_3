# проверка регистрации
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# ожидание появления кнопки Войти в аккаунт
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0")))

driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

# ожидание появления Зарегистрироваться
WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[1]/a[text()='Зарегистрироваться']")))

driver.find_element(By.XPATH, "//p[1]/a[text()='Зарегистрироваться']").click()

# ожидание появления кнопки Зарегистрироваться
WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Зарегистрироваться']")))

driver.find_element(By.XPATH, "//fieldset[1]/div/div/input").send_keys('Zanna') # ввести имя в поле Имя

driver.find_element(By.XPATH, "//fieldset[2]/div/div/input").send_keys('Zanna_Shuvalova_8777@yandex.ru') # ввести Email

driver.find_element(By.XPATH, "//input[@type='password']").send_keys(123456)  #  ввести пароль

driver.find_element(By.XPATH, "//form/button[text()='Зарегистрироваться']").click()  #  клик по кнопке Зарегистрироваться

WebDriverWait(driver, 3).until()

time.sleep(5)

# Проверка на некорректный пароль (ошибка)























#password_length = 6

#driver.find_element(By.XPATH, "//input[@type='password']").send_keys(123456)
#driver.find_element(By.XPATH, "//input[@type='password']").clear()
#driver.find_element(By.TAG_NAME, 'input').clear()
#elm = driver.find_element(By.XPATH, "//input[@type='password']")
#elm.send_keys(12345)
#assert len(elm.get_attribute('value')) != password_length

#time.sleep(5)

driver.quit()





