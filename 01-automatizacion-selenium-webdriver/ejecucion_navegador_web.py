from selenium import webdriver

#Objeto de la configuración
chrome_options = webdriver.ChromeOptions()
#Ejecuta el navegador desde la terminal
chrome_options.add_argument('--headless')
# Ajusta el tamaño de la ventana a 640 x 480 píxeles
chrome_options.add_argument('--window-size=640,480')
# Crea un controlador y pasa la configuración de los ajustes establecidos
driver = webdriver.Chrome(options=chrome_options)

# Abrir una página
driver.get('https://www.google.com/')
#Guarda y verifica la URL
assert driver.current_url == 'https://www.google.com/'
#Verífica solo una parte del URL
assert 'google.com' in driver.current_url
# Cierra la página
driver.quit()