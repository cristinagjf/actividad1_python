# Actividad 1 - Aplicación CRUD de productos en Python
# Cristina García Juan
# Programa de consola que permite crear, listar, actualizar y eliminar productos guardados en una lista


class Producto:
    """Representa un producto del inventario."""
    def __init__(self, id_producto, nombre, precio, cantidad): #  constructor
        self.id = id_producto  # identificador único (int). id_producto porque id es palabra de Python
        self.nombre = nombre  # nombre del producto (str)
        self.precio = precio  # precio del producto (float)
        self.cantidad = cantidad  # unidades en inventario (int)

    def __str__(self):  # cómo se ve el producto al imprimirlo
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Precio: {self.precio:.2f} € | Cantidad: {self.cantidad}")


# Lista vacía donde se guardan los productos mientras se ejecuta el programa
productos = []

# Variable global para dar un id único a cada producto incrementado
siguiente_id = 1


# Funciones de validación

def pedir_texto(mensaje, valor_actual=None):
    """Pide un texto que no esté vacío
    Si se pasa valor_actual y el usuario pulsa Intro, se conserva"""
    while True:  # repite la pregunta constantemente
        texto = input(mensaje).strip()  # pregunta y quita espacios sobrantes (devuelve texto)
        if texto == "" and valor_actual is not None:
            return valor_actual
        if texto != "":
            return texto
        print("Error: el texto no puede estar vacío.")


def pedir_entero(mensaje, valor_actual=None):
    """Pide un número entero mayor o igual que 0
    Si se pasa valor_actual y el usuario pulsa Intro, se conserva"""
    while True:
        texto = input(mensaje).strip()
        if texto == "" and valor_actual is not None:
            return valor_actual
        try:
            numero = int(texto)  # intenta convertir. Si eran letras lanza error y salta al except. Luego while vuelve a pregutnar
            if numero < 0:
                print("Error: el número no puede ser negativo.")
            else:
                return numero  # lo entrega ya convertido a número
        except ValueError:
            print("Error: escribe un número entero (sin letras ni decimales).")


def pedir_decimal(mensaje, valor_actual=None):
    """Pide un número decimal mayor o igual que 0
    Si se pasa valor_actual y el usuario pulsa Intro, se conserva"""
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        if texto == "" and valor_actual is not None:
            return valor_actual
        try:
            numero = float(texto)
            if numero < 0:
                print("Error: el precio no puede ser negativo.")
            else:
                return numero
        except ValueError:
            print("Error: escribe un número (por ejemplo 12.50).")

