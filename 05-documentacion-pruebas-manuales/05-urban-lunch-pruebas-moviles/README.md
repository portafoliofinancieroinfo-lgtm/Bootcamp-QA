# 📱 Urban Lunch — Pruebas de aplicación móvil (Android)

Pruebas manuales de la app Android *Urban Lunch* (pedidos de comida) ejecutadas
sobre **dos emuladores con perfiles de hardware distintos** en Android Studio,
para validar el comportamiento en gama media y gama baja.

## Matriz de dispositivos

| Dispositivo emulado | Android | Resolución | RAM | Resultado |
|---|---|---|---|---|
| Honor 8 | 9 (API 28) | 1080×1920 (480 dpi) | 2 GB | 38/38 pruebas aprobadas · 0 bugs |
| Galaxy J2 | 9 (API 28) | 540×960 (240 dpi) | 2 GB | 37/38 pruebas aprobadas · **1 bug** |

Configuración de los emuladores: acelerómetro, GPS, cámaras y sensores activados;
red a velocidad completa; orientación vertical.

## Alcance (38 comprobaciones por dispositivo)

1. Selección del punto de recogida en el mapa (selección, deselección, cambio de punto, feedback visual).
2. Flujo completo de pedido en 5 pasos.
3. Agregar y quitar platillos del carrito.
4. Cálculo de precios y tiempos de entrega.
5. Seguimiento del estado del pedido.

## Hallazgo

En el dispositivo de **pantalla pequeña (Galaxy J2, 540×960)** se detectó
**solapamiento de elementos de la interfaz**, defecto que no se reproduce en la
resolución mayor del Honor 8.

**Conclusión del informe:** el producto es estable y funcional en los entornos
probados; se recomienda definir y validar los parámetros de la interfaz según
el tamaño de pantalla del dispositivo para evitar el solapamiento de elementos.

## Evidencia

- [`evidencia/pruebas_moviles_urban_lunch.xlsx`](./evidencia/pruebas_moviles_urban_lunch.xlsx) — checklist de 38 comprobaciones por dispositivo.
- [`evidencia/informe_de_pruebas_urban_lunch.docx`](./evidencia/informe_de_pruebas_urban_lunch.docx) — informe de resultados con la configuración de los emuladores.
