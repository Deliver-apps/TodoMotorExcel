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
        if pd.isna(row["Precio"]) and row["MAHLE"] is not None:
            datos.append({'MAHLE': '', "Aplicación": row["MAHLE"],'Medidas': '', 'Precio': '' })
        else:
            medidas = str(row['Medidas']).split('/')
            ##Float para redondear (test)
            try:
                precio = round(float(row['Precio']), 2)
            except ValueError:
                precio = ''
        
            for medida in medidas:
                medida = medida.strip()
                
                datos.append({'MAHLE': f"{row['MAHLE']}",'Medidas': medida, 'Aplicación': row['Aplicación'], 'Precio': precio})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_camisa_mh')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')