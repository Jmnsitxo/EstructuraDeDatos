#ejemplo de cola (FIFO - First In First out)
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items)==0
    
    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola esta vacia")
        
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            raise IndexError("La cola esta vacia")
    
    def tamano(self):
        return len(self.items)
    
#ejemplo de uso 

if __name__=="__main__":
    cola=Cola()
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    print("frente de la cola:", cola.ver_frente())
    print("tamaño de la cola:", cola.tamano())
    print("desencolando", cola.desencolar())
    print("desencolando", cola.desencolar())
    print("tamaño de la cola despues de desencolar:", cola.tamano())

    

        