# 🕹️ Automatización Web con Selenium WebDriver

Ejercicios progresivos de automatización web en Python, desde la apertura de un
navegador controlado hasta la validación de contenido dinámico en páginas reales.

## 🎯 Habilidades demostradas

- Control de navegador con `webdriver.Chrome()` (modo normal y headless).
- Localización de elementos con `By.ID`, `By.XPATH`, `By.CLASS_NAME` y `By.CSS_SELECTOR`.
- Esperas explícitas con `WebDriverWait` y `expected_conditions` (evitando `sleep()` fijos).
- Interacción con formularios: `send_keys`, `click`, scroll a elementos con `execute_script`.
- Validaciones con `assert` sobre URL y contenido de la página.
- Cierre limpio de sesión del navegador con `driver.quit()`.

## 📂 Contenido

| Archivo | Descripción |
|---|---|
| `busqueda_elementos.py` | Prácticas de localización de elementos en el DOM. |
| `localizadores_by.py` | Ejemplos de las distintas estrategias de `By`. |
| `ejecucion_navegador_web.py` | Ejecución básica del navegador y navegación. |
| `ejercicio_01.py` … `ejercicio_07.py` | Ejercicios progresivos de práctica. |
| `caso_final_01.py` … `caso_final_03.py` | Casos finales de integración (login, espera de carga, scroll a tarjetas). |

## 🛠️ Requisitos

- Python 3.10+
- Google Chrome instalado
- `pip install selenium`

## ▶️ Ejecución

```bash
python caso_final_01.py
```
