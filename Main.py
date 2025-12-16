from controller.ControladorContenedores import ControladorContenedores
from controller.ControladorSolicitudes import ControladorSolicitudes
from controller.ControladorMenu import ControladorMenu
from carpeta_xml.Lector import Lector
from controller.ControladorVM import ControladorVM
from controller.ControladorCentros import ControladorCentros
from controller.ControladorSolicitudes import ControladorSolicitudes
from controller.ControladorInstrucciones import ControladroInstrucciones
from controller.ControladorGraphviz import ControladorGraphviz


class Main:
    def __init__(self):
        self.funciones = Funciones()
        

    def Menuprincipal(self):

        while True:
            print("\n" +"="*40)
            print("|            Menu Principal            |")
            print("="*40)
            print("|1. Cargar Archivo XML.                |")
            print("|2. Gestión de Centros de Datos.       |")
            print("|3. Gestión de Máquinas Virtuales.     |")
            print("|4. Gestión de Contenedores.           |")
            print("|5. Gestión de Solicitudes.            |")
            print("|6. Reportes en Graphviz.              |")
            print("|7. Generar Reporte XML \"salida.xml\".|")
            print("|8. Historial de Operaciopnes.         |")
            print("|9. Salir.                             |")
            print("="*40)

            opcion = input("Seleccione una opción: ")
            

            if opcion=="1":
                self.funciones.cargarArchivoXML()
            elif opcion=="2":
                self.funciones.gestionCentrosDatos()
            elif opcion=="3":
                self.funciones.gestionMaquinasVirtuales()
            elif opcion=="4":
                self.funciones.gestionContenedores()
            elif opcion=="5":
                self.funciones.gestionSolicitudes()
            elif opcion=="6":
                self.funciones.reportesGraphviz()
            elif opcion=="7":
                self.funciones.generarReporteXML()
            elif opcion=="8":
                self.funciones.historialOperaciones()
            elif opcion=="9":
                self.funciones.salir()
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

