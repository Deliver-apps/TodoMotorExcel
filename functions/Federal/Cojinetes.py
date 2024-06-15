import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import FEDERAL_COJINETES
from utils.requiredColumns import get_required_columns

def case_federal_cojinetes(archivo_excel, messagebox):
      columnas = get_required_columns(FEDERAL_COJINETES)
      df = leer_archivo_excel(archivo_excel, columnas, messagebox)

      messagebox.showinfo("Tutorial", "Para el correcto funcionamiento de este archivo debes copiar normalmente Y PEGAR A VALOR(CTRL + SHIFT + V) en la hoja nueva de excel. Y escribir MODELO en la casilla E1")
      
      # Lista para almacenar los datos
      datos = []

      for _, row in df.iterrows():
        if pd.isna(row["PRECIO LISTA"]) and row["APLICACIÓN"] is not None:
            datos.append({
                'CODIGO - MEDIDA - MODELO': '', 
                "APLICACIÓN": row["APLICACIÓN"], 
                'PRECIO LISTA': '' })
        else:
            medidas = str(row['MEDIDAS']).split('-')
        
            for medida in medidas:
                medida = medida.strip()
            
                datos.append({
                    'CODIGO - MEDIDA - MODELO': f"{row['CODIGO']} {medida} {row['MODELO']}", 
                    'APLICACIÓN': row['APLICACIÓN'],
                    'PRECIO LISTA': round(row['PRECIO LISTA'], 2)})
                
      # Crear un nuevo DataFrame a partir de la lista de diccionarios
      df_repetido = pd.DataFrame(datos)

      guardar_df_en_excel(df_repetido, 'federal_cojinetes_')

      print(df_repetido)
      print('Se ha guardado el archivo en el escritorio')
