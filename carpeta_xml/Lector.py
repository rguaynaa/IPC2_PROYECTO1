from modelos.Contenedor import Contenedor
from modelos.Solicitud import Solicitud
from modelos.Instrucciones import CrearVM, MigrarVM, Procesar
import xml.etree.ElementTree as ET
from modelos.CentroDatos import CentroDatos
from modelos.MaquinaVirtual import MaquinaVirtual
from controller.ControladorVM import ControladorVM
from controller.ControladorCentros import ControladorCentros


class Lector:
    def __init__(self, controladorVM=None, controladorCentros=None):
        self.controladorVM = controladorVM if controladorVM is not None else ControladorVM()
        self.controladorCentros = controladorCentros if controladorCentros is not None else ControladorCentros()
        self.list_solicitud = []
        self.list_crearVM = []
        self.list_migrarVM = []
        self.list_procesar = []

    
    def cargar_archivo_xml(self, ruta_archivo):
        try:
            tree = ET.parse(ruta_archivo)
            ruta = tree.getroot()

            self.cargar_centros(ruta)
            self.cargar_maquinas_virtuales(ruta)
            self.cargar_solicitudes(ruta)
            self.cargar_instrucciones(ruta)
            return True, "Archivos cargados exitosamente"
        
        except Exception as e:
            return False,f"Error al cargar el archivo {str(e)}"
    

    def cargar_centros(self, root):
        centros_xml = root.find('.//centrosDatos')
        if centros_xml is None:
            return
        
        for centro in centros_xml.findall('centro'):

            id_centro = centro.get('id')
            nombre = centro.get('nombre')

            ubicacion = centro.find('ubicacion')
            pais = ubicacion.find('pais').text
            ciudad = ubicacion.find('ciudad').text

            capacidad = centro.find('capacidad')
            cpu = int(capacidad.find('cpu').text)
            ram = int(capacidad.find('ram').text)
            almacenamiento = int(capacidad.find('almacenamiento').text)

            nuevo_centro = CentroDatos(id_centro, nombre, pais, ciudad, cpu, ram, almacenamiento)
            self.controladorCentros.crear_centro(nuevo_centro)
            

            print(f"Centro {id_centro} cargado exitosamente.")

    def cargar_maquinas_virtuales(self,root):
        maquinas_xml = root.find('.//maquinasVirtuales')
        if maquinas_xml is None:
            return
        
        for maquina in maquinas_xml.findall('vm'):

            id_mv = maquina.get('id')
            id_centro = maquina.get('centroAsignado')
            so = maquina.find('sistemaOperativo').text

            recursos = maquina.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)

            ip = maquina.find('ip').text

            nuevo_vm = MaquinaVirtual(id_mv,id_centro,so,cpu,ram,almacenamiento,ip)
            self.controladorVM.crear_vm(nuevo_vm)

            agregado = self.controladorCentros.agregar_vm(nuevo_vm, id_centro)
            if agregado:
                print(f"MaquinaVirtual {id_mv} cargado exitosamente.")


            if self.controladorVM.lista_vm is None:
                print("Hubo un error al cargar el archivo.")
            else:
                contenedores =  maquina.find('contenedores')
                for cont in contenedores.findall('contenedor'):
                    id_cont = cont.get('id')
                    nombre = cont.find('nombre').text
                    imagen = cont.find('imagen').text

                    recursos = cont.find('recursos')
                    cpu = int(recursos.find('cpu').text)
                    ram = int(recursos.find('ram').text)
                    puerto = cont.find('puerto').text

                    nuevo_cont = Contenedor(id_cont,nombre,imagen,cpu,ram,puerto)

                    nuevo_vm.contenedores.agregar_dato(nuevo_cont)

                    print(f"Contenedor {id_cont} cargado exitosamente.")



    def cargar_solicitudes(self,root):
        solicitudes_xml = root.find('.//solicitudes')
        if solicitudes_xml is None:
            return
        
        for sol in solicitudes_xml.findall('solicitud'):
            id_sol = sol.get('id')

            cliente = sol.find('cliente').text
            tipo = sol.find('cliente').text
            prioridad = int(sol.find('prioridad').text)

            recursos = sol.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)

            tiempo = int(sol.find('tiempoEstimado').text)

            nueva_solicitud = Solicitud(id_sol,cliente,tipo,prioridad,cpu,ram,almacenamiento,tiempo)

            self.list_solicitud.append(nueva_solicitud)
            print(f"Solicitud {id_sol} cargado exitosamente.")
        
        for sol in self.list_solicitud:
            sol.mostrar_datos()


    def cargar_instrucciones(self, root):
        instrucciones_xml = root.find('.//instrucciones')

        if instrucciones_xml is None:
            return
        
        for inst in instrucciones_xml.findall('instruccion'):
            tipo_inst = inst.get('tipo')

            if tipo_inst == ('crearVM'):
                id_vm = inst.find('id').text
                id_centro = inst.find('centro').text
                so = inst.find('so').text
                cpu = inst.find('cpu').text
                ram = inst.find('ram').text
                almacenamiento = inst.find('almacenamiento').text
                nuevoCrearVM = CrearVM(tipo_inst,id_vm,id_centro,so,cpu,ram,almacenamiento)
                self.list_crearVM.append(nuevoCrearVM)

                print(f"Instruccion {tipo_inst} cargado exitosamente")
                for crear in self.list_crearVM:
                    crear.mostrar_datos()
            
            elif tipo_inst == ('migrarVM'):
                id_vm = inst.find('vmId').text
                id_centro_origen = inst.find('centroOrigen').text
                id_centro_destino = inst.find('centroDestino').text

                nuevaMigra = MigrarVM(tipo_inst,id_vm,id_centro_origen,id_centro_destino)
                self.list_migrarVM.append(nuevaMigra)


                print(f"Instruccion {tipo_inst} cargado exitosamente")

                for migra in self.list_migrarVM:
                    migra.mostrar_datos()

            
            elif tipo_inst == ('procesarSolicitudes'):
                cantidad = inst.find('cantidad').text

                nuevoProce = Procesar(tipo_inst,cantidad)
                self.list_procesar.append(nuevoProce)

                for p in self.list_procesar:
                    p.mostrar_datos()

                print(f"Instruccion {tipo_inst} cargado exitosamente")




    





        
            
                
                

        
        






            

            
