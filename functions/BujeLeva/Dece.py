import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import DECE
from utils.requiredColumns import get_required_columns

def case_dece(archivo_excel, messagebox):
        columnas = get_required_columns(DECE)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precios Netos"]) and row["CODIGO DECE"] is not None:
                datos.append({'CODIGO DECE': row['CODIGO DECE'], "MOTOR ; Diametro Perno ": '','MEDIDAS': '', 'Precios Netos': '' })
            else:
                medidas = str(row['MEDIDAS']).split('/')
          
                for medida in medidas:
                    datos.append({'CODIGO DECE': row['CODIGO DECE'], 'MOTOR ; Diametro Perno ': row['MOTOR ; Diametro Perno '], 'MEDIDAS': medida, 'Precios Netos': round(row['Precios Netos'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, '_dece_')
            
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')