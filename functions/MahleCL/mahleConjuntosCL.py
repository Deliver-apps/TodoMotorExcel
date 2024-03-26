import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_CONJUNTOS_CL
from utils.requiredColumns import get_required_columns
from utils.mahleRefCL import ref_mahle_cl

def case_mahle_conjuntos_cl(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_CONJUNTOS_CL)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({'Artículo - Ref': '', "Aplicación": row["Artículo"], 'Precio': '' })
            else:
                medidas = ref_mahle_cl(row["Ref."])
                
                for medida in medidas:
                    # Añadir un diccionario por cada combinación de código y medida
                    datos.append({'Artículo - Ref': f"{row['Artículo']} / {row['Ref.']} / {medida}", 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_conjuntos_cl')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')