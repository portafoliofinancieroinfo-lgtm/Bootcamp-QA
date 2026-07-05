# 🗺️ Urban Routes — Pruebas funcionales de la interfaz del mapa

Primera suite de pruebas manuales del bootcamp: **24 casos de prueba**
documentados y ejecutados sobre la aplicación web *Urban Routes* (mapa
interactivo estilo Google Maps), con **5 defectos encontrados y reportados**
con severidad asignada.

## Alcance

- Interacción con el mapa: desplazamiento, zoom, modos de vista (Relieve, Satélite, Street View, pantalla completa).
- Campos de búsqueda de ruta "Desde" / "Hasta": selección, autocompletado, pin de dirección, borrado.
- Renderizado de objetos: edificios, estaciones de metro, lugares de interés, parques, objetos 3D.
- Ventanas de información de objetos del mapa.

## Resultados

| Métrica | Valor |
|---|---|
| Casos de prueba diseñados | 24 |
| Aprobados | 17 |
| No aprobados (con bug asociado) | 5 |
| Omitidos (justificados en comentarios) | 2 |

Cada caso no aprobado quedó vinculado a su informe de error (BR1–BR5).
Los reportes completos están en [BUG_REPORTS.md](./BUG_REPORTS.md).

## Resumen de defectos

| ID | Título | Severidad |
|---|---|---|
| BR1 | No se despliega la lista de estaciones del metro | Grave |
| BR2 | El zoom no se genera sobre la ubicación proporcionada | Crítico |
| BR3 | No se muestra el pin ni se hace zoom en las direcciones seleccionadas | Crítico |
| BR4 | La renderización 3D de los objetos no se ejecuta | Menor |
| BR5 | No se muestra la información de la aplicación al pulsar el logotipo | Trivial |

## Evidencia

- [`evidencia/casos_de_prueba_y_bugs_urban_routes.xlsx`](./evidencia/casos_de_prueba_y_bugs_urban_routes.xlsx) — hoja de cálculo original con los 24 casos de prueba y los informes de errores.
