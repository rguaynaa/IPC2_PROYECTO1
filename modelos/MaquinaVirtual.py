from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class MaquinaVirtual:
    def __init__(self,id, id_centro, so, cpu_nucleos, ram_GB, almacenamiento_GB,ip):
        self.id = id
        self.id_centro = id_centro
        self.so = so
        self.cpu_nucleos = cpu_nucleos
        self.ram_GB = ram_GB
        self.almacenamiento_GB = almacenamiento_GB
        self.ip = ip
        self.contenedores = ListaSimpleEnlazada()
        self.estado = "Activa"

    def __str__(self):
        return f"VM ID: {self.id}"
        
    def obtener_id_legible(self):
        return self.id
    

    def mostrar_datos(self):
        print("")
        print("VM: ",self.id," - ",self.so,"(", "CPU: ",self.cpu_nucleos,"RAM: ",self.ram_GB,")")
        print("Estado: ",self.estado)
        print("IP: ",self.ip)
        print("Centro Asignado: ",self.id_centro) 
        print("Contenedores: ",self.contenedores.obtener_longitud())


    # Validaciones de recursos para crear un nuevos contenedores
    def recursos_cpu_disponible(self):
        usado = 0
        porcentaje_disponible = 100
        actual = self.contenedores.primero

        while actual:
            usado += actual.dato.cpu_porcentaje
            actual = actual.siguiente
        return porcentaje_disponible - usado #Devuelve el porcentaje disponible


    def recursos_ram_disponible(self):
        usado_en_MB = 0
        actual = self.contenedores.primero

        # 1 GB son 1024 MG (MV está en GB y contenedor en MG)
        while actual:
            usado_en_MB += actual.dato.ram_MB
            actual = actual.siguiente
        return ((self.ram_GB * 1024) - usado_en_MB)

