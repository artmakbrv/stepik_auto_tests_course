from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажать на кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1] # Получаем дескриптор второй вкладки (индекс 1)
    browser.switch_to.window(new_window)  # Переключаемся на новую вкладку

    # Пройти капчу для робота
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()