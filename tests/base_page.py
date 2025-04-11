from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class base_page:

    # Metodo para la inicializacion de la pagina con el driver de Microsoft Edge y la url del SIGEI ACADEMICO
    def init_page():
        service = Service("C:/Users/Jorge Rayber Acosta/Desktop/Pruebas automaticas/driver/msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        driver.maximize_window()
        driver.get("https://sigeiacademico.itla.edu.do/")
        return driver
    
    # Metodo el cual gestiona la espera de que un elemento que es buscado por su ID sea cargado y haga click o no, 
    # ademas de hacer captura de pantalla despues del proceso.
    def element_ID(driver, isClick, id, text, screen):
        if(isClick):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, id))).click()
        else:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id))).send_keys(text)
            driver.save_screenshot(f"./results/{screen}.png")

    # Metodo el cual gestiona la espera de que un elemento que es buscado por su class sea cargado y haga click o no, 
    # ademas de hacer captura de pantalla despues del proceso.
    def element_class(driver, isClick, id, text, screen):
        if(isClick):
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, id))).click()
            driver.save_screenshot(f"./results/{screen}.png")
        else:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, id))).send_keys(text)
            driver.save_screenshot(f"./results/{screen}.png")
