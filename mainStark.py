#Abril Gallardo
from funcionesStark import * 
from dataStark import * 

seguir = "si"

while seguir == "si":
    match menu():
        case "A":
            mostrar_dato_heroe(lista_personajes, "nombre")
        case "B":
            mostrar_heroe_altura(lista_personajes, "nombre", "altura")
        case "C":
            print(f"El superheroe mas alto mide: {heroe_mayor_dato(lista_personajes, "altura")}")
        case "D":
            print(f"El superheroe mas bajo mide: {heroe_menor_dato(lista_personajes, "altura")}")
        case "E":
            print(f"El promedio de altura de los superheroes es: {promedio_altura(lista_personajes)}")
        case "F":
            altura_mas_baja = heroe_menor_dato(lista_personajes, "altura")
            altura_mas_alta = heroe_mayor_dato(lista_personajes, "altura")
            print(f"El heroe mas bajo es: {nombre_heroe(lista_personajes, "altura", altura_mas_baja)}\nEl heroe mas alto es: {nombre_heroe(lista_personajes,"altura", altura_mas_alta)}")
        case "G":
            peso_mas_bajo = heroe_menor_dato(lista_personajes, "peso")
            peso_mas_alto = heroe_mayor_dato(lista_personajes, "peso")
            print(f"El heroe menos pesado es: {nombre_heroe(lista_personajes, "peso", peso_mas_bajo)}\nEl heroe mas pesado es: {nombre_heroe(lista_personajes,"peso", peso_mas_alto)}")
        case "H":
            if pedirConfirmacion("Confirmar salida si/no: "):
                seguir = "no"
            continue
    pausar()