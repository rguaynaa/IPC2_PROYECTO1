from estructuras.ListaPrioridades import ListaCola 
from modelos.Solicitud import Solicitud
from modelos.MaquinaVirtual import MaquinaVirtual

class ControladorSolicitudes:
    def __init__(self):
        self.cola_solicitudes = ListaCola()

    def agregar_solicitud(self, id, cliente, tipo, prioridad, cpu, ram, alm, tiempo):
        nueva_sol = Solicitud(id, cliente, tipo, prioridad, cpu, ram, alm, tiempo)
        self.cola_solicitudes.insertar_dato(nueva_sol, prioridad)
        print(f"Solicitud {id} agregada con prioridad {prioridad}.")


    def ver_cola(self):
        print("\n--- COLA DE SOLICITUDES (Por Prioridad) ---")
        if self.cola_solicitudes.esta_vacia(): 
            print("La cola está vacía.")
            return

        actual = self.cola_solicitudes.primero
        pos = 1
        while actual:
            sol = actual.dato
            print(pos,f". Solicitud: {sol.id} - {sol.cliente} - ({sol.tipo}) - Prioridad: {sol.prioridad} \nEstado: {sol.estado} \n Recursos:")
            actual = actual.siguiente
            pos += 1


    def procesar_solicitud(self, controladorCentro):
        if self.cola_solicitudes.primero is None:
            print("No existe solicitudes pendientes.")
            return

        solicitud = self.cola_solicitudes.primero.dato

        centroDisponible = self.centro_mayor_recurso_disponible(controladorCentro, solicitud)

        if centroDisponible is None:
            print("No existe centro con recursos suficientes para la solicitud.")
            return

        mv_nueva = MaquinaVirtual(solicitud.id, centroDisponible.id, " ", solicitud.cpu, solicitud.ram_GB, solicitud.almacenamiento_GB, "")
        centroDisponible.vm.agregar_dato(mv_nueva)

        self.cola_solicitudes.extraer_urgente()
        print("Solicitud procesada ",solicitud.id)

    
    def procesar_varias_solicitudes(self, controladorCentro,cantidad):
        if self.cola_solicitudes.primero is None:
            print("No existe solicitudes pendientes.")
            return
        
        for i in range(cantidad):

            solicitud = self.cola_solicitudes.primero.dato

            centroDisponible = self.centro_mayor_recurso_disponible(controladorCentro, solicitud)

            if centroDisponible is None:
                print("No existe centro con recursos suficientes para la solicitud.")
                return

            mv_nueva = MaquinaVirtual(solicitud.id, centroDisponible.id, " ", solicitud.cpu, solicitud.ram_GB, solicitud.almacenamiento_GB, "")
            centroDisponible.vm.agregar_dato(mv_nueva)

            self.cola_solicitudes.extraer_urgente()
            print("Solicitud procesada ",solicitud.id)



    def centro_mayor_recurso_disponible(self, controladorCentro, solicitud=None):

        centroDisponible = None
        recursoMayor = -1

        actual = controladorCentro.lista_centros.primero

        while actual:
            centro = actual.dato

            if solicitud:
                if not (centro.cpu_disponible() >= solicitud.cpu and
                        centro.ram_disponible() >= solicitud.ram_GB and
                        centro.almacenamiento_disponible() >= solicitud.almacenamiento_GB):
                    actual = actual.siguiente
                    continue

            recurso = centro.cpu_disponible() + centro.ram_disponible() + centro.almacenamiento_disponible()
            if recurso > recursoMayor:
                recursoMayor = recurso
                centroDisponible = centro
            actual = actual.siguiente
        
        return centroDisponible


