import pandas as pd
import numpy as np
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import BUJE_LEVA
from utils.requiredColumns import get_required_columns

def case_buje_add(archivo_excel, messagebox):
    columnas = get_required_columns(BUJE_LEVA)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
    datos = []
    
    medidas = ['STD', '03', '05']  # En este excel se pedia agregar esto.
    
    for _, row in df.iterrows():
        if pd.isna(row["Codigo"]) or pd.isna(row["Precio"]):
            datos.append({ 
                'Codigo': '', 
                "Descripcion": row["Descripcion"], 
                'Precio': '', 
                'Medidas': '' 
            })
        else:
            for medida in medidas:
                datos.append({ 
                    'Codigo': row["Codigo"], 
                    "Descripcion": row["Descripcion"], 
                    'Precio': round(row['Precio'], 2), 
                    'Medidas': medida 
                    })

    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'buje_leva_')
        
    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')