#Abril Gallardo
from dataStark import * 
def menu():
    limpiar_pantalla()
    print(f"{'DESAFIO STARK 00':^50s}")
    print("A- Imprimir el nombre de cada superhéroe")
    print("B- Imprimir el nombre de cada superhéroe junto a la altura del mismo")
    print("C- Determinar cuál es el superhéroe más alto")
    print("D- Determinar cuál es el superhéroe más bajo")
    print("E- Determinar la altura promedio de los superhéroes")
    print("F- Informar cual es el Nombre del superhéroe segun el resultado de los puntos D y E")
    print("G- Calcular e informar cual es el superhéroe más y menos pesado")
    print("H- Salir del programa")
    return ingresar_opcion()

def limpiar_pantalla():
    """Limpia pantalla por cada iteracion
    """
    import os
    os.system("cls")

def pausar():
    """Pausa el programa en cada iteracion
    """
    import os
    os.system("pause")

def ingresar_opcion()->str:
    """pide al usuario que ingrese la opcion

    Returns:
        str: retorna la opcion querida
    """
    opcion = input("Ingrese una opcion: ").upper()

    while opcion not in "ABCDEFGH":
        opcion = input("Error, ingrese una opcion: ").upper()

    return opcion

def mostrar_dato_heroe(lista:list, key:str):
    """muestra el dato segun la clave pedida

    Args:
        lista (list): lista de los personaje a recorrer
        key (str): clave del cual se quiere el dato
    """
    print("SUPERHEROES: ")
    for heroe in lista:
        print(f"-{heroe[key]}")

def mostrar_heroe_altura(lista:list, key:str, key2:str):
    """muestra la altura y el nombre de cada uno de los heroes

    Args:
        lista (list): lista de los personaje a recorrer
        key (str): clave para buscar el nombre
        key2 (str): clave para buscar la altura
    """
    for heroe in lista:
        print(f"- Nombre: {heroe[key]} - Altura: {heroe[key2]}")

def heroe_mayor_dato(lista:list, key:str):
    """busca el dato maximo que sea pedido segun la clave

    Args:
        lista (list): lista de los personaje a recorrer
        key (str): clave que indica de que dato se pide el maximo

    Returns:
        _type_: retorna el valor maximo
    """
    mayor = 0

    for heroe in lista:
        if float(heroe[key]) > mayor:
            mayor = float(heroe[key])

    return mayor

def heroe_menor_dato(lista:list, key:str):
    """busca el dato minimo que sea pedido segun la clave

    Args:
        lista (list): lista de los personaje a recorrer
        key (str): clave que indica de que dato se pide el minimo

    Returns:
        _type_: retorna el valor minimo
    """
    menor = float('inf')

    for heroe in lista:
        if float(heroe[key]) < menor:
            menor = float(heroe[key])

    return menor

def promedio_altura(lista:list):
    """Busca el promedio de alturas de los superheroes

    Args:
        lista (list): lista de los personaje a recorrer

    Returns:
        _type_: retorna el resultado del promedio
    """
    contador_heroes = 0
    acumulador_altura = 0
    promedio_total  = 0

    for heroe in lista:
        altura = float(heroe["altura"])
        contador_heroes = len(lista)
        acumulador_altura += altura
    
    if contador_heroes != 0:
        promedio_total= acumulador_altura / contador_heroes
    else: 
        promedio_total = 0
    return promedio_total

def nombre_heroe(lista, key, dato):
    """asocia el nombre del heroe segun el dato y la clave en especifico que se pide

    Args:
        lista (_type_): lista de los personaje a recorrer
        key (_type_): clave que indica que dato se esta buscando
        dato (_type_): dato ya anteriormente buscado en otra funciones

    Returns:
        _type_: retorna el nombre encontrado
    """
    for heroe in lista:
        if float(heroe[key]) == dato:
            return heroe["nombre"]
        

def pedirConfirmacion(mensaje:str)->str:
    """Confirma la salida del programa

    Args:
        mensaje (str): mensaje hacia el usuario

    Returns:
        str: retorna la respuesta del usuario
    """
    rta = input(mensaje).lower()
    return rta == "si"