#......................FUNCIONES DEL MENU..........................
class Funciones:
    def __init__(self):

        self.controladorMenu = ControladorMenu()
        self.controladorCentro = ControladorCentros()
        self.controladorVM = ControladorVM()
        self.ControladorContenedores = ControladorContenedores(self.controladorVM)
        self.controladorSolicitudes = ControladorSolicitudes()
        self.controllerInstruccion = ControladroInstrucciones() 
        self.lector = Lector(controladorVM=self.controladorVM,controladorCentros=self.controladorCentro,
                             controladorSolicitudes=self.controladorSolicitudes,controllerInstruccion=self.controllerInstruccion)
        self.controladorSolicitudes = ControladorSolicitudes() 
        self.controladorGraphviz = ControladorGraphviz()



    def cargarArchivoXML(self):
        print("\n" +"="*20)
        print("|Cargar Archivo XML|")
        print("="*20)
        ruta = self.controladorMenu.cargar_xml('carpeta_xml/entrada')
        self.lector.cargar_archivo_xml(ruta)
    

    def gestionCentrosDatos(self):

        while True:
            print("\n" +"="*40)
            print("|     Gestión de Centros de Datos.     |")
            print("="*40)
            print("|1. Listar Todos los Centros de Datos  |")
            print("|2. Buscar Centro de Datos por ID.     |")
            print("|3. Ver Centro con mayor recursos      |")
            print("|4. Volver al Menú Principal           |")
            print( "="*40)
            opcion = input("Seleccione una opción: ")
        
            if opcion=="1":
                self.controladorCentro.mostrar_centros_datos()
            elif opcion=="2":
                id_buscado = input("Ingrese el ID: ")
                centro_encontrado = self.controladorCentro.lista_centros.buscar_dato_por_id(id_buscado,'id')
                if centro_encontrado:
                    centro_encontrado.mostrar_datos()
                else:
                    return centro_encontrado
            elif opcion=="3":
                print("Mostrando Centro con mayor recursos...")
                self.controladorCentro.ver_centro_mayor_recursos()
            elif opcion=="4":
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
            return opcion

    
    def gestionMaquinasVirtuales(self):
        while True:
            print("\n" +"="*46)
            print("|        Gestión de Máquinas Virtuales       |")
            print("="*46)
            print("|1. Buscar VM por ID                         |")
            print("|2. Listar Todas Las VM de un Centro de Datos|")
            print("|3. Migrar VM entre Centros de Datos         |")
            print("|4. Volver al Menú Principal                 |")
            print("="*46)

            opcion = input("Seleccione una opción: ")

            if opcion=="1":
                print("Buscando VM por ID...")
                id_vm=input("Ingrese el ID de la VM a buscar: ")
                self.controladorVM.mostrar_vm_por_id(id_vm)

            elif opcion=="2":
                print("="*40)
                id_centro = input("Ingrese el ID del Centro de Datos: ")
                self.controladorVM.listar_vms_de_centro(self.controladorCentro, id_centro=id_centro)
            elif opcion=="3":
                print("Migrando VM entre Centros de Datos...")
                
                id_vm = input("Ingrese ID de la VM a migrar: ")
                id_destino = input("Ingrese ID del Centro Destino: ")
                self.controladorVM.migrar_vm(self.controladorCentro, id_vm, id_destino)
            elif opcion=="4":
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        

    
    def gestionContenedores(self):
        while True:
            print("\n" +"="*44)
            print("|          Gestión de Contenedores         |")
            print("="*44)
            print("|1. Desplegar Contenedor en VM             |")
            print("|2. Listar Todos Los Contenedores de una VM|")
            print("|3. Cambiar Estado de un contenedor        |")
            print("|4. Elimminar Contenedor de una VM         |")
            print("|5. Volver al Menú Principal               |")
            print("="*44)
            opcion = input("Seleccione una opción: ")
            
            if opcion=="1":
                print("="*30)
                print("| Desplegar Contenedor en VM |")
                print("="*30)
                print("| Ingrese los datos|")
                print("-"*30)

                id_vm = input("ID de la VM: ")
                id_cont = input("ID del nuevo Contenedor: ")
                nombre = input("Nombre: ")
                imagen = input("Imagen: ")
                cpu = input("CPU (%): ")
                ram = input("RAM (MB): ")
                puerto = input("Puerto: ")
                self.ControladorContenedores.desplegar_contenedores(id_vm, id_cont, nombre,imagen, cpu, ram, puerto)

            elif opcion=="2":
                print("="*40)
                id_vm = input("Ingrese ID de la VM: ")

                self.ControladorContenedores.listar_contenedores_vm(id_vm)

            elif opcion=="3":
                print("Cambiando Estado de un contenedor...")
                print("Cambiando Estado de un contenedor...")
                id_vm = input("Ingrese ID de la VM: ")
                id_cont = input("Ingrese ID del Contenedor: ")
                print("1. Activar")
                print("2. Pausar")
                print("3. Reiniciar")
                accion = input("Seleccione estado: ")
                
                if accion == "1" or accion == "2" or accion == "3":
                    self.ControladorContenedores.cambiar_estado_contenedor(id_vm, id_cont, accion)
                else:
                    print("Opción no válida.")
            elif opcion=="4":
                print("Eliminando Contenedor de una VM...")
                id_vm = input("ID de la VM: ")
                id_cont = input("ID del Contenedor a eliminar: ")
                self.ControladorContenedores.eliminar_contenedor(id_vm, id_cont)
            elif opcion=="5":
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

    def gestionSolicitudes(self):
        while True:
            print("\n" +"="*42)
            print("|         Gestión de Solicitudes         |")
            print("="*42)
            print("|1. Agregar Solicitud                    |")
            print("|2. Procesar Solicitud de Mayor Prioridad|")
            print("|3. Procesar las Solicitudes             |")
            print("|4. Ver Cola de Solicitudes              |")
            print("|5. Volver al Menú Principal             |")
            print("="*42)
            opcion = input("Seleccione una opción: ")
            if opcion=="1":
                print("Agregando Solicitud...")
                print("="*30)
                print("| Agregar Nueva Solicitud |")
                print("="*30)
                print("| Ingrese los datos|")
                print("-"*30)

                id = input("ID de la solicitud: ")
                cliente = input("Nombre del cliente: ")
                tipo = input("Tipo Deploy o Backup: ")
                prioridad = int(input("Prioridad: "))
                cpu = int(input("CPU: "))
                ram = int(input("RAM (GB): "))
                alm = int(input("Almacenamiento GB: "))
                tiempo = int(input("Tiempo: "))
                self.controladorSolicitudes.agregar_solicitud( id, cliente, tipo, prioridad, cpu, ram, alm, tiempo)

            elif opcion=="2":
                print("Procesando Solicitud de Mayor Prioridad...")
                self.controladorSolicitudes.procesar_solicitud(self.controladorCentro)
            elif opcion=="3":
                print("Procesando las Solicitudes...")
                cantidad = input("Cantidad que desea ejecutar: ")
                self.controladorSolicitudes.procesar_varias_solicitudes(self.controladorCentro,cantidad)
            elif opcion=="4":
                print("Viendo Cola de Solicitudes...")
                self.controladorSolicitudes.ver_cola()
                # LOGICA O METODO A LLAMAR
            elif opcion=="5":
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")
        
    
    def reportesGraphviz(self):
        while True:
            print("\n" +"="*56)
            print("|                 Reportes en Graphviz                 |")
            print("="*56)
            print("|1. Reporte de Centros de Datos                        |")
            print("|2. Reporte de VM en un Centro de Datos según ID.      |")
            print("|3. Reporte de Contenedor Desplegado en una VM según ID|")
            print("|4. Reporte de la Cola de Solicitudes                  |")
            print("|5. Volver al Menú Principal                           |")
            print("="*56)
            opcion = input("Seleccione una opción: ")
            
            if opcion=="1":
                print("Generando Reporte de Centros de Datos...")
                self.controladorGraphviz.generar_reporte_centros(self.controladorCentro)
            elif opcion=="2":   
                print("Generando Reporte de VM en un Centro de Datos según ID...")
                id_centro = input("Ingrese ID del Centro de Datos: ")
                print(f"Generando Reporte de VM en el Centro {id_centro}...")
                self.controladorGraphviz.generar_reporte_vms(self.controladorCentro, id_centro)
            elif opcion=="3":
                print("Generando Reporte de Contenedor Desplegado en una VM según ID...")
                id_vm = input("Ingrese ID de la VM: ")
                print(f"Generando Reporte de Contenedores en la VM {id_vm}...")
                self.controladorGraphviz.generar_reporte_contenedores(self.controladorVM, id_vm)
            elif opcion=="4":
                print("Generando Reporte de la Cola de Solicitudes...")
                self.controladorGraphviz.generar_reporte_solicitudes(self.controladorSolicitudes)
            elif opcion=="5":
                print("Volviendo al Menú Principal...")
                break
            else:
                print("Opción inválida. Por favor, intente de nuevo.")

    def generarReporteXML(self):
        print("Generando Reporte XML \"salida.xml\"...")
        # LOGICA O METODO A LLAMAR
    
    def historialOperaciones(self):
        print("Mostrando Historial de Operaciones...")
        # LOGICA O METODO A LLAMAR
    
    def salir(self):
        print("Saliendo del programa...")
        exit()

if __name__ == '__main__':
        main = Main()
        main.Menuprincipal()

#......................METODOS DEL PROGRAMA..........................