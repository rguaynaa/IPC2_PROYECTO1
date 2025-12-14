from estructuras.Nodo import Nodo

class ListaSimpleEnlazada:

    def __init__(self):
        self.primero = None
        self.longitud = 0
    
    def esta_vacia(self):
        return self.primero is None


    def agregar_dato(self,dato):
        nuevo_nodo = Nodo(dato)

        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1


    def mostrar_informacion(self):

        if self.esta_vacia():
            print("La lista no contiene infomarción.")
            return
        
        actual = self.primero
        while actual is not None:
            if hasattr(actual.dato, 'mostrar_datos'):
                actual.dato.mostrar_datos()
            else:
                print(actual.dato) 
            actual = actual.siguiente


    def buscar_dato_por_id(self, id_buscado, atributo_id):
        actual = self.primero
        while actual is not None:
            if hasattr(actual.dato, atributo_id):
                if getattr(actual.dato, atributo_id) == id_buscado:
                    return actual.dato.mostrar_datos()
            actual = actual.siguiente
        return None


    def obtener_longitud(self):
        return self.longitud
    

    def eliminar_dato_por_id(self, id_buscado, atributo_id):

        if self.esta_vacia():
            print("La lista se encuentra vacía.")
            return False
        
        # El dato a eliminar es el primer nodo
        if hasattr(self.primero.dato, atributo_id):
            if getattr(self.primero.dato, atributo_id) == id_buscado:
                dato_eliminado = self.primero.dato
                self.primero = self.primero.siguiente
                self.longitud -= 1
                print(f"El elemento {dato_eliminado} fue eliminado exitosamente.")
                return True
            
        # El datro a eliminar se encuentra en medio o final
        actual = self.primero
        while actual.siguiente is not None:
            if hasattr(actual.siguiente.dato,atributo_id):
                if getattr(actual.siguiente.dato, atributo_id) == id_buscado:
                    dato_eliminado = actual.siguiente.dato
                    actual.siguiente = actual.siguiente.siguiente
                    self.longitud -= 1
                    print(f"El elmento {dato_eliminado} fue eliminado exitosamente.")
                    return True
            actual = actual.siguiente
        
        print(f"No se encontró el elemento {id_buscado} buscado.")
        return False

            


