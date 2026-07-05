import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

class_element = driver.find_elements(By.XPATH, ".//img")
assert len(class_element) > 1, f"Found {len(class_element)} elements"

driver.quit()