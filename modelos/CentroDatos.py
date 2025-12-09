from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class CentroDatos:
    def __init__(self, id, nombre, pais, ciudad, cpu_total, ram_total_GB, almacenamiento_total_GB):
        self.id = id
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu_total = cpu_total
        self.ram_total_GB = ram_total_GB
        self.almacenamiento_total_GB = almacenamiento_total_GB
        self.vm = ListaSimpleEnlazada() # se va elmacenar los vm de Centro de Datos.

    def mostrar_datos(self):
        print(f'\nCentro: {self.nombre} ({self.id}) - {self.pais}, {self.ciudad} \nUbicacion: {self.pais}, {self.ciudad} \nCPU: {self.cpu_total} \nRAM: {self.ram_total_GB} \nAlmacen: {self.almacenamiento_total_GB}')
    
    