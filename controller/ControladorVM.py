from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada


class ControladorVM: 
    def __init__(self):
        self.lista_vm = ListaSimpleEnlazada()

    def crear_vm(self,vm):
        self.lista_vm.agregar_dato(vm)
    
    def mostrar_vm(self):
        self.lista_vm.mostrar_informacion()
    
    def buscar_vm_id(self,id_vm):
        vm=self.lista_vm.buscar_dato_por_id(id_vm,'id')
        return vm
    
    def mostrar_vm_por_id(self, id_vm):
        vm = self.buscar_vm_id(id_vm)
        if vm:
            print("VM encontrada:")
            vm.mostrar_datos()
        else:
            print(f"La VM {id_vm} no existe en el sistema o esta mal redactada.")


    def listar_vms_de_centro(self, controlador_centros, id_centro):

        centro = controlador_centros.lista_centros.buscar_dato_por_id(id_centro, 'id')
        if centro:
            print("="*40)
            print(f"\n VMS EN {centro.nombre}")
            print("")

            lista_vms_del_centro = centro.vm

            if lista_vms_del_centro.esta_vacia():
                print("No hay vms de datos registrados.")
                return
            
            contador=1
            actual= lista_vms_del_centro.primero
            while actual is not None:
                vm=actual.dato

                print(f"{contador}.{vm.id}")
                vm.mostrar_datos()
                contador += 1

                actual = actual.siguiente
                print("")

        else:
            print(f"ERROR:El centro {id_centro} no existe.")


    def migrar_vm(self, controlador_centros, id_vm, id_centro_destino):
        vm = self.buscar_vm_id(id_vm)# buscammos la vm globalmente(entre todos los centros)
        if not vm:
            print(f"ERROR:VM {id_vm} no encontrada")
            return

        centro_origen=controlador_centros.lista_centros.buscar_dato_por_id(vm.id_centro, 'id')#buscamos el centro de origen de la vm
        centro_destino=controlador_centros.lista_centros.buscar_dato_por_id(id_centro_destino, 'id')#buscamos el centro destino

        if not centro_origen or not centro_destino:
            print("Error: Centro de origen o destino no válidos o no existen.")
            return
        
        if (centro_destino.cpu_disponible() >= vm.cpu_nucleos and
            centro_destino.ram_disponible() >= vm.ram_GB and
            centro_destino.almacenamiento_disponible() >= vm.almacenamiento_GB):
            
                if centro_origen.vm.eliminar_dato_por_id(id_vm, 'id'):

                    vm.id_centro = id_centro_destino

                    centro_destino.vm.agregar_dato(vm)
                    print(f"La VM {id_vm} migrada a {id_centro_destino}.")
                else:
                    print("Error al eliminar la VM del centro de origen.")
        else:
                print(f"Error: El centro {id_centro_destino} no tiene recursos suficientes para ser migrada")