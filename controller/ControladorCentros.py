from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class ControladorCentros: 
    def __init__(self):
        self.lista_centros = ListaSimpleEnlazada()

    def crear_centro(self,centro):
        self.lista_centros.agregar_dato(centro)

    def mostrar_centros_datos(self):
        self.lista_centros.mostrar_informacion()
    
    
    
       
    

    

