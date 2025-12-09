class CrearVM:
    def __init__(self, tipo, id_VM, id_centro, so, cpu, ram, almacenamiento):
        self.tipo = tipo
        self.id_VM = id_VM
        self.id_centro = id_centro
        self.so = so
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento

    def mostrar_datos(self):
        print(f'\nTipo: {self.tipo} - Id MV: {self.id_VM} - Id Centro : {self.id_centro} \nSO: {self.so}')


class MigrarVM:
    def __init__(self, tipo, id_VM, id_centro, id_centro_destino):
        self.tipo = tipo
        self.id_VM = id_VM
        self.id_centro = id_centro
        self.id_centro_destino = id_centro_destino

    def mostrar_datos(self):
        print(f'\nTipo: {self.tipo} - Id MV: {self.id_VM} - Id Centro : {self.id_centro} \nCentro Destino: {self.id_centro_destino}')

class Procesar:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
    
    def mostrar_datos(self):
        print(f'\nTipo: {self.tipo} \nCantidad: {self.cantidad}')
        