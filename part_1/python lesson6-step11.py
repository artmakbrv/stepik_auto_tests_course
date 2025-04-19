from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    input1 = driver.find_element("xpath", "//input[@placeholder='Input your first name']")
    input1.send_keys("Ivan")
    input2 = driver.find_element("xpath", "//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = driver.find_element("xpath", "//input[@placeholder='Input your email']")
    input3.send_keys("Smolensk@ya.ru")
    input4 = driver.find_element("xpath", "//input[@placeholder='Input your phone:']")
    input4.send_keys("+79121112233")
    input5 = driver.find_element("xpath", "//input[@placeholder='Input your address:']")
    input5.send_keys("Russia, Tyumen")
    button = driver.find_element("xpath", "//input[@placeholder='Input your first name']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
