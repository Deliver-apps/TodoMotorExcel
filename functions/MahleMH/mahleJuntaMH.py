import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_JUNTAS_MH
from utils.requiredColumns import get_required_columns

def case_mahle_juntas(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_JUNTAS_MH)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Código MAHLE"] is not None:
                datos.append({'Código MAHLE': '', "Aplicación": row["Código MAHLE"],'Material': '', 'Precio': '' })
            else:
                medidas = str(row['Código MAHLE']).split('/')
          
                for medida in medidas:
                    # Añadir un diccionario por cada combinación de código y medida
                    datos.append({'Código MAHLE': medida, 'Aplicación': row['Aplicación'],'Material': row['Material'], 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_juntas_mh')
            
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')