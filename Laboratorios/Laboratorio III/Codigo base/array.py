import array

# prueba array 10 elementos:
#despues probar para n elementos generados
arr=array.array('i',[1,2,3,4,5,6,7,8,9,10])
print(arr)
#remover elemetno con pop()

arr.pop(0)
print(arr)

#insert(posicion,numero)
arr.insert(0,3)
print(arr)

# para biscar usar metodo binario recurisvo?¿?¡
# o buscar dsegun indice?
# Ejemplo: buscar numero de indice 4
print(arr[5])