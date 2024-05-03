from constants.empresas import  DECE, LEVA_IM, BUJE_LEVA, FEDERAL_SUBCONJUNTOS, MAHLE_COJINETES_CL,MAHLE_TAPAS_MH, MAHLE_JUNTAS_MH,MAHLE_COJINETES_PC,MAHLE_AROS_CL, MAHLE_CAMISA_CL, MAHLE_SUBCONJUNTOS_CL, MAHLE_CONJUNTOS_CL, MAHLE_ORING, MAHLE_AROS_TH, MAHLE_AROS_RECTIF_MH, MAHLE_AROS_MH, MAHLE_COJINETES_MH, MAHLE_CAMISA_MH, MAHLE_SUBCONJUNTOS_MH, MAHLE_AROS_PC, MAHLE_SUBCONJUNTOS_PC, MAHLE_CONJUNTOS_MH, NUBO_ASIENTO_VALVULA, NUBO_GUIA_VALVULA

def get_required_columns(opcion):
    # INSERTAR COLUMNAS POR CADA DEF
    opciones = {
        #NUBO
        NUBO_GUIA_VALVULA: ['Código', 'Marca', 'Precio', 'Modelo (Aplicación)'],
        NUBO_ASIENTO_VALVULA: ['Código', 'Marca', 'Precio', 'Modelo (Aplicación)'],
        
        #MAHLE PC
        MAHLE_SUBCONJUNTOS_PC: ['CODIGO ANTIGUO', 'APLICACION', 'MEDIDAS', 'Precio'],
        MAHLE_AROS_PC: ['APLICACION', 'MEDIDAS', 'Precio'],
        MAHLE_COJINETES_PC: ['Marca', 'Código Corto', 'Aplicación', 'Precio'],
        #MAHLE MH
        MAHLE_CONJUNTOS_MH: ['Artículo', 'Ref.', 'Precio', 'Aplicación'],
        MAHLE_SUBCONJUNTOS_MH: ['Artículo', 'Ref.', 'Precio', 'Aplicación'],
        MAHLE_CAMISA_MH: ['MAHLE', 'Medidas', 'PC', 'Precio', 'Aplicación'],
        MAHLE_COJINETES_MH: ['Artículo', 'Ref.', 'Precio', 'Aplicación'],
        MAHLE_AROS_MH: ['Artículo', 'Ref.', 'Precio', 'Aplicación'],
        MAHLE_AROS_RECTIF_MH: ['Artículo', 'Ref.', 'Precio', 'Aplicación'],
        MAHLE_AROS_TH: ['CODIGO', 'APLICACION', 'MEDIDAS', 'PRECIO LISTA '],
        MAHLE_ORING: ['Código MAHLE', 'Aplicación (motor)', 'Conjunto equivalente', 'Precio'],
        MAHLE_JUNTAS_MH: ['Código MAHLE', 'Aplicación', 'Material', 'Precio'],
        MAHLE_TAPAS_MH: ['Código MAHLE', 'Aplicación', 'Material', 'Precio'],

        #MAHLE CL
        MAHLE_CONJUNTOS_CL: ['Artículo', 'Ref.', 'Aplicación', 'Precio'],
        MAHLE_SUBCONJUNTOS_CL: ['Artículo', 'Ref.', 'Aplicación', 'Precio'],
        MAHLE_CAMISA_CL: ['Artículo', 'Ref.', 'Aplicación', 'Precio'],
        MAHLE_AROS_CL: ['Artículo', 'Ref.', 'Aplicación', 'Precio'],
        MAHLE_COJINETES_CL: ['Artículo', 'Aplicación', 'Precio'],

        #FEDERAL
        FEDERAL_SUBCONJUNTOS: ['APLICACIÓN', 'CÓDIGO'],

        #BUJE LEVA y OTROS
        BUJE_LEVA: ['Codigo', "Descripcion", 'Precio'],
        LEVA_IM: ['Cod. IM', 'Descripción', 'Precio'],
        DECE: ['CODIGO DECE', 'MOTOR ; Diametro Perno ', 'MEDIDAS', 'Precios Netos']
    }
    return opciones.get(opcion, [])