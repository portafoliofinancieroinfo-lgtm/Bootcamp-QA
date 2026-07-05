# 🏆 Proyecto Final: Urban Grocers API - Pruebas de Kits

> **Proyecto destacado** — Suite de pruebas de API que encontró **3 bugs reales**,
> incluyendo un error crítico 500 en producción. Ejemplo de pensamiento QA de
> punta a punta: diseño de casos, ejecución, evidencia y reporte de defectos.

Este proyecto contiene una suite de pruebas automatizadas para validar la creación de "Kits" en la aplicación Urban Grocers. El objetivo principal es verificar el comportamiento del campo `name` bajo diferentes condiciones (límites de caracteres, tipos de datos y caracteres especiales).

## 🎯 Habilidades demostradas

- Diseño de casos de prueba por límites y equivalencia (0, 1, 511, 512 caracteres).
- Pruebas negativas orientadas a romper el sistema (caracteres especiales, tipos incorrectos, parámetros ausentes).
- Detección y documentación de un **bug crítico (Error 500)** con severidad y evidencia.
- Redacción de un reporte de resultados claro, apto para stakeholders no técnicos.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- `configuration.py`: Contiene la URL base del servidor y las rutas de los endpoints (`/api/v1/users/` y `/api/v1/kits/`).
- `data.py`: Diccionarios con los cuerpos de las solicitudes (payloads) y encabezados.
- `sender_stand_request.py`: Contiene las funciones que realizan las peticiones HTTP (POST) utilizando la librería `requests`.
- `create_kit_name_kit_test.py`: Suite de pruebas con 9 casos de prueba (positivos y negativos).
- `.gitignore`: Configuración para evitar subir archivos temporales de Python al repositorio.

## Instrucciones de Ejecución

1. **Requisitos**: Tener instalado Python 3.14 y las librerías `requests` y `pytest`.
2. **Configuración**: Actualiza la variable `URL_SERVICE` en el archivo `configuration.py` con la URL de tu servidor activo.
3. **Ejecutar pruebas**: Abre una terminal en la carpeta del proyecto y ejecuta:
   ```bash
   pytest create_kit_name_kit_test.py
   ```

## Casos de Prueba

| # | Caso de Prueba                    | Resultado | Observación del QA                                                    |
|---|-----------------------------------|-----------|-----------------------------------------------------------------------|
| 1 | 1 carácter permitido ("a")        | ✅ PASSED  | Comportamiento esperado (201).                                        |
| 2 | 511 caracteres permitidos         | ✅ PASSED  | Comportamiento esperado (201).                                        |
| 3 | 0 caracteres (vacío "")           | ❌ FAILED  | Error: El servidor creó el kit (201) en lugar de dar error (400).     |
| 4 | 512 caracteres (excede límite)    | ❌ FAILED  | Error: El servidor no validó el límite máximo (201).                  |
| 5 | Caracteres especiales ("№%@")     | ✅ PASSED  | Los símbolos se procesan correctamente.                               |
| 6 | Espacios en blanco (" A Aaa ")    | ✅ PASSED  | El sistema permite espacios intermedios y extremos.                   |
| 7 | Números como texto ("123")        | ✅ PASSED  | Aceptado correctamente como string.                                   |
| 8 | Parámetro name ausente/nulo       | ❌ FAILED  | Bug Crítico: El servidor lanza un Error 500 (Internal Server Error).  |
| 9 | Tipo de dato incorrecto (int 123) | ❌ FAILED  | Error: El servidor acepta números sin comillas (201).                 |

## Conclusion

Tras la ejecución de la suite de pruebas automatizadas, se han identificado hallazgos críticos que afectan la integridad de los datos en el módulo de creación de kits:

### 1. Inestabilidad del Servidor (Error 500)
El hallazgo más grave se presenta en el **Caso 8 (Parámetro ausente)**. El servidor responde con un código **500 Internal Server Error** en lugar de un **400 Bad Request**. Esto indica una falta en el backend, lo que provoca que el servidor "colapse" ante una solicitud mal formada.

### 2. Deficiencia en la Validación de Límites
El sistema **no respeta las reglas de la documentacion** sobre la longitud del nombre del kit:
* **Caso 3 (0 caracteres):** El servidor permite nombres vacíos (devuelve 201).
* **Caso 4 (512 caracteres):** El servidor acepta nombres que exceden el límite máximo permitido (devuelve 201).
Esto sugiere que no hay una validación de longitud en la API.

### 3. Permisividad en el Tipado de Datos
En el **Caso 9 (Tipo de dato número)**, el servidor acepta un valor entero (`123`) como válido para un campo que debería ser estrictamente una cadena de texto (`string`).

---
**Nota Final:** Se recomienda priorizar la corrección del **Error 500** y endurecer las validaciones de entrada en el backend para cumplir con los requisitos de negocio y mejorar la robustez de la aplicación.