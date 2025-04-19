from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Посчитать математическую функцию от x
    y = calc(x)

    # Найти текстовое поле, checkbox и radiobutton
    answer_field = browser.find_element(By.ID, "answer")
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robots_radio = browser.find_element(By.ID, "robotsRule")
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")


    # Проскроллить страницу вниз (используем execute_script)
    browser.execute_script("window.scrollBy(0, 150);")

    # Ввести ответ в текстовое поле
    answer_field.send_keys(y)

    # Выбрать checkbox "I'm the robot"
    robot_checkbox.click()

    # Переключить radiobutton "Robots rule!"
    robots_radio.click()

    # Нажать на кнопку "Submit"
    submit_button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    