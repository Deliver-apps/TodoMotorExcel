import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import FEDERAL_SUBCONJUNTOS
from utils.requiredColumns import get_required_columns
import re

def case_federal_subconjuntos(archivo_excel, messagebox):
      columnas = get_required_columns(FEDERAL_SUBCONJUNTOS)
      df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
      messagebox.showinfo("Tutorial", "Para el correcto funcionamiento de este archivo debes copiar normalmente Y PEGAR A VALOR(CTRL + SHIFT + V) en la hoja nueva de excel. Y escribir MEDIDAS en la casilla C1")
      
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

      guardar_df_en_excel(df_repetido, 'federal_subconjuntos_')

      print(df_repetido)
      print('Se ha guardado el archivo en el escritorio')
