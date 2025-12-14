from estructuras.Nodo import NodoCola

class ListaCola:
    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def esta_vacia(self):
        return self.primero is None

    def insertar_dato(self,dato,prioridad):
        nuevo_nodo = NodoCola(dato,prioridad)

        if self.esta_vacia or prioridad > self.primero.prioridad:
            nuevo_nodo.siguiente = self.primero
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente and actual.siguiente.prioridad >= prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            
        self.longitud += 1