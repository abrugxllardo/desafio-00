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
            print("Superheroes masculinos: ")
            superheroes_generos(lista_personajes, "M")
        case "I":
            print("Superheroes femenino: ")
            superheroes_generos(lista_personajes, "F")
        case "J":
            
            print(f"El superheore masculino mas alto mide: {heroe_mas_alto_genero(lista_personajes, "M")}cm")
        case "K":
            
            print( f"El superheore femenino mas alto mide: {heroe_mas_alto_genero(lista_personajes, "F")}cm")
        case "L":
            
            print(f"El superheore masculino mas bajo mide: {heroe_mas_bajo_genero(lista_personajes, "M")}cm")
        case "M":
            
            print(f"El superheore femenino mas bajo mide: {heroe_mas_bajo_genero(lista_personajes, "F")}cm")
        case "N":
            promedio_altura_masc = f"El promedio de altura entre los superheroes masculinos es: {promedio_altura_genero(lista_personajes, "M")}"
            print(promedio_altura_masc)
        case "O":
            promedio_altura_fem = f"El promedio de altura entre los superheroes femeninos es: {promedio_altura_genero(lista_personajes, "F")}"
            print(promedio_altura_fem)
        case "P":
            masc_mas_alto = heroe_mas_alto_genero(lista_personajes, "M")
            fem_mas_alto =heroe_mas_alto_genero(lista_personajes, "F")
            masc_mas_bajo = heroe_mas_bajo_genero(lista_personajes, "M")
            fem_mas_bajo = heroe_mas_bajo_genero(lista_personajes, "F")
            print(f"El heroe masculino mas alto es: {nombre_heroe(lista_personajes, "altura", masc_mas_alto)}")
            print(f"El heroe femenino mas alto es: {nombre_heroe(lista_personajes, "altura", fem_mas_alto)}")
            print(f"El heroe masculino mas bajo es: {nombre_heroe(lista_personajes, "altura", masc_mas_bajo)}")
            print(f"El heroe femenino mas bajo es: {nombre_heroe(lista_personajes, "altura", fem_mas_bajo)}")
        case "Q":
            print(obtener_cantidad_por_dato(lista_personajes, "color_ojos"))
        case "R":
            print(obtener_cantidad_por_dato(lista_personajes, "color_pelo"))
        case "S":
            print(obtener_cantidad_por_dato(lista_personajes, "inteligencia"))
        case "T":
            print(ordenar_por_dato(lista_personajes, "color_ojos"))
            mostrar_heroes(lista_personajes, "color_ojos")
        case "U":
            print(ordenar_por_dato(lista_personajes, "color_pelo"))
            mostrar_heroes(lista_personajes, "color_pelo")
        case "V":
            print(ordenar_por_dato(lista_personajes, "inteligencia"))
            mostrar_heroes(lista_personajes, "inteligencia")
        case "W":
            if pedirConfirmacion("Confirmar salida si/no: "):
                seguir = "no"
            continue
    pausar()