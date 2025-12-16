class Instruccion:
    def __init__(self, tipo, id_VM, id_centro, so, cpu, ram, almacenamiento,centro_destino,cantidad):
        self.tipo = tipo
        self.id_VM = id_VM
        self.id_centro = id_centro
        self.so = so
        self.cpu = cpu
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.centro_destino = centro_destino
        self.cantidad = cantidad


    def mostrar_datos(self):
        print(f'\nTipo: {self.tipo} - Id MV: {self.id_VM} - Id Centro : {self.id_centro} \nSO: {self.so}')

    def mostrar_datos(self):
        print(f'\nTipo: {self.tipo} - Id MV: {self.id_VM} - Id Centro : {self.id_centro} \nCentro Destino: {self.id_centro_destino}')

    def mostrar_datos(self):
        print(f'\nTipo: {self.tipo} \nCantidad: {self.cantidad}')
        