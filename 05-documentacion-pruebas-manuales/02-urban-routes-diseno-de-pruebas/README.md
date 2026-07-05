# 📐 Urban Routes — Diseño de pruebas

Aplicación de técnicas formales de **diseño de pruebas** sobre los requisitos
de *Urban Routes* (formulario de registro de conductor y cálculo de viajes):
análisis de requisitos, descomposición funcional y derivación de datos de
prueba óptimos.

## Técnicas aplicadas

### Clases de equivalencia y valores límite

Ejemplo aplicado a los campos *Nombre* y *Apellido* del formulario (regla: 2–14 caracteres, alfabeto latino):

| Clase | Límites | Dato dentro de la clase | Dato en el límite | Propósito |
|---|---|---|---|---|
| Válida: 2–14 caracteres | 2, 14 | `David` (5) | `BD` (2), `Brian David-B` (14) | Validación principal de longitud |
| Inválida: menos de 2 | 1 | — | `D` (1) | Rechazo de entradas cortas |
| Inválida: más de 14 | 15 | — | `Brian David-Br` (15) | Truncamiento o rechazo de entradas largas |
| Inválida: caracteres no latinos | — | `Óscañû` | — | Solo alfabeto latino permitido |

También se derivaron clases para la **distancia entre direcciones** (> 0 km válido,
≤ 0 km inválido) y la **hora de salida** (rango 00:00–23:59 con casos en ambos límites).

### Casos de prueba de lógica de negocio

Casos diseñados para el cálculo de **tiempo y costo del viaje** según la tarifa,
el modo (Personal/Compartido) y la franja horaria (la velocidad promedio del
sistema cambia entre 30 y 45 km/h según el horario).

### Artefactos de análisis

- **Mapa mental** — descomposición funcional de la aplicación ([`evidencia/mapa_mental.pdf`](./evidencia/mapa_mental.pdf)).
- **Diagrama de flujo** — flujo del proceso de registro de la licencia de conducir ([`evidencia/diagrama_de_flujo.png`](./evidencia/diagrama_de_flujo.png)).

## Evidencia

- [`evidencia/diseno_de_pruebas_urban_routes.xlsx`](./evidencia/diseno_de_pruebas_urban_routes.xlsx) — clases de equivalencia (2 partes) y casos de prueba completos.
- [`evidencia/mapa_mental.pdf`](./evidencia/mapa_mental.pdf)
- [`evidencia/diagrama_de_flujo.png`](./evidencia/diagrama_de_flujo.png)
