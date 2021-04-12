import functions as func
arreglo_generado = print("Arreglo de", func.cant_num_random, "elementos generados aleatoriamente correctamente")
arreglo_ordenado = sorted(func.list_num_random)
numero_a_buscar = int(input("Ingresa un número, para retornar la posición de este en el arreglo \n"))
print("El número ingresado fue:",numero_a_buscar)
print("Por el método lineal obtenemos que:")
result_lineal=func.busqueda_lineal(arreglo_generado,numero_a_buscar)
if result_lineal != -1:
    print("El número esta presente en el indice:",result_lineal)
else:
    print("El número no esta presente en el arreglo generado")
print("Tiempo de ejecución para el método de búsqueda lineal:",func.time_lineal)
print("Para el método binario, el arreglo es ordenado en forma ascendente. Obtenemos que:")
result_binario=func.busqueda_binaria_recursiva(arreglo_ordenado,numero_a_buscar)
if result_binario != -1:
    print("El número esta presente en el indice:",result_binario)
else:
    print("El número no esta presente en el arreglo generado")

print("Tiempo de ejecución para el método de búsqueda binaria recursiva:",func.time_binrec)

