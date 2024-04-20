#Este tiene las Medidas: dentro de Aplicación.

import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_COJINETES_CL
from utils.requiredColumns import get_required_columns

def case_mahle_cojinetes_cl(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_COJINETES_CL)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({ 'Artículo': row["Artículo"], "Aplicación": '', 'Precio': '' })
            else:
                medidas = str(row['Aplicación']).split(',')
        
                for medida in medidas:
                    medida = medida.strip()
                    datos.append({'Artículo': f"{row['Artículo']}", 'Aplicación': medida, 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_cojinetes_cl')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')