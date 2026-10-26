# Actividad 1 - Aplicación CRUD de productos en Python
# Cristina García Juan
# Programa de consola que permite crear, listar, actualizar y eliminar productos guardados en una lista


class Producto: 
    """Representa un producto del inventario."""
    def __init__(self, id_producto, nombre, precio, cantidad): #  constructor
        self.id = id_producto #  identificador único (int). id_producto porque id es palabra de Python
        self.nombre = nombre #  nombre del producto (str)
        self.precio = precio #  precio del producto (float)
        self.cantidad = cantidad #  unidades en inventario (int)

    def __str__(self): #  cómo se ve el producto al imprimirlo
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Precio: {self.precio:.2f} € | Cantidad: {self.cantidad}")




# Lista vacía donde se guardan los productos mientras se ejecuta el programa
productos = []

# Variable global para dar un id único a cada producto incrementado
siguiente_id = 1
