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
        print("CPU: ",self.cpu_disponible(),"/",self.cpu_nucleos_total) #Pendiente de configurar
        print("RAM: ",self.ram_disponible(),"/",self.ram_total_GB,"GB") #Pendiente de configurar
        print("Almacenamiento: ",self.almacenamiento_disponible(),"/",self.almacenamiento_total_GB,"TB") #Pendiente de configurar 
        print("VMs activas: ",self.vm.obtener_longitud())
    
    def cpu_disponible(self):
        usado = 0
        actual = self.vm.primero
        while actual:
            usado += actual.dato.cpu_nucleos
            actual = actual.siguiente
        return self.cpu_nucleos_total - usado
    
    def ram_disponible(self):
        usado = 0
        actual = self.vm.primero
        while actual:
            usado += actual.dato.ram_GB
            actual = actual.siguiente
        return self.ram_total_GB - usado
    
    def almacenamiento_disponible(self):
        usado = 0
        actual = self.vm.primero
        while actual:
            usado += actual.dato.almacenamiento_GB
            actual = actual.siguiente
        return self.almacenamiento_total_GB - usado
    
    def porcentaje_uso_cpu(self):
        if self.cpu_nucleos_total > 0:
            procentaje = ((self.cpu_nucleos_total - self.cpu_disponible)/ self.cpu_nucleos_total * 100)
            return procentaje
        else:
            return 0
            


    
