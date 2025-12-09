from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class MaquinaVirtual:
    def __init__(self,id, id_centro, so, cpu, ram_GB, almacenamiento_GB,ip):
        self.id = id
        self.id_centro = id_centro
        self.so = so
        self.cpu = cpu
        self.ram_GB = ram_GB
        self.almacenamiento_GB = almacenamiento_GB
        self.ip = ip
        self.contenedores = ListaSimpleEnlazada() #Acá se va estar almacenando los contenedores.
        self.estado = "activo"
    
    def mostrar_datos(self):
        print(f'\nMV: {self.id} - {self.so} (CPU: {self.cpu}, RAM: {self.ram_GB}) \nEstado: {self.estado} \nIP: {self.ip} \nContenedores: ')
