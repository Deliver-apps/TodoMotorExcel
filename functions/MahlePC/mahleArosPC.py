#no accede a las columnas RECTIF. RECAMBIO y Precio porque no estan arriba del todo, estan en el row(2), sigo con este despues. Hay 2 columnas con Precio y diferentes var
import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_AROS_PC
from utils.requiredColumns import get_required_columns

def case_mahle_aros_pc(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_AROS_PC)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    datos = []

    for _, row in df.iterrows():
        medidas = str(row['MEDIDAS']).split('-')
        
        for medida in medidas:
            medida = medida.strip()
            datos.append({
            'APLICACION': row['APLICACION'],
            'MEDIDAS': medida,
            'RECTIF': row['RECTIF.'],
            'RECAMBIO': row['RECAMBIO'],
            'Precio': round(row['Precio'], 2)
            })

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_aros_pc')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')