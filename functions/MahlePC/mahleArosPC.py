#Va a tener que cambiar el valor de Precio en el excel por Precio RECTIF y Precio RECAMBIO. Todavia tiene bug al iterar.
import pandas as pd
from utils.excelHandler import guardar_df_en_excel
# from constants.empresas import MAHLE_AROS_PC
# from utils.requiredColumns import get_required_columns

def leer_archivo_excel_header(archivo_excel, messagebox):
    try:
        df1 = pd.read_excel(archivo_excel, usecols=['APLICACION', 'MEDIDAS', 'CODIGO'], header=0)

        df2 = pd.read_excel(archivo_excel, usecols=['RECTIF.', 'Precio RECTIF', 'RECAMBIO', 'Precio RECAMBIO'], header=1)

        df = pd.concat([df1, df2], axis=1)
        return df
    except Exception as e:
        messagebox.showwarning("Warning", "Error al leer el archivo Excel. Asegúrate de que el archivo es un archivo Excel válido y cumpla con los formatos establecidos.")
        print(f"Error: {e}")
        return None

def case_mahle_aros_pc(archivo_excel, messagebox):
    df = leer_archivo_excel_header(archivo_excel, messagebox)
    datos = []

    for _, row in df.iterrows():
        # if (pd.isna(row["Precio"]) or row["Precio"] == 0) and pd.isna(row['MEDIDAS']) and row["APLICACION"] is not None:
        #         datos.append({
        #         'Codigo RECTIF - Medidas': '',
        #         'Codigo RECAMBIO - Medidas': '',
        #         'APLICACION': row['APLICACION'],
        #         'Precio': '' 
        #         })
        # else:
        if pd.notna(row['MEDIDAS']):
            medidas = str(row['MEDIDAS']).split('-')
            precio_rectif = round(row['Precio RECTIF'], 2) if pd.notna(row['Precio RECTIF']) else ''
            precio_recambio = round(row['Precio RECAMBIO'], 2) if pd.notna(row['Precio RECAMBIO']) else ''
            
            for medida in medidas:
                medida = medida.strip()
                rectif_medida = f"{row['RECTIF.']} {medida}" if pd.notna(row['RECTIF.']) else ''
                recambio_medida = f"{row['RECAMBIO']} {medida}" if pd.notna(row['RECAMBIO']) else ''
                datos.append({
                'Codigo RECTIF - Medidas': rectif_medida,
                'Codigo RECAMBIO - Medidas': recambio_medida,
                'APLICACION': row['APLICACION'],
                'Precio RECTIF': precio_rectif,
                'Precio RECAMBIO': precio_recambio,
                })

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_aros_pc')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')