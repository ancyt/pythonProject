import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
# driver.find_element(By.XPATH,'//a[text()="Register"]').click()
# driver.back()
# print(driver.title)
# print(driver.current_url)
driver.execute_script("alert('Hello, world!');")
alert=driver.switch_to.alert
alert.accept()
driver.find_element(By.XPATH,'//a[text()="Register"]').click()
driver.back()

# action=ActionChains(driver)
# element=driver.find_element(By.CSS_SELECTOR,'a[class="btn btn-theme btn-sm btn-min-block"]')
# action.context_click(element).perform()
time.sleep(10)







