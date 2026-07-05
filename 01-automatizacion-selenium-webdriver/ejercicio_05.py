import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
time.sleep(2)

# Buscar el campo Correo electrónico y rellenarlo
Email = driver.find_element(By.ID, "email")
Email.send_keys("Tucorreo@gmail.com")
# Buscar el campo Contraseña y rellenarlo
Password = driver.find_element(By.ID, "password")
Password.send_keys("MiPassword123")
time.sleep(2)

# Buscar el botón Iniciar sesión y hacer clic en él
Button = driver.find_element(By.CLASS_NAME, "auth-form__button")
Button.click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Comprobar que la URL actual es 'https://around-v1.nm.tripleten-services.com/'
assert driver.current_url == 'https://around-v1.nm.tripleten-services.com/'

driver.quit()