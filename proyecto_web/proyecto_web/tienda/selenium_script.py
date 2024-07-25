from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Ruta al controlador de ChromeDriver (ajusta según tu configuración)
CHROME_DRIVER_PATH = 'path/to/chromedriver'

# Configuración de Selenium (usando el navegador Chrome en este ejemplo)
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

# Abrir la página web local
driver.get('http://127.0.0.1:8000/api')  # Ajusta esta URL según sea necesario

# Esperar a que la página cargue completamente
time.sleep(5)  # Puedes ajustar el tiempo según sea necesario

# Obtener el elemento del selector
select_element = driver.find_element_by_id('api')

# Imprimir las opciones disponibles en el selector
for option in select_element.find_elements_by_tag_name('option'):
    print(f"Value: {option.get_attribute('value')}, Text: {option.text}")

# Cerrar el navegador
driver.quit()
