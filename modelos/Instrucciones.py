class CrearVM:
    def __init__(self, tipo, id_VM, id_centro, so, cpu, ram, almacenamiento):
        self.tipo = tipo
        self.id_MV = id_VM
        self.id_centro = id_centro
        self.so = so
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento


class MigrarMV:
    def __init__(self, tipo, id_MV, id_centro, id_centro_destino):
        self.tipo = tipo
        self.id_MV = id_MV
        self.id_centro = id_centro
        self.id_centro_destino = id_centro_destino

class Procesar:
    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad
        
        