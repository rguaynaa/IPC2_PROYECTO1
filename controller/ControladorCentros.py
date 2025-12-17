from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class ControladorCentros: 
    def __init__(self):
        self.lista_centros = ListaSimpleEnlazada()

    def crear_centro(self,centro):
        self.lista_centros.agregar_dato(centro)

    def mostrar_centros_datos(self):
        print("\n" +"="*32)
        print("|   Lista de Centros de Datos   |")
        print("="*32)
        print("")

        if self.lista_centros.esta_vacia():
            print("No hay centros de datos registrados.")
            return
        
        contador=1
        actual= self.lista_centros.primero
        while actual is not None:
            print(f"{contador}.{actual.dato.id}")
            actual.dato.mostrar_datos()
            contador += 1

            actual = actual.siguiente
            print("")
            



    def agregar_vm(self, vm, id_centro):
        centro = self.lista_centros.buscar_dato_por_id(id_centro, 'id')
        if centro is None:
            print("El centro ",{id_centro}," no existe para agregar VM ",{vm.id})
            return False
        centro.vm.agregar_dato(vm)
        return True

    def ver_centro_mayor_recursos(self):
            print("\n" +"="*40)
            print("| Centro de Datos con Mayor Recursos |")
            print("="*40)
    
            if self.lista_centros.esta_vacia():
                print("No hay centros de datos registrados")
                return None
    
            maximo_recursos = -1
            centro_mayor = None

            actual = self.lista_centros.primero    
            while actual is not None:
                centro = actual.dato

                recursos_totales = (centro.cpu_nucleos_total + 
                                centro.ram_total_GB + 
                                centro.almacenamiento_total_GB)
                #recursos_mayor = centro_mayor.cpu + centro_mayor.ram + centro_mayor.almacenamiento
    
                if recursos_totales > maximo_recursos:
                    centro_mayor = centro
                    maximo_recursos = recursos_totales
    
                actual = actual.siguiente
            if centro_mayor:
                print("")
                centro_mayor.mostrar_datos()
            else:
                print("No se encontraron centros de datos") 

    

    
       
    

    

