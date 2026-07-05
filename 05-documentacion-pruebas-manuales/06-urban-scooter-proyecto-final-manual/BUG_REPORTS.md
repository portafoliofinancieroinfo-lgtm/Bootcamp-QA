# 🐞 Informes de errores — Urban Scooter

Defectos encontrados durante el proyecto final, gestionados originalmente en
Jira (proyecto `KAN`).

## Aplicación web

---

### KAN-5 — La cadena de estados del pedido no avanza (bloqueante)

- **Severidad:** 🔴 Crítico / Bloqueante
- **Impacto:** bloqueó 9 comprobaciones del checklist de "Estado del pedido".

**Descripción:** los estados del pedido ("El scooter está en el almacén",
"El repartidor está en camino", "El servicio de entrega llegó", "Bien, vamos a
dar un paseo", "El periodo de alquiler terminó") no se actualizan al avanzar el
flujo, por lo que no fue posible verificar la cadena de estados, la
desactivación del botón "Cancelar el pedido" ni la visibilidad del pedido
cancelado.

---

### KAN-6 — El calendario permite seleccionar la fecha actual y fechas pasadas

- **Severidad:** 🟠 Grave

**Resultado esperado:** el calendario de "Fecha de entrega" solo permite fechas a partir del día siguiente.

**Resultado actual:** se pueden seleccionar la fecha actual y fechas anteriores.

---

### KAN-7 — El campo de fecha acepta entrada manual

- **Severidad:** 🟡 Menor

**Resultado esperado:** la fecha solo puede elegirse desde el calendario desplegable.

**Resultado actual:** el campo permite escribir la fecha manualmente, evadiendo las restricciones del calendario.

---

### KAN-8 — El campo "Comentario" acepta más de 24 caracteres

- **Severidad:** 🟡 Menor

**Resultado esperado:** máximo 24 caracteres.

**Resultado actual:** se aceptan textos de 25+ caracteres sin error.

---

### KAN-9 — El campo "Comentario" acepta caracteres no permitidos

- **Severidad:** 🟡 Menor

**Resultado esperado:** solo letras latinas, números, guiones, puntos y comas.

**Resultado actual:** se aceptan símbolos especiales (`@#$%`, `¿?`, `¡!`).

---

### KAN-4 — Defecto de visualización en Chrome (pedido nº 51909)

- **Severidad:** 🟡 Menor

**Descripción:** comportamiento divergente del flujo "Estado del pedido" en
Google Chrome respecto a Opera, detectado durante las pruebas cross-browser.

## Aplicación móvil (app del repartidor)

---

### KAN-10 — La notificación push de vencimiento no se dispara

- **Severidad:** 🔴 Crítico
- **Entorno:** emulador Android Studio, Google Pixel 4 XL, Android 10

**Pasos para reproducir**
1. Iniciar sesión como repartidor con un pedido asignado que vence a las 11:59 p.m.
2. Esperar a que el reloj del sistema marque las 9:59 p.m. (2 horas antes) sin entregar el pedido.
3. Observar el dispositivo.

**Resultado esperado:** a las 9:59 p.m. se dispara una notificación push ("2 horas hasta el final del pedido").

**Resultado actual:** la notificación no se dispara. Este defecto bloqueó los casos CP-02 y CP-03 (contenido del mensaje y navegación al tocar la notificación).

## API

---

### KAN-11 — `POST /api/v1/courier` no valida el formato del campo `login`

- **Severidad:** 🟠 Grave

**Resultado esperado:** `400 Bad Request` para logins de 1 u 11 caracteres, con números, caracteres no latinos (ñ, á) o símbolos especiales.

**Resultado actual:** `201 Created` en todos los casos — el mensajero se crea con un login inválido.

---

### KAN-12 — `POST /api/v1/courier` no valida el formato del campo `password`

- **Severidad:** 🟠 Grave

**Resultado esperado:** `400 Bad Request` para contraseñas de 3 o 5 dígitos, o que contienen letras (regla: 4 dígitos).

**Resultado actual:** `201 Created` — se aceptan contraseñas fuera de regla.

---

### KAN-13 — `POST /api/v1/courier` no valida el formato del campo `firstName`

- **Severidad:** 🟡 Menor

**Resultado esperado:** `400 Bad Request` para nombres de 1 u 11 caracteres o con números.

**Resultado actual:** `201 Created` — se aceptan nombres fuera de regla.

---

### KAN-14 — `DELETE /api/v1/courier/:id` con ID no numérico devuelve el error incorrecto

- **Severidad:** 🟡 Menor

**Resultado esperado:** `400 Bad Request` cuando el ID contiene letras (`/api/v1/courier/abc`).

**Resultado actual:** la API responde con un código/mensaje incorrecto en lugar del 400 esperado.
