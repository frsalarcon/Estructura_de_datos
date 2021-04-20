class Nodo():
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None       

class LinkedList():
    def __init__(self):
        self.cabecera = None
        self.contador=0

    def agregar_elemento_inicio(self, elemento):
        nuevo_nodo = Nodo(elemento)
        nuevo_nodo.siguiente=self.cabecera
        self.cabecera=nuevo_nodo

    def eliminar_elemento_final(self):
        if self.cabecera is None:
            print("La lista no contiene elementos para eliminar.")
            return
        elemento_eliminar = self.cabecera
        while elemento_eliminar.siguiente.siguiente is not None:
            elemento_eliminar = elemento_eliminar.siguiente
        elemento_eliminar.siguiente = None

    def tamaño_lista(self):
        if self.cabecera is None:
            return 0
        inicio_lista=self.cabecera
        while inicio_lista is not None:
            self.contador=self.contador+1
            inicio_lista=inicio_lista.siguiente
            return self.contador

    def buscar_por_indice(self, indice):
        elemento_actual=self.cabecera
        while(elemento_actual):
            if (self.contador==indice-1):
                return elemento_actual.elemento
            self.contador +=1
            elemento_actual=elemento_actual.siguiente
            

    def imprimir_lista(self):
        if self.cabecera is None:
            print("La lista no contiene elementos.")
            return
        else:
            elemento_cabecera = self.cabecera
            while elemento_cabecera is not None:
                print(elemento_cabecera.elemento , " ")
                elemento_cabecera = elemento_cabecera.siguiente

