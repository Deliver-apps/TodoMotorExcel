##Va a tener que añadir la Columna 'Precio' en C1 y abajo pegar solo el value de precio
#El excel por default viene en columna C '$' y los values en la D. Mientras que la columna 'Precio' solo abarca la C
#Si se trabaja sin headers seguramente funcione.

import pandas as pd
import numpy as np
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import LEVA_IM
from utils.requiredColumns import get_required_columns

def case_leva_im(archivo_excel, messagebox):
    columnas = get_required_columns(LEVA_IM)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox) 
    datos = []
    
    medidas_mm = ['STD', '0.05 mm', '0.13 mm', '0.25 mm', '0.50 mm', '0.75 mm', '1.00 mm']
    medidas_inch = ['STD', '002"', '005"', '010"', '015"', '020"', '030"']  # En este excel se pedia agregar esto.
    
    for _, row in df.iterrows():
        cod_im = str(row['Cod. IM']) if not pd.isna(row['Cod. IM']) else ''
        if cod_im.endswith('*'):
            medidas = medidas_mm
        elif cod_im.endswith('T'):
            medidas = medidas_inch
        else:
            medidas = ['']

        for medida in medidas:
            datos.append({
                'Cod. IM': cod_im,
                "Descripción": row["Descripción"],
                'Precio': round(row['Precio'], 2),
                'Medidas': medida
            })

    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'buje_leva_IM_')
        
    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')