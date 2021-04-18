class Lista():
    def __init__(self):
        self.elementos = []
    def lista_vacia(self):
            return self.elementos == []
    def push(self, item):
        self.elementos.append(item)				
    def pop(self):
        return self.elementos.pop()
    def peek(self):
        if not self.lista_vacia():
            return self.elementos[-1]
    def size(self):
        return len(self.elementos)
    # retornar la lista    
    def dar_lista(self):
        return self.elementos

