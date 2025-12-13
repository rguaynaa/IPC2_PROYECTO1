from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada
from modelos.MaquinaVirtual import MaquinaVirtual
from controller.ControladorCentros import ControladorCentros

class ControladorVM: 
    def __init__(self):
        self.vm = ListaSimpleEnlazada()
        self.controlerCentro  = ControladorCentros

    def crear_vm(self,id, id_centro, so, cpu, ram_GB, almacenamiento_GB,ip):
        nuevo_vm = MaquinaVirtual(id, id_centro, so, cpu, ram_GB, almacenamiento_GB,ip)
        self.vm.agregar_dato(nuevo_vm)
        return
    