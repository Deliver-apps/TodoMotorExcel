import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_AROS_RECTIF_MH
from utils.requiredColumns import get_required_columns
from utils.mahleRefAros import ref_mahle_aros

def case_mahle_aros_rectif_mh(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_AROS_RECTIF_MH)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({'Artículo - Ref - Medida': '', "Aplicación": row["Artículo"], 'Precio': '' })
            else:
                medidas = ref_mahle_aros(row["Ref."])
                
                for medida in medidas:
                    datos.append({'Artículo - Ref - Medida': f"{row['Artículo']} {row['Ref.']} {medida}", 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_aros_rectif_mh')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')