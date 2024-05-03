import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import os

# Set up WebDriver
driver = webdriver.Chrome()

# Open the webpage with file upload functionality
driver.get("https://demo.guru99.com/test/upload/")

# Find the file input element
upload_button = driver.find_element(By.ID,"uploadfile_0")
# upload_button.send_keys("C:\\Users\\AncyThomas\\Downloads\\sample4.csv")
upload_button.click()
# alert=driver.switch_to.alert
time.sleep(5)




# Close the WebDriver
driver.quit()