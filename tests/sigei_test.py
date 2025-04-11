from base_page import base_page
from selenium.webdriver.common.by import By
import time

class sigei_test:

    # Metodo que es el test de login, el cual pone las credenciales y inicia seccion automatizamente
    def test_login(driver):
        base_page.element_ID(driver, False, "email", "jrayberacarvajal@gmail.com", "login/insert_user")
        base_page.element_ID(driver, False, "password", "Rayber 17725", "login/insert_password")
        base_page.element_ID(driver, True, "btnLogin", "", "")
        time.sleep(7)
        assert "PERFIL" in driver.page_source
        driver.save_screenshot("./results/login/lobby.png")
        base_page.element_class(driver, True, "btn.btn-danger.px-10.btn-pill.font-weight-bolder.mt-5.animate__animated.fadeInUp.align-items-center", "", "login/login")

    # Metodo que es el test de inscripciones, el cual pone las credenciales y inicia seccion automatizamente 
    # y va a la seccion de inscripcion automaticamente para comprobar la carga de este.
    def test_inscription(driver):
        base_page.element_ID(driver, False, "email", "jrayberacarvajal@gmail.com", "inscription/insert_user")
        base_page.element_ID(driver, False, "password", "Rayber 17725", "inscription/insert_password")
        base_page.element_ID(driver, True, "btnLogin", "", "")
        time.sleep(3)
        driver.save_screenshot("./results/inscription/lobby.png")
        base_page.element_class(driver, True, "btn-lobby-container", "", "")
        time.sleep(15)
        driver.save_screenshot("./results/inscription/dashboard.png")
        driver.find_elements(By.CLASS_NAME, "nav-link")[3].click()
        time.sleep(4)
        assert "Última Inscripción" in driver.page_source
        driver.save_screenshot("./results/inscription/inscription.png")
        base_page.element_class(driver, True, "las.la-angle-left.icon-2x", "", "")
        base_page.element_class(driver, True, "btn.btn-danger.px-10.btn-pill.font-weight-bolder.mt-5.animate__animated.fadeInUp.align-items-center", "", "inscription/login")

    # Metodo que es el test de calificaciones, el cual pone las credenciales y inicia seccion automatizamente 
    # y va a la seccion de calificaciones automaticamente para comprobar la carga de este.
    def test_ratings(driver):
        base_page.element_ID(driver, False, "email", "jrayberacarvajal@gmail.com", "ratings/insert_user")
        base_page.element_ID(driver, False, "password", "Rayber 17725", "ratings/insert_password")
        base_page.element_ID(driver, True, "btnLogin", "", "")
        time.sleep(3)
        driver.save_screenshot("./results/ratings/lobby.png")
        base_page.element_class(driver, True, "btn-lobby-container", "", "")
        time.sleep(7)
        driver.save_screenshot("./results/ratings/dashboard.png")
        driver.find_elements(By.CLASS_NAME, "nav-link")[4].click()
        time.sleep(4)
        assert "Últimas Calificaciones" in driver.page_source
        driver.save_screenshot("./results/ratings/ratings.png")
        base_page.element_class(driver, True, "las.la-angle-left.icon-2x", "", "")
        base_page.element_class(driver, True, "btn.btn-danger.px-10.btn-pill.font-weight-bolder.mt-5.animate__animated.fadeInUp.align-items-center", "", "ratings/login")

    # Metodo que es el test de datos generales, el cual pone las credenciales y inicia seccion automatizamente 
    # y va a la seccion de historico estudiantil automaticamente para comprobar la carga de este.
    def test_his_student(driver):
        base_page.element_ID(driver, False, "email", "jrayberacarvajal@gmail.com", "his_student/insert_user")
        base_page.element_ID(driver, False, "password", "Rayber 17725", "his_student/insert_password")
        base_page.element_ID(driver, True, "btnLogin", "", "")
        time.sleep(3)
        driver.save_screenshot("./results/his_student/lobby.png")
        base_page.element_class(driver, True, "btn-lobby-container", "", "")
        time.sleep(7)
        driver.save_screenshot("./results/his_student/dashboard.png")
        driver.find_elements(By.CLASS_NAME, "nav-link")[2].click()
        time.sleep(4)
        assert "Datos Generales" in driver.page_source
        driver.save_screenshot("./results/his_student/his_student.png")
        base_page.element_class(driver, True, "las.la-angle-left.icon-2x", "", "")
        base_page.element_class(driver, True, "btn.btn-danger.px-10.btn-pill.font-weight-bolder.mt-5.animate__animated.fadeInUp.align-items-center", "", "his_student/login")

    # Metodo que es el test de reservas, el cual pone las credenciales y inicia seccion automatizamente 
    # y va a la seccion de reservas de tickets automaticamente para comprobar la carga de este.
    def test_reserved_tickets(driver):
        base_page.element_ID(driver, False, "email", "jrayberacarvajal@gmail.com", "reserved_tickets/insert_user")
        base_page.element_ID(driver, False, "password", "Rayber 17725", "reserved_tickets/insert_password")
        base_page.element_ID(driver, True, "btnLogin", "", "")
        time.sleep(3)
        driver.save_screenshot("./results/reserved_tickets/lobby.png")
        driver.find_elements(By.CLASS_NAME, "btn-lobby-container")[4].click()
        time.sleep(10)
        driver.save_screenshot("./results/reserved_tickets/dashboard.png")
        driver.find_elements(By.ID, "kt_aside_mobile_toggle")[2].click()
        time.sleep(2)
        assert "Tickets reservados" in driver.page_source
        driver.save_screenshot("./results/reserved_tickets/reserved_tickets.png")
        base_page.element_class(driver, True, "icon-button", "", "")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[h6[text()=' Volver al Lobby ']]").click()
        base_page.element_class(driver, True, "btn.btn-danger.px-10.btn-pill.font-weight-bolder.mt-5.animate__animated.fadeInUp.align-items-center", "", "reserved_tickets/login")