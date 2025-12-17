class Contenedor:
    def __init__(self, id, nombre, imagen, cpu_porcentaje, ram_MB, puerto):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.cpu_porcentaje = cpu_porcentaje
        self.ram_MB = ram_MB
        self.puerto = puerto
        self.estado = "Activo"

    def __str__(self):
        return f"{self.id}"
        
    def obtener_id_legible(self):
        return self.id

    def mostrar_datos(self):
        print(f'\nContenedor:{self.id}-{self.nombre} ({self.imagen})-Puerto:{self.puerto} \nEstado: {self.estado} \nCPU: {self.cpu_porcentaje}\nRAM:  {self.ram_MB}' )