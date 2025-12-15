from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada
from controller.ControladorVM import ControladorVM

class ControladorCentros: 
    def __init__(self):
        self.lista_centros = ListaSimpleEnlazada()

    def crear_centro(self,centro):
        self.lista_centros.agregar_dato(centro)

    def mostrar_centros_datos(self):
        self.lista_centros.mostrar_informacion()

    def agregar_vm(self, vm, id_centro):
        centro = self.lista_centros.buscar_dato_por_id(id_centro, 'id')
        if centro is None:
            print("El centro ",{id_centro}," no existe para agregar VM ",{vm.id})
            return False
        centro.vm.agregar_dato(vm)
        return True



    

    
       
    

    

