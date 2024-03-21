import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import NUBO_GUIA_VALVULA
from utils.requiredColumns import get_required_columns

def case_nubo_guia_valvula(archivo_excel, messagebox):
    columnas = get_required_columns(NUBO_GUIA_VALVULA)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Los valores de 'medida' que quieres añadir al 'Código'
    medidas = ['STD' ,'003', '005', '010', '015']

    # Lista para almacenar los datos
    datos = []

    for _, row in df.iterrows():
        for medida in medidas:
            # Añadir un diccionario por cada combinación de código y medida
            datos.append({'Código': f"{row['Código']} {medida}", 'Marca': row['Marca'], 'Precio': round(row['Precio'], 2)})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'nubo_guia_valvula')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')