import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import FEDERAL_SUBCONJUNTOS
from utils.requiredColumns import get_required_columns

def case_federal_subconjuntos(archivo_excel, messagebox):
		
    columnas = get_required_columns(FEDERAL_SUBCONJUNTOS)
    # df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Lista para almacenar los datos
    # datos = []
    df = pd.read_excel(archivo_excel)
    # for index, row in df.iterrows():
    #   print(row)
    for col in df.columns:
        print(col)

        # if pd.isna(row["PRECIO LISTA "]) and row["APLICACION"] is not None:
        #     datos.append({'CODIGO': '', "APLICACION": row["APLICACION"], 'PRECIO LISTA ': '' })
        # else:
        #     medidas = str(row['']).split('-')
        
        #     for medida in medidas:
        #         medida = medida.strip()
            
        #         datos.append({'CODIGO': f"{row['CODIGO']}", 'APLICACION': row['APLICACION'],'': medida, 'PRECIO LISTA ': round(row['PRECIO LISTA '], 2)})

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    # df_repetido = pd.DataFrame(datos)

    # guardar_df_en_excel(df_repetido, 'federal_subconjuntos_')

    # print(df_repetido)
    # print('Se ha guardado el archivo en el escritorio')