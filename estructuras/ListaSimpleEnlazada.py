from estructuras.Nodo import Nodo

class ListaSimpleEnlazada:
    """
    Clase que modela una lista enlazada.
    """

    def __init__(self):
        """Constructor de la lista enlazada simple"""
        self.primero = None
        self.longitud = 0
    
    def esta_vacia(self):
        """Medodo que valida si la lista se encuentra vacía. Retornando True o False"""
        return self.primero is None


    # Método para insertar datos en la lista
    def insertar_dato(self,dato):
        nuevo_nodo = Nodo(dato)
        #El primer nod esta vació, va entrar a esta conedición en la primera iteración
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevo_nodo
        self.longitud += 1

    # Método para mostrar la lista completa.
    def mostrar_informacion(self):

        if self.esta_vacia():
            print("Lista se encuentra vacía.")
            return
        
        actual = self.primero

        while actual is not None:
            if hasattr(actual.dato, 'mostrar_datos'):
                actual.dato.mostrar_datos()
            else:
                print(actual.dato)
            actual = actual.next

