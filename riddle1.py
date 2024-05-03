import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://techstepacademy.com/trial-of-the-stones")
driver.find_element(By.CSS_SELECTOR,'input[id="r1Input"]').send_keys("rock")
driver.find_element(By.XPATH,"//button[@id='r1Btn']").click()

hidden_elem=driver.find_element(By.XPATH,"//div[@id='passwordBanner']//h4")
print(hidden_elem.text)

driver.find_element(By.CSS_SELECTOR,'input[id="r2Input"]').send_keys(hidden_elem.text)
driver.find_element(By.XPATH,"//button[@id='r2Butn']").click()

richest_merchant=driver.find_element(By.XPATH,"//p[text()='3000']/../span")
print(richest_merchant.text)
driver.find_element(By.CSS_SELECTOR,'input[id="r3Input"]').send_keys(richest_merchant.text)
driver.find_element(By.XPATH,"//button[@id='r3Butn']").click()

driver.find_element(By.XPATH,"//button[@id='checkButn']").click()

success_message=driver.find_element(By.XPATH,"//h4[text()='Trial Complete']")

assert success_message.text == "Trial Complete"
driver.close()

time.sleep(5)

