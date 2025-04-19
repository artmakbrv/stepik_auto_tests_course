from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")
for element in elements:
    element.send_keys("привет")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)

browser.quit()
