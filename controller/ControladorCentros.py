from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada
from modelos.CentroDatos import CentroDatos

class ControladorCentros: 
    def __init__(self):
        self.centrosDatos = ListaSimpleEnlazada()

    def crear_centros(self, id, nombre, pais, ciudad, cpu_total, ram_total_GB, almacenamiento_total_GB):
        nuevo_centro = CentroDatos(id,nombre,pais,ciudad,cpu_total,ram_total_GB,almacenamiento_total_GB)
        self.centrosDatos.agregar_dato(nuevo_centro)
        return
    

