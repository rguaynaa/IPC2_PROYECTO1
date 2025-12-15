from controller.ControladorMenu import ControladorMenu
from carpeta_xml.Lector import Lector
from controller.ControladorVM import ControladorVM
from controller.ControladorCentros import ControladorCentros


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
        self.controladorVM = ControladorVM()
        self.controladorCentro = ControladorCentros()
        self.lector = Lector(controladorVM=self.controladorVM, controladorCentros=self.controladorCentro)


    def cargarArchivoXML(self):
        print("\n" +"="*20)
        print("|Cargar Archivo XML|")
        print("="*20)
        ruta = self.controladorMenu.cargar_xml('carpeta_xml\entrada.xml')
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
                self.controladorCentro.lista_centros.buscar_dato_por_id(id_buscado,'id')
            elif opcion=="3":
                print("Mostrando Centro con mayor recursos...")
                # LOGICA O METODO A LLAMAR
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
                self.controladorVM.mostrar_vm()
                # LOGICA O METODO A LLAMAR
            elif opcion=="2":
                print("Listando Todas Las VMs de un Centro de Datos...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="3":
                print("Migrando VM entre Centros de Datos...")
                # LOGICA O METODO A LLAMAR
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
                print("Desplegando Contenedor en VM...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="2":
                print("Listando Todos Los Contenedores de una VM...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="3":
                print("Cambiando Estado de un contenedor...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="4":
                print("Eliminando Contenedor de una VM...")
                # LOGICA O METODO A LLAMAR
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
                # LOGICA O METODO A LLAMAR
            elif opcion=="2":
                print("Procesando Solicitud de Mayor Prioridad...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="3":
                print("Procesando las Solicitudes...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="4":
                print("Viendo Cola de Solicitudes...")
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
                # LOGICA O METODO A LLAMAR
            elif opcion=="2":   
                print("Generando Reporte de VM en un Centro de Datos según ID...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="3":
                print("Generando Reporte de Contenedor Desplegado en una VM según ID...")
                # LOGICA O METODO A LLAMAR
            elif opcion=="4":
                print("Generando Reporte de la Cola de Solicitudes...")
                # LOGICA O METODO A LLAMAR
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