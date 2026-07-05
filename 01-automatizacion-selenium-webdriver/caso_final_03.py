from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin")
driver.implicitly_wait(10)

# Iniciar sesión
driver.find_element(By.ID, "email").send_keys("Tucorreo@gmail.com")
driver.find_element(By.ID, "password").send_keys("MiPassword123")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 3).until(
    expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, "places__list")))

# Buscar la tarjeta y desplazarla a la vista
tarjeta = driver.find_element(By.CSS_SELECTOR, ".places__item")
driver.execute_script("arguments[0].scrollIntoView();", tarjeta)
driver.implicitly_wait(5)

driver.quit()