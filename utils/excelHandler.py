# excel_handler.py
import pandas as pd
import os
from datetime import datetime

def leer_archivo_excel(archivo_excel, columnas, messagebox):
    try:
        df = pd.read_excel(archivo_excel, usecols=columnas)
        return df
    except Exception as e:
        messagebox.showwarning("Warning", "Error al leer el archivo Excel. Asegúrate de que el archivo es un archivo Excel válido y cumpla con los formatos establecidos.")
        print(f"Error: {e}")
        return None

def guardar_df_en_excel(df, prefijo_nombre_archivo):
    escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    # Verifica y ajusta la ruta del escritorio si es necesario
    if not os.path.exists(escritorio):
        escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Escritorio')
        if not os.path.exists(escritorio):
            escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Desktop')

    timestamp_actual = datetime.now().strftime("%Y%m%d%H%M%S")
    ruta_archivo = f'{escritorio}/{prefijo_nombre_archivo}_{timestamp_actual}.xlsx'
    df.to_excel(ruta_archivo, index=False)
    return ruta_archivo