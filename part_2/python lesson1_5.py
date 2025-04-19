from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

driver = webdriver.Chrome()
driver.get(link)

x_element = driver.find_element("xpath", "//*[@id='input_value']")
x = x_element.text
print(x)
input1 = driver.find_element("xpath", "//input[@id='answer']")
y = calc(x)
print(y)

input1.send_keys(y)

input2 = driver.find_element("xpath", "//input[@id='robotCheckbox']")
input2.click()

input3 = driver.find_element("xpath", "//input[@id='robotsRule']")
input3.click()

input4 = driver.find_element("xpath", "//button[@type='submit']")
input4.click()

time.sleep(3)
