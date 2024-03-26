#Este no se si es necesario!.

import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_ORING
from utils.requiredColumns import get_required_columns

def case_mahle_oring(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_ORING)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Lista para almacenar los datos
    datos = []

    for _, row in df.iterrows():
        if pd.isna(row["Precio"]) and row["Código MAHLE"] is not None:
            datos.append({'CODIGO': '', "Aplicación (motor)": row["Código MAHLE"], 'Precio': '' })
        else:
            medidas = str(row['Conjunto equivalente']).split('/')
        
            for medida in medidas:
                medida = medida.strip()
            
                datos.append({'Código MAHLE': f"{row['Código MAHLE']}", 'Aplicación (motor)': row['Aplicación (motor)'],'Aplicación (motor)': medida, 'Precio': round(row['Precio'], 2)})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_oring_')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')