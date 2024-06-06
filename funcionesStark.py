#Abril Gallardo
from dataStark import * 
def menu():
    limpiar_pantalla()
    print(f"{'DESAFIO STARK':^50s}")
    print("A- Imprimir el nombre de cada superhéroe")
    print("B- Imprimir el nombre de cada superhéroe junto a la altura del mismo")
    print("C- Determinar cuál es el superhéroe más alto")
    print("D- Determinar cuál es el superhéroe más bajo")
    print("E- Determinar la altura promedio de los superhéroes")
    print("F- Informar cual es el Nombre del superhéroe segun el resultado de los puntos D y E")
    print("G- Calcular e informar cual es el superhéroe más y menos pesado")
    print("H- Nombre de cada superhéroe de género M")
    print("I- Nombre de cada superhéroe de género F")
    print("J- Superhéroe más alto de género M")
    print("K- Superhéroe más alto de género F")
    print("L- Superhéroe más bajo de género M")
    print("M- Superhéroe más bajo de género F")
    print("N- Altura promedio de los superhéroes de género M")
    print("O- Altura promedio de los superhéroes de género F")
    print("P- Informar cual es el Nombre del superhéroe segun el resultado de los puntos de J a la N")
    print("Q- Determinar cuántos superhéroes tienen cada tipo de color de ojos")
    print("R- Determinar cuántos superhéroes tienen cada tipo de color de pelo")
    print("S- Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    print("T- Listar todos los superhéroes agrupados por color de ojos.")
    print("U- Listar todos los superhéroes agrupados por color de pelo.")
    print("V- Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("W- Salir del programa ")
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

    while opcion not in "ABCDEFGHIJKLMNOPQRSTUVW":
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
        print(f"- Nombre: {heroe[key]:<20} - Altura: {heroe[key2]:<20}")

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

def superheroes_generos(lista:list, genero:str):
    """
    Imprime los nombres de los superhéroes que pertenecen al genero especificado

    Args:
        lista (list): Una lista de diccionarios que contienen informacion sobre supereroes
        genero (str): El genero de los superhéroes que se quiera imprimir
    """
    lista_generos = []
    for heroe in lista:
        if heroe["genero"] == genero:
            lista_generos.append(heroe["nombre"])

    for heroe in lista_generos:
        print(f"- {heroe}")

def heroe_mas_alto_genero(lista:list, genero:str)-> float:
    """
    Encuentra la altura del superheroe mas alto del genero especificado

    Args:
        lista (list): Una lista de diccionarios que contienen informacion sobre superheroes
        genero (str): El genero de los superheroes entre los cuales se busca al mas alto

    Returns:
        float: La altura del superheroe mas alto del genero especificado
    """
    mas_alto = 0
    
    for heroe in lista:
        altura = float(heroe["altura"])
        if heroe["genero"] == genero:
            if altura > mas_alto:
                mas_alto = altura
            
    return mas_alto
            

def heroe_mas_bajo_genero(lista:list, genero:str)-> float:
    """
    Encuentra la altura del superheroe mas bajo del genero especificado

    Args:
        lista (list): Una lista de diccionarios que contienen informacion sobre superheroes
        genero (str): El genero de los superheroes entre los cuales se busca al mas bajo

    Returns:
        float: La altura del superheroe mas bajo del genero especificado
    """
    mas_bajo = float('inf')
    
    for heroe in lista:
        altura = float(heroe["altura"])
        if heroe["genero"] == genero:
            if altura < mas_bajo:
                mas_bajo = altura
            
    return mas_bajo

def promedio_altura_genero(lista:list, genero:str)-> float:
    """
    Calcula el promedio de altura de los superheroes del genero especificado

    Args:
        lista (list): Una lista de diccionarios que contienen informacion sobre superheroes
        genero (str): El genero de los superheroes para calcular el promedio de altura

    Returns:
        float: El promedio de altura de los superheroes del genero especificado
    """
    contador_heroes = 0
    acumulador_altura = 0
    promedio_total  = 0

    for heroe in lista:
        if heroe["genero"] == genero:
            altura = float(heroe["altura"])
            contador_heroes = len(lista)
            acumulador_altura += altura
        
    if contador_heroes != 0:
        promedio_total= acumulador_altura / contador_heroes
    else: 
        promedio_total = 0
    return promedio_total

def obtener_cantidad_por_dato(lista_heroes:list, key_dato:str):
    """
    Obtiene la cantidad de superheroes agrupados por un dato especifico

    Args:
        lista_heroes (list): Una lista de diccionarios que contienen informacion sobre superheroes
        key_dato (str): El nombre del dato por el cual se quiere agrupar

    Returns:
        dict: Un diccionario que contiene la cantidad de superheroes agrupados por el dato especificado
    """
    if not lista_heroes:
        return False

    cantidad_por_dato = {}
    for heroe in lista_heroes:
        dato = heroe[key_dato]
        if dato == "":
            cantidad_por_dato["No tiene"] = cantidad_por_dato.get(dato, 0) + 1
        else:
            cantidad_por_dato[dato] = cantidad_por_dato.get(dato, 0) + 1

    return cantidad_por_dato 

def swapLista(lista:list, i :int, j:int):
    """
    Intercambia dos elementos en una lista

    Args:
        lista (list): La lista en la cual se realizan los intercambios
        i (int): Indice del primer elemento a intercambiar
        j (int): Indice del segundo elemento a intercambiar
    """
    aux = lista[i]
    lista[i], lista[j] = lista[j], aux

def ordenar_por_dato(lista:list, key:str):
    """
    Ordena una lista de diccionarios por el valor de una clave especifica

    Args:
        lista (list): Una lista de diccionarios que se desea ordenar
        key (str): La clave por la cual se desea ordenar los diccionarios
    """
    cant_heroes = len(lista)
    for i in range(cant_heroes - 1):
        for j in range(i + 1, cant_heroes):
            if lista[i][key] > lista[j][key] :
                swapLista(lista, i ,j)


def mostrar_heroes(lista:list, key:str):
    """
    Muestra una lista de superheroes y un atributo especifico de cada uno

    Args:
        lista (list): Una lista de diccionarios que contienen informacion sobre superheroes
        key (str): La clave de los superheroes que se desea mostrar
    """
    tam = len(lista)
    print("       ***LISTADO DE HEROES***   ")
    print(f"Nombre              | {key.capitalize()} ")
    print("------------------------------------------")
    for i in range(tam):
        mostrar_heroe(lista[i], key)
    print()

def mostrar_heroe(heroe:list, key):
    """
    Muestra la informacion de un superheroe

    Args:
        heroe (list): Una lista que contiene la informacion de un superheroe
        key (str): La clave especifica del superheroe que se desea mostrar
    """
    if heroe[key] == "":
        print(f"{heroe["nombre"]:<20}| {"No tiene":<9}")
    else:
        print(f"{heroe["nombre"]:<20}| {heroe[key]:<9}")








