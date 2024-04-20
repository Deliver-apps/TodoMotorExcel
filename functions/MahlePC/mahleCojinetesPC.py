import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_COJINETES_PC
from utils.requiredColumns import get_required_columns

def case_mahle_cojinetes_pc(archivo_excel, messagebox):
      columnas = get_required_columns(MAHLE_COJINETES_PC)
      df = leer_archivo_excel(archivo_excel, columnas, messagebox)
      
      # Lista para almacenar los datos
      datos = []

      for _, row in df.iterrows():
            medidas = str(row['Código Corto']).split(' ')
            for medida in medidas:
                medida = medida.strip()   
                datos.append({'Marca': row['Marca'], 'Código Corto': medida,'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})
      # Crear un nuevo DataFrame a partir de la lista de diccionarios
      df_repetido = pd.DataFrame(datos)

      guardar_df_en_excel(df_repetido, 'mahle_cojinetes_pc')

      print(df_repetido)
      print('Se ha guardado el archivo en el escritorio')
