import array as arr

class ArrayList():
    def __init__(self):
        self.elementos=arr.array('i',[])

    def agregar_elemento_inicio(self, elemento_int):
        self.elementos.insert(0,elemento_int)

    def eliminar_elemento_final(self):
        if len(self.elementos)==0:
            return "La lista no contiene elementos para eliminar."
        else:
            return self.elementos.pop()
            
    def tamaño_lista(self):
        if len(self.elementos)==0:
            return "La lista no contiene elementos."
        else:
            self.tamaño=len(self.elementos)
            return self.tamaño

    def buscar_por_indice(self, indice):
        if len(self.elementos)==0:
            return "La lista no contiene elementos."
        else:    
            self.elemento_del_indice=self.elementos[indice-1]
            return self.elementos[indice-1]
         
    def lista_completa(self):
        if len(self.elementos)==0:
            return "La lista no contiene elementos."
        else:
            return self.elementos