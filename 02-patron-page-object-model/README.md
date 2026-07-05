# 🧩 Patrón Page Object Model (POM)

Automatización de pruebas web aplicando el patrón de diseño **Page Object
Model**, que separa la lógica de interacción con la página (localizadores y
acciones) de la lógica de las pruebas en sí.

## 🎯 Habilidades demostradas

- Diseño de clases "Page Object" que encapsulan localizadores y acciones de una página.
- Separación de responsabilidades: los tests solo orquestan llamadas a métodos de página, sin conocer detalles de implementación (localizadores, esperas).
- Uso de `WebDriverWait` + `expected_conditions` dentro de los métodos de página para sincronizar la ejecución.
- Estructura reutilizable y mantenible, escalable a suites de prueba más grandes.

## 📂 Contenido

| Archivo | Descripción |
|---|---|
| `ejemplo_uso_pom.py` | Ejemplo completo: clase de página `PageWeather` + clase de test que la consume. |
| `page_object_methods1.py` / `page_object_methods2.py` | Definición de métodos de página. |
| `page_object_practice_task1.py` / `page_object_practice_task2.py` | Ejercicios prácticos aplicando POM. |
| `page_object_registration_locator.py` | Localizadores para un flujo de registro. |

## 🛠️ Requisitos

- Python 3.10+
- Google Chrome instalado
- `pip install selenium pytest`

## ▶️ Ejecución

```bash
pytest ejemplo_uso_pom.py
```
