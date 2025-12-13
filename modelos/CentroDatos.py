from estructuras.ListaSimpleEnlazada import ListaSimpleEnlazada

class CentroDatos:
    def __init__(self, id, nombre, pais, ciudad, cpu_nucleos_total, ram_total_GB, almacenamiento_total_GB):
        self.id = id
        self.nombre = nombre
        self.pais = pais
        self.ciudad = ciudad
        self.cpu_nucleos_total = cpu_nucleos_total
        self.ram_total_GB = ram_total_GB
        self.almacenamiento_total_GB = almacenamiento_total_GB
        self.vm = ListaSimpleEnlazada() # se va elmacenar los vm de Centro de Datos.

    def mostrar_datos(self):
        print("Centro: ",self.nombre, "(",self.id,")", "-", self.ciudad, ",", self.pais)
        print("Ubicación: ",self.ciudad, "," ,self.pais)
        print("CPU: ",self.cpu_nucleos_total,"/100") #Pendiente de configurar
        print("RAM: ",self.ram_total_GB,"/100") #Pendiente de configurar
        print("Almacenamiento: ",self.almacenamiento_total_GB,"/100 TB") #Pendiente de configurar 
        print("VMs activas: ",self.vm.obtener_longitud())
    
    
