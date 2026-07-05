from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# Se crea espera explícita para todas las interacciones
wait = WebDriverWait(driver, 10)

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Espera de la página hasta que le objeto correo electrónico esté presente para ingresarlo
wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("Tucorreo@gmail.com")

# Espera de la página hasta que el campo de contraseña esté presente para ingresarla
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("MiPassword123")

# Espera de la página hasta que el botón de inicio de sesión sea clickable para ingresar
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".auth-form__button"))).click()

# Espera de la página hasta que la sección de usuario sea visible después de iniciar sesión
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header__user")))

# Espera de la página hasta para obtener el botón de cierre de sesión y verificar que su texto sea 'Log out'
logout_text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header__logout"))).text
assert logout_text.strip() == 'Cerrar sesión', f"Se esperaba 'Cerrar sesión', pero se obtuvo '{logout_text}'"

driver.quit()