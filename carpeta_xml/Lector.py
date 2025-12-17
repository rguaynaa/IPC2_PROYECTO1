from modelos.Contenedor import Contenedor
from modelos.Instrucciones import Instruccion
import xml.etree.ElementTree as ET
from modelos.CentroDatos import CentroDatos
from modelos.MaquinaVirtual import MaquinaVirtual
from controller.ControladorVM import ControladorVM
from controller.ControladorCentros import ControladorCentros
from controller.ControladorSolicitudes import ControladorSolicitudes
from controller.ControladorInstrucciones import ControladroInstrucciones


class Lector:
    def __init__(self, controladorVM=None, controladorCentros=None, controladorSolicitudes = None, controllerInstruccion = None):
        self.controladorVM = controladorVM if controladorVM is not None else ControladorVM()
        self.controladorCentros = controladorCentros if controladorCentros is not None else ControladorCentros()
        self.controladorSolicitudes = controladorSolicitudes if controladorSolicitudes is not None else ControladorSolicitudes()
        self.controllerInstruccion = controllerInstruccion if controllerInstruccion is not None else ControladroInstrucciones()
        
    
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
            

            print(f"Centro {id_centro} cargado.")

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
                print(f" MaquinaVirtual {id_mv} cargado.")


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

                    print(f"  Contenedor {id_cont} cargado.")



    def cargar_solicitudes(self,root):
        solicitudes_xml = root.find('.//solicitudes')
        if solicitudes_xml is None:
            return
        
        for sol in solicitudes_xml.findall('solicitud'):
            id_sol = sol.get('id')

            cliente = sol.find('cliente').text
            tipo = sol.find('tipo').text
            prioridad = int(sol.find('prioridad').text)

            recursos = sol.find('recursos')
            cpu = int(recursos.find('cpu').text)
            ram = int(recursos.find('ram').text)
            almacenamiento = int(recursos.find('almacenamiento').text)

            tiempo = int(sol.find('tiempoEstimado').text)

            self.controladorSolicitudes.agregar_solicitud(id_sol,cliente,tipo,prioridad,cpu,ram,almacenamiento,tiempo)


    def cargar_instrucciones(self, root):

        print("=== Ejecutando Instrucciones ===")
        instrucciones_xml = root.find('.//instrucciones')

        if instrucciones_xml is None:
            return
        
        for inst in instrucciones_xml.findall('instruccion'):
            tipo_inst = inst.get('tipo')

            if tipo_inst == ('crearVM'):

                id_vm = inst.find('id').text
                id_centro = inst.find('centro').text
                so = inst.find('so').text
                cpu = int(inst.find('cpu').text)
                ram = int(inst.find('ram').text)
                almacenamiento = int(inst.find('almacenamiento').text)

                nueva_VM = MaquinaVirtual(id_vm,id_centro,so,cpu,ram,almacenamiento,"")
                nuevaInst = Instruccion(tipo_inst,id_vm,id_centro,so,cpu,ram,almacenamiento," ",0)

                self.controllerInstruccion.crear_instrucciones(nuevaInst)

                self.controladorCentros.agregar_vm(nueva_VM, id_centro)

                print(f"Instruccion {tipo_inst} ejecutado exitosamente")

            
            elif tipo_inst == ('migrarVM'):
                id_vm = inst.find('vmId').text
                id_centro = inst.find('centroOrigen').text
                id_centro_destino = inst.find('centroDestino').text

                nuevaInst = Instruccion(tipo_inst,id_vm,id_centro," ",0,0,0,id_centro_destino,0)

                self.controllerInstruccion.crear_instrucciones(nuevaInst)
                
                self.controladorVM.migrar_vm(self.controladorCentros,id_vm,id_centro_destino)

                print(f"Instruccion {tipo_inst} ejecutado exitosamente")

            
            elif tipo_inst == ('procesarSolicitudes'):
                cantidad = int(inst.find('cantidad').text)

                nuevaInst = Instruccion(tipo_inst," "," "," ",0,0,0," ",cantidad)

                self.controllerInstruccion.crear_instrucciones(nuevaInst)

                self.controladorSolicitudes.procesar_varias_solicitudes(self.controladorCentros, cantidad)

                print(f"Instruccion {tipo_inst} ejecutado exitosamente")



    





        
            
                
                

        
        






            

            
