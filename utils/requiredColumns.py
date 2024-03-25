from constants.empresas import MAHLE_AROS_RECTIF_MH, MAHLE_AROS_MH, MAHLE_COJINETES_MH, MAHLE_CAMISA_MH, MAHLE_SUBCONJUNTOS_MH, MAHLE_AROS_PC, MAHLE_SUBCONJUNTOS_PC, MAHLE_CONJUNTOS_MH, NUBO_ASIENTO_VALVULA, NUBO_GUIA_VALVULA

def get_required_columns(opcion):
    # INSERTAR COLUMNAS POR CADA DEF
    opciones = {
        #NUBO
        NUBO_GUIA_VALVULA: ['Código', 'Marca', 'Precio'],
        NUBO_ASIENTO_VALVULA: ['Código', 'Marca', 'Precio'],
        
        #MAHLE PC
        MAHLE_SUBCONJUNTOS_PC: ['CODIGO', 'APLICACION', 'MEDIDAS', 'Precio'],
        MAHLE_AROS_PC: ['APLICACION', 'MEDIDAS', 'RECTIF.', 'RECAMBIO', 'Precio'],
        
        #MAHLE MH
        MAHLE_CONJUNTOS_MH: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
        MAHLE_SUBCONJUNTOS_MH: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
        MAHLE_CAMISA_MH: ['MAHLE', 'Medidas', 'Precio', "Aplicación"],
        MAHLE_COJINETES_MH: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
        MAHLE_AROS_MH: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
        MAHLE_AROS_RECTIF_MH: ['Artículo', 'Ref.', 'Precio', "Aplicación"],
    }
    return opciones.get(opcion, [])