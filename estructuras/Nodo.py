class Nodo:

    def __init__(self,dato=None,siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
    
class NodoCola:
    def __init__(self,dato,prioridad):
        self.dato = dato
        self.prioridad = prioridad
        self.siguiente = None
