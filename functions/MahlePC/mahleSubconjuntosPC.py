#Funciona. Pero queda el layout bug con NaN por el tema de las marcas de auto que estan escritas en CODIGO ANTIGUO (columna)

import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_SUBCONJUNTOS_PC
from utils.requiredColumns import get_required_columns

def case_mahle_subconjuntos_pc(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_SUBCONJUNTOS_PC)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Lista para almacenar los datos
    datos = []

    for _, row in df.iterrows():
        medidas = str(row['MEDIDAS']).split('-')
        
        for medida in medidas:
            medida = medida.strip()
            
            datos.append({'CODIGO': f"{row['CODIGO']}", 'APLICACION': row['APLICACION'],'MEDIDAS': medida, 'Precio': round(row['Precio'], 2)})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_subconjuntos_pc')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')