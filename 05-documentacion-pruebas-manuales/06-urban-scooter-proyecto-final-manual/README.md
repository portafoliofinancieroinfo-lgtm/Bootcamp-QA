# 🛴 Urban Scooter — Proyecto final de pruebas manuales (Web + Móvil + API)

Proyecto final del bootcamp: pruebas integrales de la plataforma *Urban Scooter*
(alquiler de scooters con entrega a domicilio) cubriendo sus **tres capas** —
aplicación web, aplicación móvil Android y API REST — con **11 defectos
reportados en Jira** (proyecto `KAN`). Los reportes están reproducidos en
[BUG_REPORTS.md](./BUG_REPORTS.md).

## 1. Aplicación web — "Estado del pedido" y "Realizar pedido"

- **Checklist de 22 comprobaciones** del flujo de estado del pedido (búsqueda por número, cadena de 4 estados, cancelación, pedido atrasado), ejecutada en **Opera 132** y contrastada con Chrome.
- **36 pruebas de validación de datos** del formulario "Realizar pedido" por clases de equivalencia y valores límite: Nombre y Apellido (2–15 letras latinas), Dirección (5–50 caracteres), Teléfono (10–12 dígitos), Estación de metro (lista de la API), Fecha de entrega, Período de alquiler (1–7 días), Color y Comentario (máx. 24 caracteres).

Resultados: 4 defectos de validación (fechas pasadas seleccionables, entrada
manual de fecha permitida, comentario sin límite de longitud ni filtro de
caracteres) y un **defecto bloqueante** (KAN-5) que impidió verificar la cadena
de estados del pedido.

## 2. Aplicación móvil — app del repartidor

**5 casos de prueba** ejecutados en emulador (Android Studio, Google Pixel 4 XL,
Android 10) sobre las notificaciones push de vencimiento de pedido y el manejo
de pérdida de conexión:

| Caso | Resultado |
|---|---|
| Push 2 horas antes del vencimiento del pedido | ❌ NO APROBADO (KAN-10 — la notificación no se dispara) |
| Contenido del mensaje de la notificación | ⛔ BLOQUEADO (depende de KAN-10) |
| Navegación al tocar la notificación | ⛔ BLOQUEADO (depende de KAN-10) |
| Pop-up "Sin acceso a Internet" | ✅ APROBADO |
| Cierre del pop-up y persistencia sin conexión | ✅ APROBADO |

## 3. API — mensajeros y pedidos

**Checklist de 30 comprobaciones** sobre tres endpoints (`POST /api/v1/courier`,
`DELETE /api/v1/courier/:id`, `GET /api/v1/orders/track`) con casos happy path,
valores límite y negativos.

**Hallazgo principal:** la API **no valida el formato de los campos** — acepta
logins de 1 u 11 caracteres, con números, caracteres no latinos y símbolos;
contraseñas de longitud incorrecta o con letras; nombres fuera de regla; e IDs
con letras (devuelve el error incorrecto). Solo las validaciones de presencia
(campo ausente/vacío) y de duplicados funcionan correctamente.

## Artefactos adicionales

- Mapa mental de descomposición de la funcionalidad "Realizar pedido" ([`evidencia/mapa_mental_urban_scooter.jpg`](./evidencia/mapa_mental_urban_scooter.jpg)).
- Capturas de las pruebas móviles ([`evidencia/`](./evidencia)).
- Cuestionario teórico completo (diseño de pruebas, HTTP/HTTPS, SQL, bases de datos, estrategia de automatización) incluido en la hoja de cálculo.

## Evidencia

- [`evidencia/proyecto_final_urban_scooter.xlsx`](./evidencia/proyecto_final_urban_scooter.xlsx) — las 4 tareas completas: teoría, checklist web, validación de datos, casos móviles y checklist de API.
