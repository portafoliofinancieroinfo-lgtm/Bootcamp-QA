import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

title_element = driver.find_element(By.CSS_SELECTOR, ".auth-form__title")

print("Login form title:", title_element.text)

driver.quit()