from constants.empresas import MAHLE_COJINETES_PC, MAHLE_CONJUNTOS, NUBO_ASIENTO_VALVULA, NUBO_GUIA_VALVULA


def get_required_columns(opcion):
    # INSERTAR COLUMNAS POR CADA DEF
    opciones = {
        NUBO_GUIA_VALVULA: ['Código', 'Marca', 'Precio'],
        NUBO_ASIENTO_VALVULA: ['Código', 'Marca', 'Precio'],
        MAHLE_CONJUNTOS: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
        MAHLE_COJINETES_PC: ['Marca', 'Código Corto', 'Aplicación', 'Precio']
        # añadir...
    }
    return opciones.get(opcion, [])