# 🔌 Urban Grocers — Pruebas de API con Postman

Pruebas manuales de la API REST de *Urban Grocers* ejecutadas con **Postman**:
36 casos de prueba sobre tres endpoints, con **14 defectos documentados en
Jira** (proyecto `BD4CG4OS`), incluidos **errores 500 del servidor** ante
entradas inválidas.

## Endpoints probados

| Endpoint | Casos | Enfoque |
|---|---|---|
| `POST /everything-you-need/v1/calculate` | 5 | Disponibilidad de producto y validación de `deliveryTime` contra el horario laboral |
| `POST /api/v1/kits/:id/products` | 17 | Límite de 30 productos por kit, tipos de dato, IDs inexistentes/negativos/cero, JSON malformado |
| `POST /order-and-go/v1/delivery` | 19 | Reglas de negocio de entrega (`deliveryTime`, `productsCount`, `productsWeight`) por valores límite |

## Hallazgos principales

Los reportes completos están en [BUG_REPORTS.md](./BUG_REPORTS.md).

1. **Errores 500 en lugar de 400 (crítico):** enviar `deliveryTime` fuera de rango o un `id`/`quantity` de tipo string provoca `500 Internal Server Error` con mensajes internos expuestos (`"Invalid cast of deliveryTime property"`), en lugar de un `400 Bad Request` controlado.
2. **El límite de 30 productos por kit se puede evadir:** la validación funciona al enviar 31 productos en una sola solicitud, pero **no** al superar el límite acumulando solicitudes sucesivas (PK-16).
3. **La regla de negocio de entrega no se aplica:** `isItPossibleToDeliver` devuelve `True` incluso con horario fuera de rango, cantidad de productos superior al máximo, peso excedido o valores negativos (PE-2 a PE-13).
4. **Datos sin sanear:** se aceptan IDs negativos, ID 0, IDs inexistentes, cantidades negativas y cuerpos que no son JSON válido, siempre con respuesta `200 OK`.

## Evidencia

- [`evidencia/pruebas_api_urban_grocers.xlsx`](./evidencia/pruebas_api_urban_grocers.xlsx) — casos de prueba completos con payloads, resultados esperados/obtenidos y enlaces a Jira.

> Este trabajo manual fue la base de la [suite automatizada de Urban Grocers](../../04-proyecto-final-urban-grocers-qa)
> desarrollada después con `requests` + `pytest`.
