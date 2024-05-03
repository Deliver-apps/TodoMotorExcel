import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_AROS_TH
from utils.requiredColumns import get_required_columns

def case_mahle_aros_th(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_AROS_TH)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Lista para almacenar los datos
    datos = []

    for _, row in df.iterrows():
        if pd.isna(row["PRECIO LISTA "]) and row["APLICACION"] is not None:
            datos.append({'CODIGO - MEDIDA': '', "APLICACION": row["APLICACION"], 'PRECIO LISTA ': '' })
        else:
            medidas = str(row['MEDIDAS']).split('-')
        
            for medida in medidas:
                medida = medida.strip()
            
                datos.append({'CODIGO - MEDIDA': f"{row['CODIGO']} {medida}", 'APLICACION': row['APLICACION'],'PRECIO LISTA ': round(row['PRECIO LISTA '], 2)})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_aros_th')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')