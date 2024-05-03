from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Open the webpage with file download link/button
driver.get("https://filesamples.com/formats/csv")

# Click on the download link/button
download_button = driver.find_element(By.XPATH,'//a[@href="/samples/document/csv/sample4.csv"]')
download_button.click()

# Wait for the file to download
time.sleep(5)  # Wait for 5 seconds (adjust as needed)

# Verify the file has been downloaded
download_directory = "C:\\Users\\AncyThomas\\Downloads\\"
downloaded_file_path = os.path.join(download_directory, "sample4.csv")

# Check if the file exists
if os.path.exists(downloaded_file_path):
    print("File has been downloaded successfully.")
else:
    print("File download failed.")

# Close the WebDriver
driver.quit()
