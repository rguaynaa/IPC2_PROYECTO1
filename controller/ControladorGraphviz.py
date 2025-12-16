import graphviz
import os
import sys

class ControladorGraphviz:
    def __init__(self):
        self.output_dir="reportes_graphviz"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
    def render_reporte(self, dot, filename): #renderiza y guarda el archivo
        try:
            dot.render(f'{self.output_dir}/{filename}', view=True, format="png")
            print(f"Reporte'{filename}.png' generado exitosamente en la carpeta '{self.output_dir}'")
        except graphviz.backend.ExecutableNotFound:
            print("\nError: Graphviz no encontrado en el sistema")
        except Exception as e:
            print(f"Hubo un problema al generar Graphviz {e}")

    
    def generar_reporte_centros(self,controlador_centros):

        dot=graphviz.Digraph("Reporte_Centros",comment="Centros de Datos",graph_attr={'rankdir':'LR'})
        dot.attr('node', shape = 'box', style= 'filled', color = 'cyan')

        actual=controlador_centros.lista_centros.primero
        node_count= 0
        
        with dot.subgraph(name='cluster_centros') as c:
            c.attr(label='Lista de Centros de Datos')
            c.attr(bgcolor='lightgray')

            while actual is not None:
                centro = actual.dato
                node_id = f'C{centro.id}'
                
                label = f"ID:{centro.id}\n{centro.nombre}\n\nCPU: {centro.cpu_nucleos_total}\nRAM:{centro.ram_total_GB}GB\nAlmacenamiento:{centro.almacenamiento_total_GB}GB"
                c.node(node_id, label, fillcolor='lightgreen', shape='octagon')
                
                #simulacion de la lista simple enlazada
                if node_count > 0:
                    c.edge(prev_node_id, node_id, label='Siguiente')

                prev_node_id = node_id
                actual = actual.siguiente
                node_count += 1

        self.render_reporte(dot, 'reporte_centros_datos')


    def generar_reporte_vms(self, controlador_centros, id_centro):
        centro =controlador_centros.lista_centros.buscar_dato_por_id(id_centro, 'id')
        if not centro:
            print(f"Centro de Datos {id_centro} no encontrado")
            return

        dot=graphviz.Digraph(f"Maquinas Virtuales {id_centro}",comment=f"VMs en {centro.nombre}", graph_attr={'rankdir':'TB'})
        dot.attr('node', shape='box', style='filled')

        dot.node('root', f'CENTRO: {centro.id}\n{centro.nombre}', fillcolor='gold', shape='doubleoctagon')

        actual_vm= centro.vm.primero
        vm_count= 0
        
        with dot.subgraph(name='cluster_vms') as v:

            v.attr(label=f"Máquinas Virtuales en {centro.id}")
            
            while actual_vm is not None:

                vm= actual_vm.dato
                vm_node_id = f'VM{vm.id}'
                
                label=f"ID: {vm.id}\nSO: {vm.so}\nRecursos:\nCPU: {vm.cpu_nucleos} | RAM: {vm.ram_GB}GB"
                v.node(vm_node_id, label, fillcolor='lightblue')

                if vm_count == 0:
                    dot.edge('root', vm_node_id, label='Contiene VMs')
                
                #Enlazar VM anterior con la actual

                if  vm_count> 0:
                    v.edge(prev_vm_node_id,vm_node_id, label= 'Siguiente VM')

                prev_vm_node_id = vm_node_id
                actual_vm = actual_vm.siguiente
                vm_count += 1
            
        self.render_reporte(dot, f'reporte_vms_{id_centro}')

    def generar_reporte_contenedores(self,controlador_vm,id_vm ):
        vm = controlador_vm.lista_vm.buscar_dato_por_id(id_vm,'id' )
        if not vm:
            print(f"Error: Máquina Virtual {id_vm} no encontrada. No se generará el reporte.")
            return

        dot = graphviz.Digraph(f'Contenedores_{id_vm}', comment=f'Contenedores en {id_vm}', graph_attr={'rankdir': 'LR'})
        dot.attr('node', shape='box', style='filled')

        dot.node('root', f'VM: {vm.id}\nSO: {vm.so}', fillcolor='orange', shape='box3d') #nodo
        
        actual_cont = vm.contenedores.primero
        cont_count = 0
        
        with dot.subgraph(name='cluster_contenedores') as cont_sub:
            cont_sub.attr(label=f'Contenedores en VM {vm.id}')
            cont_sub.attr(rankdir='TB') #grafica de arriba hacia abajo
            
            while actual_cont is not None:
                cont = actual_cont.dato
                cont_node_id = f'CONT{cont.id}'
                
                # color del estado
                color_map= {"Activo":'greenyellow', "Pausado":'yellow' , "Reiniciando": 'red'}
                fill_color= color_map.get(cont.estado, 'gray')
                
                label = f"ID: {cont.id}\n{cont.nombre}\nEstado: {cont.estado}\nCPU: {cont.cpu_porcentaje}% | RAM: {cont.ram_MB}MB"
                cont_sub.node(cont_node_id, label, fillcolor=fill_color, shape='note')
                
                # Enlazar VM con el primer Contenedor
                if cont_count == 0:
                    dot.edge('root', cont_node_id, label='Despliegue')
                
                # Enlazar Contenedor anterior con el actual
                if cont_count > 0:
                    cont_sub.edge(prev_cont_node_id, cont_node_id, label='Siguiente Cont.')

                prev_cont_node_id = cont_node_id
                actual_cont = actual_cont.siguiente
                cont_count += 1
            
        self.render_reporte(dot, f'reporte_contenedores_{id_vm}')


    def generar_reporte_solicitudes(self, controlador_solicitudes):
        dot = graphviz.Digraph('ColaSolicitudes', comment='Cola de Solicitudes por Prioridad', graph_attr={'rankdir': 'TB'})
        dot.attr('node', shape='box', style='filled')

        actual = controlador_solicitudes.cola_solicitudes.primero
        sol_count = 0
        
        #nodo frente a la cola
        dot.node('HEAD', 'FRENTE DE COLA\n(Mayor Prioridad)', shape='box', fillcolor='red', fontcolor='white')
        
        while actual is not None:
            sol = actual.dato
            sol_node_id = f'SOL{sol.id}'
            
            #Color basado en la prioridad
            priority_value = sol.prioridad if hasattr(sol, 'prioridad') else 1 
            
            #egun la prioridad va de un color mas claro a mas oscuro
            color_int = 255 - (priority_value * 25) 
            priority_color = f'#33{color_int:02X}FF'
                        
            label = (f"ID: {sol.id}\nCliente: {sol.cliente}\nTipo: {sol.tipo}\nPRIORIDAD: {priority_value}\n"
                     f"CPU: {sol.cpu} | RAM: {sol.ram_GB}GB\nAlmacenamiento: {sol.almacenamiento_GB}GB\n"
                     f"Tiempo Est.: {sol.tiempo_estimado} min")
            
            dot.node(sol_node_id, label, fillcolor=priority_color, shape='note')
            
            #orden de la cola
            if sol_count == 0:
                dot.edge('HEAD', sol_node_id, label='Procesar Primero')
            else:
                dot.edge(prev_sol_node_id, sol_node_id, label='Siguiente')

            prev_sol_node_id = sol_node_id
            actual = actual.siguiente
            sol_count += 1
            
        self.render_reporte(dot, 'reporte_cola_solicitudes')