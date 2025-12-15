from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class ControladorVM: 
    def __init__(self):
        self.lista_vm = ListaSimpleEnlazada()

    def crear_vm(self,vm):
        self.lista_vm.agregar_dato(vm)
    
    def mostrar_vm(self):
        self.lista_vm.mostrar_informacion()
    
   

