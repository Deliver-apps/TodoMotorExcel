import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_CAMISA_MH
from utils.requiredColumns import get_required_columns

def case_mahle_camisa_mh(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_CAMISA_MH)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Lista para almacenar los datos
    datos = []

    for _, row in df.iterrows():
        medidas = str(row['Medidas']).split('/')
        
        for medida in medidas:
            medida = medida.strip()
            
            datos.append({'MAHLE': f"{row['MAHLE']}",'Medidas': medida, 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_camisa_mh')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')