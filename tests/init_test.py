from base_page import base_page
from sigei_test import sigei_test

# Inicia el navegador controlado por el selenium
driver = base_page.init_page()

# Metodo que inicia el test de login
def test_login():

    # Se llama el test de login
    sigei_test.test_login(driver)

# Metodo que inicia el test de inscripcion
def test_inscription():

    # Se llama el test de inscripcion
    sigei_test.test_inscription(driver)

# Metodo que inicia el test de datos generales
def test_his_student():

    # Se llama el test de datos generales
    sigei_test.test_his_student(driver)

# Metodo que inicia el test de calificaciones
def test_ratings():

    # Se llama el test de calificaciones
    sigei_test.test_ratings(driver)

# Metodo que inicia el test de reservas
def test_reserved_tickets():

    # Se llama el test de reservas
    sigei_test.test_reserved_tickets(driver)