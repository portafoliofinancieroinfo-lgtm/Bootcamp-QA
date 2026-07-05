# 🔌 Pruebas de API con Python (Requests + Pytest)

Suite de pruebas automatizadas para un endpoint de creación de usuarios,
enfocada en validar reglas de negocio sobre el campo `firstName` mediante
casos positivos y negativos.

## 🎯 Habilidades demostradas

- Diseño de casos de prueba por **partición de equivalencia y valores límite**
  (2, 15, 1 y 16 caracteres en el nombre).
- Pruebas **positivas** (respuesta `201`, token generado, alta visible en el
  listado de usuarios) y **negativas** (respuesta `400` con mensaje de error esperado).
- Validación de reglas de formato: caracteres especiales, espacios, dígitos,
  parámetro ausente y tipos de dato incorrectos.
- Separación de responsabilidades en capas: `data.py` (payloads), `configuration.py`
  (endpoints), `sender_stand_request.py` (cliente HTTP), `create_user_test.py` (casos de prueba).

## 📂 Contenido

| Archivo | Descripción |
|---|---|
| `configuration.py` | URL base y rutas de los endpoints. |
| `data.py` | Payloads y headers de las solicitudes. |
| `sender_stand_request.py` | Funciones que ejecutan las peticiones HTTP con `requests`. |
| `create_user_test.py` | 10 casos de prueba (positivos y negativos) sobre el alta de usuarios. |

## 🛠️ Requisitos

- Python 3.10+
- `pip install requests pytest`

## ▶️ Ejecución

1. Actualiza `URL_SERVICE` en `configuration.py` con la URL de tu servidor activo.
2. Ejecuta las pruebas:

```bash
pytest create_user_test.py
```
