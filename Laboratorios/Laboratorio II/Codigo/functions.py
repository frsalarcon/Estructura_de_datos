import random #Generador de números random
import time # Tiempo transcurrido durante la ejecución
list_num_random= []
cant_num_random= int(input("Ingresa un número, el cual correspondera a la cantidad de números que compondran tu arreglo aleatoriamente generado:\n"))
#Generador de números aleatorios:
for i in range(0, cant_num_random):
    n = random.randint(1, 100000000)
    list_num_random.append(n)
# Funciones:
#Busqueda lineal:
t_lineal_ini=time.perf_counter()
def busqueda_lineal(lista_de_numeros_random, numero_a_buscar):
    for i in range(cant_num_random):
        indice_buscado=i+1
        if list_num_random[i] == numero_a_buscar:
            return i+1
    return -1
#Tiempo ejecución busqueda lineal:
t_lineal_fin=time.perf_counter()
time_lineal=format(t_lineal_fin-t_lineal_ini,'.10f')


#Busqueda Binaria Recursiva:
t_binrec_ini=time.perf_counter()
def busqueda_binaria_recursiva(arreglo_ordenado, numero_a_buscar):
    index_inicio=0
    index_final=len(arreglo_ordenado)-1
    mitad_arreglo=0
    while index_inicio <= index_final:
        mitad_arreglo= (index_inicio+index_final)//2
        if arreglo_ordenado[mitad_arreglo] > numero_a_buscar:
            index_final=mitad_arreglo-1
        elif arreglo_ordenado[mitad_arreglo]<numero_a_buscar:
            index_inicio=mitad_arreglo+1
        else:
            return mitad_arreglo+1
    return -1
#Tiempo ejecución busqueda binaria recursiva:
t_binrec_fin=time.perf_counter()
time_binrec=format(t_binrec_fin-t_binrec_ini, '.10f')
