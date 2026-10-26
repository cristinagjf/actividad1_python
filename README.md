# Actividad Individual 1 - Programación en Python (2º DAW)

## Descripción

Practicar el diseño de clases en Python y su aplicación en un sistema CRUD (create, read, update and delete / crear, leer, actualizar y eliminar). Los productos se representan con la clase `Producto` y se guardan en una lista en memoria mientras el programa está en ejecución.

## Requisitos

- Python 3 (desarrollado con Python 3.14).
- No necesita librerías externas: solo usa Python estándar.
- Opcional: Visual Studio Code con las extensiones Python (Microsoft) y Code Runner.
- Opcional: Git, para clonar el repositorio.

## Instalación y ejecución

1. Descargar el proyecto de una de estas dos formas:
   - Clonar el repositorio:

```bash
     git clone https://github.com/cristinagjf/actividad1_python.git
     cd actividad1_python
```

   - O descomprimir el ZIP entregado y abrir una terminal dentro de la carpeta.
2. Comprobar que Python está instalado:

```bash
   python --version
```

3. Ejecutar el programa:

```bash
   python crud_productos.py
```

   En Visual Studio Code también se puede abrir `crud_productos.py` y pulsar el botón Run Code (con Code Runner configurado para ejecutarse en la terminal).
4. Elegir una opción del menú escribiendo su número y pulsando Enter. La opción 5 cierra el programa.

## Estructura del proyecto

```text
actividad1_python/
├── crud_productos.py       # Código fuente de la aplicación
├── README.md               # Este documento
├── .gitignore              # Ficheros que Git no debe guardar
└── historial_commits.txt   # Historial de commits (solo en la entrega ZIP)
```

## Explicación del código

El programa está organizado de arriba abajo en cinco bloques:

- **Clase `Producto`**: define los atributos `id` (int), `nombre` (str), `precio` (float) y `cantidad` (int). El constructor `__init__` los inicializa y el método `__str__` devuelve el producto en formato legible, con el precio a 2 decimales.
- **Lista y contador global**: `productos = []` almacena los objetos `Producto`. `siguiente_id` es una variable global que se incrementa con cada producto creado para asignar ids únicos automáticamente. No disminuye al eliminar, así los ids nunca se repiten.
- **Funciones de validación**: `pedir_texto`, `pedir_entero` y `pedir_decimal` piden datos con `input()`, los convierten al tipo adecuado y, mediante `try/except ValueError`, repiten la pregunta con un mensaje claro si el usuario escribe letras, decimales o números negativos donde no corresponde. Si reciben un valor actual y el usuario pulsa Intro sin escribir, lo conservan (se usa al actualizar).
- **Funciones CRUD**:
  - `crear_producto()`: pide nombre, precio y cantidad, crea el objeto y lo añade a la lista.
  - `listar_productos()`: recorre la lista y muestra cada producto, o avisa si está vacía.
  - `actualizar_producto()`: busca un producto por id y permite modificar sus datos.
  - `eliminar_producto()`: busca un producto por id y lo elimina de la lista.
  - Las dos últimas usan `buscar_producto_por_id()` e informan al usuario si el id no existe.
- **Menú principal**: `mostrar_menu()` imprime las opciones y `main()` repite el menú con un bucle `while` hasta que se elige la opción 5. La opción leída se compara como texto (`"1"`, `"2"`...). El programa arranca con `if __name__ == "__main__":`.

## Resultados esperados

Al ejecutar el programa aparece el menú:

```text
GESTIÓN DE PRODUCTOS
1. Crear producto
2. Listar productos
3. Actualizar producto
4. Eliminar producto
5. Salir
Selecciona una opción:
```

Ejemplo de uso:

```text
Crear producto
Nombre: Barco
Precio: abc
Error: escribe un número (por ejemplo 12.50).
Precio: 12.5
Cantidad: 30
Producto creado correctamente con id 1.

Listado de productos
ID: 1 | Nombre: Barco | Precio: 12.50 € | Cantidad: 30

Eliminar producto
Id del producto a eliminar: 99
Error: no existe ningún producto con id 99.
```

- Si se lista sin productos, se muestra "No hay productos registrados."
- Al actualizar, pulsar Intro sin escribir mantiene el valor actual.
- Una opción de menú no válida muestra "Esta opción no existe. Elige un número/opción del 1 al 5." y vuelve a mostrar el menú.
- Con la opción 5 aparece "¡Hasta pronto!" y el programa termina.

## Control de versiones

El proyecto se ha desarrollado con Git, con un commit por cada parte del programa validada.

- Repositorio: https://github.com/cristinagjf/actividad1_python
- Historial de commits: https://github.com/cristinagjf/actividad1_python/commits/main
- En local: `git log --oneline`

## Autora

- Nombre: Cristina García Juan
- Correo: cristinagj.f@gmail.com
- Módulo: Programación en Python, 2º DAW (UNIR FP - PROEDUCA)

## Licencia

Uso académico: Proyecto realizado con fines educativos para la Actividad 1 Individual del módulo de Python de UNIR.