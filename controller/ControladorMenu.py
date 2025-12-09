class ControladorMenu:

    def __init__(self):
        pass


    def cargar_xml(tipo):
        nombre_archivo = input(f'Ingrese el nombre del archvo "{tipo}.xml": ').strip()
        if nombre_archivo == '':
            return ''
        ruta_archivo = f'{nombre_archivo}'
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                pass
            return ruta_archivo
        except FileNotFoundError:
            print(f'Archivo no encontrado: {ruta_archivo}')
            return ''