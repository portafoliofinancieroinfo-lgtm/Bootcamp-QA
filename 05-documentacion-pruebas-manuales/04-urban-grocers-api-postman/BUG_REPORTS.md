# 🐞 Informes de errores — API Urban Grocers

Defectos encontrados con Postman sobre la API de Urban Grocers. Los IDs `BD4CG4OS-n`
corresponden a los tickets originales de Jira.

## Defectos destacados

---

### DEF-01 — `deliveryTime` fuera de rango provoca 500 Internal Server Error

- **Casos asociados:** TC02.1, TC03.01
- **Severidad:** 🔴 Crítico

**Pasos para reproducir**
1. Enviar `POST /everything-you-need/v1/calculate` con body `{"productId": 1, "quantity": 2, "deliveryTime": 2}` (o `24`).

**Resultado esperado:** `400 Bad Request` — la hora de entrega está fuera del rango `workingHours` (7–23).

**Resultado actual:** `500 Internal Server Error` con el mensaje interno `"Invalid cast of deliveryTime property"`. El servidor colapsa ante un dato de entrada inválido y expone detalles de implementación.

---

### DEF-02 — `id` de producto tipo string provoca 500 (BD4CG4OS-2)

- **Caso asociado:** PK-06
- **Severidad:** 🔴 Crítico

**Pasos para reproducir**
1. Enviar `POST /api/v1/kits/6/products` con `{"productsList": [{"id": "CP-03", "quantity": 1}]}`.

**Resultado esperado:** `400 Bad Request` por tipo de dato inválido.

**Resultado actual:** `500 Internal Server Error`. Mismo comportamiento con `quantity` string (PK-07, BD4CG4OS-8).

---

### DEF-03 — El límite de 30 productos por kit se evade con solicitudes acumuladas (BD4CG4OS-14)

- **Caso asociado:** PK-16
- **Severidad:** 🟠 Grave

**Pasos para reproducir**
1. Partir de un kit que ya está cerca del límite de 30 productos.
2. Enviar `POST /api/v1/kits/2/products` con una lista que, sumada al contenido existente, supera los 30 artículos.

**Resultado esperado:** `400 Bad Request` — "No más de 30 artículos por conjunto".

**Resultado actual:** `200 OK`; los productos se añaden y el kit supera el límite de negocio. La validación solo se aplica cuando el exceso llega en una sola solicitud (PK-01 sí la aplica).

---

### DEF-04 — La regla `isItPossibleToDeliver` no valida las restricciones de entrega (BD4CG4OS-16 a 24)

- **Casos asociados:** PE-2 a PE-7, PE-11 a PE-13
- **Severidad:** 🟠 Grave

**Pasos para reproducir**
1. Enviar `POST /order-and-go/v1/delivery` con cualquiera de estas combinaciones fuera de regla:
   - `deliveryTime` fuera del horario permitido (p. ej. `7`) o negativo (`-9`)
   - `productsCount` sobre el máximo (`16`) o negativo (`-9`)
   - `productsWeight` sobre el máximo (`7`, `10`) o negativo (`-5`)

**Resultado esperado:** `200 OK` con `isItPossibleToDeliver: False`.

**Resultado actual:** `200 OK` con `isItPossibleToDeliver: True` en todos los casos — el sistema aceptaría entregas imposibles según las reglas de negocio.

---

## Tabla completa de defectos

| Ticket | Caso | Descripción | Esperado | Obtenido |
|---|---|---|---|---|
| — | TC02.1 / TC03.01 | `deliveryTime` fuera de rango (2, 24) | 400 | **500** `"Invalid cast of deliveryTime property"` |
| BD4CG4OS-1 | PK-04 | `productsList` vacía se acepta | 400 | 200 |
| BD4CG4OS-2 | PK-06 | `id` de producto tipo string | 400 | **500** |
| BD4CG4OS-8 | PK-07 | `quantity` tipo string | 400 | **500** |
| BD4CG4OS-9 | PK-08 | `id` de producto negativo | 400 | 200 |
| BD4CG4OS-10 | PK-09 | `quantity` negativa se añade al kit | 400 | 200 (se añade) |
| BD4CG4OS-11 | PK-10 | `id` de producto = 0 | 400 | 200 |
| BD4CG4OS-12 | PK-11 | `quantity` = 0 se añade al kit | 400 | 200 (se añade) |
| BD4CG4OS-13 | PK-14 | `id` de producto inexistente (99999999) | 400 | 200 |
| BD4CG4OS-14 | PK-16 | Límite de 30 productos evadido por acumulación | 400 | 200 (se añaden) |
| BD4CG4OS-15 | PK-17 | Body con JSON inválido | 400 | 200 |
| BD4CG4OS-16/18 | PE-2, PE-5 | Entrega con `deliveryTime` fuera de horario | `False` | `True` |
| BD4CG4OS-17/21 | PE-3, PE-7 | Entrega con `productsWeight` excedido | `False` | `True` |
| BD4CG4OS-19/20 | PE-4, PE-6 | Entrega con `productsCount` excedido | `False` | `True` |
| BD4CG4OS-22/23/24 | PE-11 a PE-13 | Valores negativos en los tres campos | `False` | `True` |
