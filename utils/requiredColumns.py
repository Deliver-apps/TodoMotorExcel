from constants.empresas import MAHLE_AROS_PC, MAHLE_SUBCONJUNTOS_PC, MAHLE_CONJUNTOS, NUBO_ASIENTO_VALVULA, NUBO_GUIA_VALVULA


def get_required_columns(opcion):
    # INSERTAR COLUMNAS POR CADA DEF
    opciones = {
        NUBO_GUIA_VALVULA: ['Código', 'Marca', 'Precio'],
        NUBO_ASIENTO_VALVULA: ['Código', 'Marca', 'Precio'],
        MAHLE_CONJUNTOS: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
        MAHLE_SUBCONJUNTOS_PC: ['CODIGO', 'APLICACION', 'MEDIDAS', 'Precio'],
        MAHLE_AROS_PC: ['APLICACION', 'MEDIDAS', 'RECTIF.', 'RECAMBIO', 'Precio RECTIF.', 'Precio RECAMBIO']
        # añadir...
    }
    return opciones.get(opcion, [])