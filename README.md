# SIGEI ACADEMICO [TESTS CASES]
Este es un proyecto para la tarea 4 de programación 3 con Kelyn Tejada.

SIGEI ACADEMICO es una aplicación web el cual ayuda al estudiante del ITLA a consultar y solicitar diferentes servicios, que van desde la consulta de la última inscripción, hasta la reserva de tickets para el transporte.

Este repositorio está dirigido más para las pruebas automatizadas que se le hacen a esta aplicación web, el cual, compruebas algunas de las funcionalidades fundamentales de este.

## Tests

- Inicio de sesión.
- Últimas Calificaciones.
- Últimas Inscripciones.
- Datos Generales.
- Reservas de tickets.

## Librerías 
- Selenium.
- Pytest.
- Pytest-html.

## Driver del navegador
- msedgedriver "135.0.3179.66"
 
## Ejecución de las pruebas  

**1. Clonar el repositorio:**  
```
git clone https://github.com/Raybelino/SIGEI-ACADEMICO-TESTS-CASES.git
```
**2. Iniciamos los tests:**

Se inicia ejecutando el siguiente comando en la terminal:
```
python -m pytest init_test.py --html=../report/report.html
```

> [!NOTE]
> Asegurate de estar en el directorio:
`
C:\...\SIGEI-ACADEMICO--TESTS-CASES-\tests>
`
