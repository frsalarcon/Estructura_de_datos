import array as arr

class ArrayList():
    def __init__(self):
        self.elementos=arr.array('f',[])

    def agregar_elemento_inicio(self, elemento):
        self.elementos.insert(0,elemento)

    def eliminar_elemento_final(self):
        self.elementos.pop()

    def tamaño_lista(self):
        self.tamaño=len(self.elementos)
        return self.tamaño

    def buscar_por_indice(self, indice):
        self.elemento_del_indice=self.elementos[indice-1]
        return self.elementos[indice-1]
         
    def imprimir_lista(self):
        return self.elementos

