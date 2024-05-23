# Va a tener que copiar manualmente el nombre de las columnas tal como viene en la original (solo los que necesite) y pegar abajo toda la data completa.
import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_AROS_PC
from utils.requiredColumns import get_required_columns

# def leer_archivo_excel_header(archivo_excel, messagebox):
#     try:
#         df1 = pd.read_excel(archivo_excel, usecols=['APLICACION', 'MEDIDAS', 'CODIGO'], header=1)

#         df2 = pd.read_excel(archivo_excel, usecols=['RECTIF', 'Precio RECTIF', 'RECAMBIO', 'Precio RECAMBIO'], header=0)

#         df = pd.concat([df1, df2], axis=1)
#         return df
#     except Exception as e:
#         messagebox.showwarning("Warning", "Error al leer el archivo Excel. Asegúrate de que el archivo es un archivo Excel válido y cumpla con los formatos establecidos.")
#         print(f"Error: {e}")
#         return None

def case_mahle_aros_pc(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_AROS_PC)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    datos = []
    
    for _, row in df.iterrows():
        if (pd.isna(row["PRECIO RECAMBIO"]) or row["PRECIO RECAMBIO"] == 0) and (pd.isna(row["PRECIO RECTIF"]) or row["PRECIO RECTIF"] == 0) and pd.isna(row['MEDIDAS']) and row["APLICACION"] is not None:
            datos.append({
            'APLICACION': row['APLICACION'],
            })
        elif pd.notna(row['MEDIDAS']):
            medidas = str(row['MEDIDAS']).split('-')
            precio_rectif = round(row['PRECIO RECTIF'], 2) if (pd.notna(row['PRECIO RECTIF']) or row["PRECIO RECTIF"] == 0) else ''
            precio_recambio = round(row['PRECIO RECAMBIO'], 2) if (pd.notna(row['PRECIO RECAMBIO']) or row ["PRECIO RECAMBIO"] == 0) else ''

            for medida in medidas:
                medida = medida.strip()
                rectif_medida = f"{row['RECTIF']} {medida}" if pd.notna(row['RECTIF']) else ''
                recambio_medida = f"{row['RECAMBIO']} {medida}" if pd.notna(row['RECAMBIO']) else ''
                datos.append({
                    'APLICACION': row['APLICACION'],
                    'Codigo RECTIF - Medidas': rectif_medida,
                    'PRECIO RECTIF': precio_rectif,
                    'Codigo RECAMBIO - Medidas': recambio_medida,
                    'PRECIO RECAMBIO': precio_recambio,
                })

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_aros_pc')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')
