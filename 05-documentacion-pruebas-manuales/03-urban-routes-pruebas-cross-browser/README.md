# 🌐 Urban Routes — Pruebas web cross-browser (función "Compartir automóvil")

Pruebas de una aplicación web ejecutadas en **dos entornos en paralelo** —
Google Chrome a 800×600 y Mozilla Firefox a 1920×1080 — sobre la funcionalidad
de reserva de automóvil compartido. Los defectos se reportaron y gestionaron
en **Jira** (proyecto `BRIAN`, 15 informes de errores).

## Alcance

1. **Lista de comprobación de diseño (9 checks):** estado inicial del formulario, tarifas disponibles, correspondencia visual con el diseño, ortografía/tipografía e idioma de la interfaz.
2. **Validación de las ventanas "Método de pago" y "Agregar tarjeta" (21 checks):** formato del número de tarjeta (nnnn nnnn nnnn) y del código de seguridad, con comprobaciones positivas y negativas por valores límite (11, 12 y 13 dígitos; 1, 2 y 3 caracteres; caracteres mezclados; espaciados incorrectos).
3. **Casos de prueba de la lógica del botón "Reservar" (5 casos):** combinaciones de campos obligatorios completos/incompletos.
4. **Casos de prueba del flujo de reserva (6 casos):** ventana "Automóvil reservado", información del vehículo, temporizador de espera gratuita (30 s) y lógica del botón "Cancelar".

## Resultados

| Bloque | Checks/Casos | No aprobados |
|---|---|---|
| Diseño | 9 | 2 (ortografía de tarifa; idioma en Firefox) |
| Método de pago / Agregar tarjeta | 21 | 11 (validaciones negativas de tarjeta y código no implementadas) |
| Lógica del botón "Reservar" | 5 | 2 (no exige licencia ni método de pago faltantes) |
| Flujo de reserva | 6 | 0 |

**Hallazgo principal:** el formulario de tarjeta acepta entradas con formato
inválido (11 o 13 dígitos, caracteres alfanuméricos, espaciado incorrecto) en
**ambos navegadores**, y el botón "Reservar" permite continuar sin licencia de
conducir o sin método de pago — defectos de validación que afectan el flujo de
pago (reportados como BRIAN-3 a BRIAN-17).

También se detectó un defecto **exclusivo de Firefox** (idioma de la interfaz
no corresponde al español latino, BRIAN-2), evidenciando el valor de las
pruebas multi-navegador.

## Evidencia

- [`evidencia/pruebas_cross_browser_urban_routes.xlsx`](./evidencia/pruebas_cross_browser_urban_routes.xlsx) — listas de comprobación y casos de prueba con resultados por navegador y enlaces a Jira.

> Los informes BRIAN-1 a BRIAN-17 se gestionaron en una instancia privada de
> Jira del bootcamp; la hoja de cálculo conserva los enlaces originales como
> trazabilidad.
