from modelos.Contenedor import Contenedor

class ControladorContenedores:
    def __init__(self,controlador_vm):
        self.controlador_vms = controlador_vm
    
    def desplegar_contenedores(self,id_vm,id_contenedor,nombre,cpu,ram,puerto):

        vm = self.controlador_vms.buscar_vm_id(id_vm)

        if vm:
            disponible_cpu = vm.recursos_cpu_disponibles()
            disponible_ram = vm.recursos_ram_disponibles()


            if disponible_cpu >= int(cpu) and disponible_ram >= int(ram):
                from modelos.Contenedor import Contenedor
                nuevo_contenedor = Contenedor(id_contenedor,nombre,int(cpu),int(ram),puerto)
                vm.contenedores.agregar_dato(nuevo_contenedor)
                print(f"Contenedor {nombre} desplegado en VM {id_vm}.")
            else:
                print(f"Error: Recursos insuficientes en VM {id_vm} para desplegar el contenedor {nombre}.")

    def listar_contenedores_vm(self,id_vm):
        vm = self.ctrl_vms.buscar_vm_por_id(id_vm)
        if vm:
            print("="*40)
            print(f"Contenedores en VM {id_vm}:")
            print("="*40)
            vm.contenedores.mostrar_informacion()
        else:
            print(f"Error: VM {id_vm} no encontrada.")
    
    def eliminar_contenedor(self,id_vm,id_contenedor):
        vm = self.controlador_vms.buscar_vm_id(id_vm)
        if vm:
            if vm.contenedores.eliminar_dato_por_id(id_contenedor,'id'):
                print(f"Contenedor {id_contenedor} eliminado de VM {id_vm}.")
            else:
                print(f"Error: Contenedor {id_contenedor} no encontrado en VM {id_vm}.")
    
    def cambiar_estado_contenedor(self, id_vm, id_cont, nueva_accion):
        vm = self.controlador_vms.buscar_vm_id(id_vm)
        if not vm:
            print(f"Error: La VM {id_vm} no existe.")
            return

        contenedor = vm.contenedores.buscar_dato_por_id(id_cont, 'id')
        
        if contenedor:
            print(f"Estado actual: {contenedor.estado}")
            
            if nueva_accion == "1": # Activar
                if contenedor.estado == "Activo":
                    print("El contenedor ya está Activo.")
                else:
                    contenedor.estado = "Activo"
                    print("Contenedor ACTIVADO.")
            
            elif nueva_accion == "2": # Pausar
                if contenedor.estado == "Pausado":
                    print("El contenedor ya está Pausado.")
                else:
                    contenedor.estado = "Pausado"
                    print("Contenedor PAUSADO.")
            
            elif nueva_accion == "3": # Reiniciar
                print("Reiniciando contenedor...")
                contenedor.estado = "Activo"
                print("Contenedor REINICIADO y Activo.")
        else:
            print(f"Error: El contenedor {id_cont} no existe en la VM {id_vm}.")