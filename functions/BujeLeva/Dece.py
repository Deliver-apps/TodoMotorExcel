import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import DECE
from utils.requiredColumns import get_required_columns

def case_dece(archivo_excel, messagebox):
        columnas = get_required_columns(DECE)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            precios_netos_column = next((col for col in row.index if col.strip() == "Precios Netos"), None)
            codigo_dece_column = next((col for col in row.index if col.strip() == "CODIGO DECE"), None)
            motor_diametro_perno_column = next((col for col in row.index if col.strip() == "MOTOR ; Diametro Perno "), None)
            
            if pd.isna(precios_netos_column) and codigo_dece_column is not None:
                datos.append({'CODIGO DECE': codigo_dece_column, "MOTOR ; Diametro Perno ": '','MEDIDAS': '', 'Precios Netos': '' })
            else:
                medidas = str(row['MEDIDAS']).split('/')

                for medida in medidas:
                    datos.append({'CODIGO DECE': codigo_dece_column, 'MOTOR ; Diametro Perno ': motor_diametro_perno_column, 'MEDIDAS': medida, 'Precios Netos': round(precios_netos_column, 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, '_dece_')
            
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')