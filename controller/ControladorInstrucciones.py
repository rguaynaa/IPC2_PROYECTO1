from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada


class ControladroInstrucciones:
    def __init__(self):
        self.list_instrucciones = ListaSimpleEnlazada()
    
    def crear_instrucciones(self,instruccion):
        self.list_instrucciones.agregar_dato(instruccion)

    # def ejecutar_instrucciones(self,tipo,vm,id_centro):
    #         if tipo == 'crearVM':
    #             self.controladorCentro.agregar_vm(vm,id_centro)
    #         elif tipo == 'migrarVM':
    #             pass
    #         elif tipo == 'procesarSolicitudes':
    #             pass
    #         else:
    #             print("Instrucción no encontrada.")
            