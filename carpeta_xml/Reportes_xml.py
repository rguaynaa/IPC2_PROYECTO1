import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime


class ReporteXML:
    def __init__(self, controlador_centros):
        self.controlador_centros = controlador_centros

    def generar_salida(self, ruta_salida):

        try:
            root = ET.Element('resultadoCloudSync')

            timestamp = ET.SubElement(root, 'timestamp')
            timestamp.text = datetime.now().isoformat()

            estado_centros = ET.SubElement(root, 'estadoCentros')

            total_vms = 0
            total_contenedores = 0

            # Si no hay lista de centros o está vacía, se generan las secciones vacías
            if not hasattr(self.controlador_centros, 'lista_centros') or self.controlador_centros.lista_centros.primero is None:
                estadisticas = ET.SubElement(root, 'estadisticas')
                vms_act = ET.SubElement(estadisticas, 'vmsActivas')
                vms_act.text = str(total_vms)
                conts = ET.SubElement(estadisticas, 'contenedoresTotales')
                conts.text = str(total_contenedores)

                pretty = minidom.parseString(ET.tostring(root, 'utf-8')).toprettyxml(indent='  ')
                with open(ruta_salida, 'w', encoding='utf-8') as f:
                    f.write(pretty)
                return True, 'Archivo generado (no se encontraron centros)'

            actual = self.controlador_centros.lista_centros.primero


            while actual:
                centro = actual.dato
                centro_elem = ET.SubElement(estado_centros, 'centro', {'id': str(centro.id)})

                nombre = ET.SubElement(centro_elem, 'nombre')
                nombre.text = str(centro.nombre)

                recursos = ET.SubElement(centro_elem, 'recursos')

                cpu_total = ET.SubElement(recursos, 'cpuTotal')
                cpu_total.text = str(centro.cpu_nucleos_total)
                cpu_disp = ET.SubElement(recursos, 'cpuDisponible')
                cpu_disp.text = str(centro.cpu_disponible())

                # Cálculo de porcentaje de uso de CPU
                try:
                    if centro.cpu_nucleos_total and centro.cpu_nucleos_total > 0:
                        cpu_util = ((centro.cpu_nucleos_total - centro.cpu_disponible()) / centro.cpu_nucleos_total) * 100
                    else:
                        cpu_util = 0.0
                except Exception:
                    cpu_util = 0.0
                cpu_util_elem = ET.SubElement(recursos, 'cpuUtilizacion')
                cpu_util_elem.text = f"{cpu_util:.2f}%"

                ram_total = ET.SubElement(recursos, 'ramTotal')
                ram_total.text = str(centro.ram_total_GB)
                ram_disp = ET.SubElement(recursos, 'ramDisponible')
                ram_disp.text = str(centro.ram_disponible())

                try:
                    if centro.ram_total_GB and centro.ram_total_GB > 0:
                        ram_util = ((centro.ram_total_GB - centro.ram_disponible()) / centro.ram_total_GB) * 100
                    else:
                        ram_util = 0.0
                except Exception:

                    ram_util = 0.0
                ram_util_elem = ET.SubElement(recursos, 'ramUtilizacion')
                ram_util_elem.text = f"{ram_util:.2f}%"

                # Cantidad de VMs y contenedores
                cantidad_vms = centro.vm.obtener_longitud()
                cantidad_contenedores = 0
                vm_actual = centro.vm.primero
                
                while vm_actual:
                    mv = vm_actual.dato
                    # contar contenedores de esta VM
                    cantidad_contenedores += mv.contenedores.obtener_longitud()
                    vm_actual = vm_actual.siguiente

                total_vms += cantidad_vms
                total_contenedores += cantidad_contenedores

                c_vms = ET.SubElement(centro_elem, 'cantidadVMs')
                c_vms.text = str(cantidad_vms)
                c_conts = ET.SubElement(centro_elem, 'cantidadContenedores')
                c_conts.text = str(cantidad_contenedores)

                actual = actual.siguiente


            estadisticas = ET.SubElement(root, 'estadisticas')
            vms_act = ET.SubElement(estadisticas, 'vmsActivas')
            vms_act.text = str(total_vms)
            conts = ET.SubElement(estadisticas, 'contenedoresTotales')
            conts.text = str(total_contenedores)

            # Formatear y escribir XML
            rough = ET.tostring(root, 'utf-8')
            reparsed = minidom.parseString(rough)
            pretty = reparsed.toprettyxml(indent='  ')

            with open(ruta_salida, 'w', encoding='utf-8') as f:
                f.write(pretty)

            return True, f'Reporte generado correctamente en {ruta_salida}'

        except Exception as e:
            return False, f'Error al generar salida XML: {str(e)}'