import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import FEDERAL_PISTONES
from utils.requiredColumns import get_required_columns
import re

def case_federal_pistones(archivo_excel, messagebox):
      columnas = get_required_columns(FEDERAL_PISTONES)
      df = leer_archivo_excel(archivo_excel, columnas, messagebox)

      messagebox.showinfo("Tutorial", "Para el correcto funcionamiento de este archivo debes copiar solo los valores de la tabla y PEGAR A VALOR (CTRL + SHIFT + V) en la hoja nueva de excel en A2. Recuerda de escribir los nombres de las columnas segun su debido valor. Deberia quedar asi A1 = APLICACIÓN, C1 = MEDIDAS, E1 = CÓDIGO, G1 = PRECIO LISTA. Con sus respectiva data abajo de cada columna ")     
      # Lista para almacenar los datos
      datos = []

      for _, row in df.iterrows():
        if pd.isna(row["PRECIO LISTA"]) and row["APLICACIÓN"] is not None:
            datos.append({
                'CÓDIGO - MEDIDA': '', 
                "APLICACIÓN": row["APLICACIÓN"], 
                'PRECIO LISTA': '' })
        else:
            medidas = re.split('-|/', str(row['MEDIDAS']))
        
            for medida in medidas:
                medida = medida.strip()
            
                datos.append({
                    'CÓDIGO - MEDIDA': f"{row['CÓDIGO']} {medida}", 
                    'APLICACIÓN': row['APLICACIÓN'],
                    'PRECIO LISTA': round(row['PRECIO LISTA'], 2)})
                
      # Crear un nuevo DataFrame a partir de la lista de diccionarios
      df_repetido = pd.DataFrame(datos)

      guardar_df_en_excel(df_repetido, 'federal_pistones_')

      print(df_repetido)
      print('Se ha guardado el archivo en el escritorio')
