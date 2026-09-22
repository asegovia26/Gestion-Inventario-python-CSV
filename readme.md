# Práctica: Gestión de Inventario con CSV

## Integrantes del Equipo
* Antonio Segovia
* Juan Francisco Martínez
* Héctor Dorado
* Juan David García

## Distribución Inicial de Roles
* **Antonio Segovia:** Configuración del repositorio Git/GitHub, estructuración inicial del proyecto y desarrollo de la validación integral del fichero CSV (Pregunta 5).
* **Juan Francisco Martínez:** Implementación del formateo visual y tabulación con f-strings en el listado general de productos (Pregunta 2).
* **Héctor Dorado:** Desarrollo de la funcionalidad de filtrado de stock configurable por teclado y tratamiento de excepciones (Pregunta 3).
* **Juan David García:** Implementación de la función para productos agotados, reestructuración del menú interactivo (Pregunta 4) y diseño de la batería de pruebas.

## Cambios Realizados
1. **Presentación de productos (`mostrar_productos`):**
   * Conversión explícita de `precio` a `float` y `stock` a `int`.
   * Formateo del nombre alineado a 25 caracteres a la izquierda (`:<25`).
   * Representación monetaria con dos cifras decimales (`:.2f €`) y captura de `ValueError`.

2. **Límite de stock interactivo (`mostrar_poco_stock`):**
   * Sustitución del valor fijo `5` por una entrada dinámica mediante `input()`.
   * Validación de entradas no numéricas con bloque `try/except ValueError`.
   * Validación preventiva frente a números negativos.

3. **Detección de productos sin stock (`mostrar_productos_agotados`):**
   * Creación de la función que filtra registros con `stock == 0`.
   * Integración de la nueva opción en el menú principal (`Opción 4`).
   * Reasignación de la opción de salida (`Opción 6`) y actualización del diccionario de despacho `opciones`.

4. **Validación de integridad del CSV (`cargar_productos`):**
   * Integración de `enumerate(lector, start=2)` para asociar errores a la línea física real del archivo.
   * Descarte con `continue` ante registros que carezcan de código o nombre.
   * Validación numérica de `precio` y `stock`, rechazando valores no parseables o cantidades negativas.

## Casos de Prueba Ejecutados
* **Prueba de stock configurable (Pregunta 3):**
  * *Entrada: 5* -> Muestra monitor (3) y auriculares (4).
  * *Entrada: 10* -> Muestra monitor (3), auriculares (4), teclado (8) y webcam (0).
  * *Entrada: -2* -> Notifica: "El límite no puede ser negativo" y vuelve al menú.
  * *Entrada: cinco* -> Notifica: "Debes introducir un número entero" y vuelve al menú.
* **Prueba de productos agotados (Pregunta 4):**
  * Muestra con éxito la `P006 | Webcam` (stock: 0).
* **Prueba de robustez del CSV (Pregunta 5):**
  * Inclusión de filas de prueba en `productos.csv`:
    * `P007;Altavoces;treinta;6` -> Salida: *Fila 8 ignorada: precio incorrecto.*
    * `P008;;25.50;4` -> Salida: *Fila 9 ignorada: falta el nombre.*
    * `P009;Disco externo;79.90;-3` -> Salida: *Fila 10 ignorada: el stock no puede ser negativo.*
    * `;Adaptador USB;9.95;10` -> Salida: *Fila 11 ignorada: falta el código.*
  * La aplicación omite las líneas corruptas y carga únicamente los 6 productos válidos originales.

## Dificultades Encontradas
El principal reto residió en mantener la sincronización exacta del número de línea al informar de registros inválidos en el CSV, resuelto eficazmente configurando `start=2` en `enumerate()` para no computar la cabecera. Asimismo, fue clave asegurar que las cadenas de texto vacías o compuestas exclusivamente por espacios en blanco fueran detectadas como inválidas mediante el método `.strip()`.

## Resultado Final
El gestor es capaz de procesar ficheros CSV delimitados por punto y coma, ignorar registros con datos de negocio inconsistentes sin interrumpir la ejecución, y ofrecer una interfaz interactiva de consola completamente protegida contra entradas de usuario inválidas.

## Ventajas de DictReader
El uso de `csv.DictReader` frente a lectores convencionales basados en listas proporciona una capa de abstracción semántica fundamental. Al mapear automáticamente la primera fila del CSV como claves de un diccionario, permite acceder a los datos mediante nombres descriptivos de columna (`fila['precio']`) en lugar de índices posicionales numéricos (`fila[2]`). Esta característica desacopla el código de la estructura física del archivo, evitando que la aplicación se rompa si se reorganiza o añade una columna en el fichero fuente. Además, mejora drásticamente la legibilidad, reduce la probabilidad de cometer errores de acceso fuera de rango (`IndexError`) y facilita el mantenimiento a largo plazo del software.