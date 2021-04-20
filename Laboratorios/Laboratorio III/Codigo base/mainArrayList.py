import random
import time 
from ArrayList import ArrayList 

lista=ArrayList()


def salir():
    print("Salida...!")
    exit()

def main():
    while True:
        print("ArrayList:")
        print(" ")
        print("Selecciona una opción:\n")
        print("1. Agregar elemento al inicio de la lista.")
        print("2. Eliminar un elemento al final de la lista.")
        print("3. Tamaño de la lista.")
        print("4. Buscar elemento por indice.")
        print("5. Imprimir la lista.")
        print("6. Salir.")


        opcion=int(input("Opción: "))
        if opcion ==1:
            print("1. Agregar elemento al inicio de la lista.")
            elemento_int=int(input("Ingresar elemento para añadir al inicio de la lista:"))
            tiempo_agregar_inicio=time.perf_counter()
            lista.agregar_elemento_inicio(elemento_int)
            tiempo_agregar_final=time.perf_counter()
            tiempo_total_agregar=format(tiempo_agregar_final-tiempo_agregar_inicio,'.10f')
            print("Tiempo de ejecución de la operación: ",tiempo_total_agregar)
            print("Operación realizada!\n")

        if opcion ==2:
            print("2. Eliminar un elemento al final de la lista.")
            tiempo_eliminar_inicio=time.perf_counter()
            lista.eliminar_elemento_final()
            tiempo_eliminar_final=time.perf_counter()
            tiempo_total_eliminar=format(tiempo_eliminar_final-tiempo_eliminar_inicio,'.10f')
            print("Tiempo de ejecución de la operación: ",tiempo_total_eliminar)
            print("Operación realizada!\n")

        if opcion == 3:
            print("3. Tamaño de la lista.")
            print("El tamaño de la lista es de:")
            tiempo_tamaño_inicio=time.perf_counter()
            print(lista.tamaño_lista(),"elementos.")
            tiempo_tamaño_final=time.perf_counter()
            tiempo_tamaño_total=format(tiempo_tamaño_final-tiempo_tamaño_inicio,'.10f')
            print("Tiempo de ejecución de la operación: ",tiempo_tamaño_total)
            print("Operación realizada!\n")

        if opcion == 4:
            print("4. Buscar elemento por indice.")
            elemento_int=int(input("Ingresa el indice, para retornar el número correspondiente:"))
            tiempo_buscar_inicio=time.perf_counter()
            print("Para el indice ingresado corresponde el elemento de la lista es:", lista.buscar_por_indice(elemento_int))
            tiempo_buscar_final=time.perf_counter()
            tiempo_buscar_total=format(tiempo_buscar_final-tiempo_buscar_inicio,'.10f')
            print("Tiempo de ejecución de la operación: ",tiempo_buscar_total)
            print("Operación realizada!\n")

        if opcion ==5:
            print("5. Imprimir la lista.")
            print("Lista:")
            tiempo_imprimir_inicio=time.perf_counter()
            print(lista.lista_completa())
            tiempo_imprimir_final=time.perf_counter()
            tiempo_imprimir_total=format(tiempo_imprimir_final-tiempo_imprimir_inicio,'.10f')
            print("Tiempo de ejecución de la operación: ",tiempo_imprimir_total)
            print("Operación realizada!\n")

        if opcion == 6:
            salir()

if __name__ == '__main__':
    main();