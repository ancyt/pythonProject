from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")

driver.implicitly_wait(20)
table=driver.find_element(By.ID,"customers")
rows=driver.find_element(By.XPATH,"//table/tbody/tr")
print(rows)
