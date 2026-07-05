# 🐞 Informes de errores — Urban Routes

Defectos encontrados durante la ejecución de la suite de pruebas funcionales.
Formato: identificador, título, pasos para reproducir, resultado esperado,
resultado actual y severidad.

---

## BR1 — No se despliega la lista de estaciones del metro

- **Caso de prueba asociado:** CASO-6
- **Severidad:** 🟠 Grave

**Pasos para reproducir**
1. Abrir la aplicación Urban Routes.
2. Hacer clic en el campo "Hasta".
3. Escribir "Subway" (Metro).

**Resultado esperado:** se muestra la lista de estaciones de metro.

**Resultado actual:** no se despliega la lista mencionada, ni ningún elemento de la misma índole.

---

## BR2 — El zoom no se genera sobre la ubicación proporcionada

- **Caso de prueba asociado:** CASO-7
- **Severidad:** 🔴 Crítico

**Pasos para reproducir**
1. Abrir la aplicación Urban Routes.
2. Hacer clic en el campo "Desde".
3. Ingresar una dirección (ejemplo: *East 2nd Street, 601*).

**Resultado esperado:** el mapa hace zoom sobre el pin de la dirección seleccionada; la vista coincide con la descripción del diseño.

**Resultado actual:** el mapa genera zoom en una zona predeterminada, la misma para todas las ubicaciones proporcionadas.

---

## BR3 — No se muestra el pin ni se hace zoom en las direcciones seleccionadas

- **Caso de prueba asociado:** CASO-8
- **Severidad:** 🔴 Crítico

**Pasos para reproducir**
1. Abrir la aplicación Urban Routes.
2. Hacer clic en el campo "Hasta".
3. Ingresar una dirección (ejemplo: *1300 1st St*).

**Resultado esperado:** el mapa hace zoom sobre el pin de la dirección seleccionada.

**Resultado actual:** el mapa genera zoom en la misma zona predeterminada del error BR2 y, adicionalmente, no se muestra el pin indicado.

---

## BR4 — La renderización 3D de los objetos no se ejecuta

- **Caso de prueba asociado:** CASO-11
- **Severidad:** 🟡 Menor

**Pasos para reproducir**
1. Abrir la aplicación Urban Routes.
2. Ampliar el mapa varias veces sobre un objeto 3D (ejemplo: *Los Angeles International Airport LAX*).

**Resultado esperado:** el objeto se renderiza en 3D.

**Resultado actual:** el mapa solo se renderiza en 2D al ampliar al máximo los objetos.

---

## BR5 — No se muestra la información de la aplicación al pulsar el logotipo

- **Caso de prueba asociado:** CASO-24
- **Severidad:** ⚪ Trivial

**Pasos para reproducir**
1. Abrir la aplicación Urban Routes.
2. Hacer clic en el logotipo de Urban Routes.

**Resultado esperado:** se muestra la información sobre la aplicación.

**Resultado actual:** no se despliega la información sobre la aplicación al pulsar el logotipo.
