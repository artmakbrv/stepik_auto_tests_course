from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    # Найти элементы с числами
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    # Получить значения чисел из текста элементов
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # Посчитать сумму
    sum_result = str(num1 + num2)

    # Найти выпадающий список
    select = Select(browser.find_element(By.TAG_NAME, "select"))

    # Выбрать значение в выпадающем списке, равное сумме
    select.select_by_value(sum_result)

    # Нажать кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()


finally:
    # Даем время скопировать код
    time.sleep(10)
    browser.quit()





from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()