import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_SUBCONJUNTOS_PC
from utils.requiredColumns import get_required_columns

def case_mahle_subconjuntos_pc(archivo_excel, messagebox):
    columnas = get_required_columns(MAHLE_SUBCONJUNTOS_PC)
    df = leer_archivo_excel(archivo_excel, columnas, messagebox)
    
    # Lista para almacenar los datos
    datos = []

    for _, row in df.iterrows():
        if (pd.isna(row["Precio"]) or row["Precio"] == 0) and row["CODIGO ANTIGUO"] is not None:
            datos.append({'CODIGO ANTIGUO - Medida': '', "APLICACION": row["CODIGO ANTIGUO"], 'Precio': '' })
        else:
            medidas = str(row['MEDIDAS']).split('-')
            
            #Precio error handling
            if isinstance(row['Precio'], (int, float)):
                precio = round(row['Precio'], 2)
            else:
                precio = row['Precio']
                

            for medida in medidas:
                medida = medida.strip()   
                articulo = f"{row['CODIGO ANTIGUO']} {medida}"
                articulo = articulo.replace("nan", "")

                datos.append({
                    'CODIGO ANTIGUO - Medida': articulo, 
                    'APLICACION': row['APLICACION'], 
                    'Precio': precio 
                })

    # Crear un nuevo DataFrame a partir de la lista de diccionarios
    df_repetido = pd.DataFrame(datos)

    guardar_df_en_excel(df_repetido, 'mahle_subconjuntos_pc')

    print(df_repetido)
    print('Se ha guardado el archivo en el escritorio')