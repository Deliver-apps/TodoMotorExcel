#Lee Aros: Hidráulico y Recambio. y Aros: Recambio Linea "A" al mismo tiempo 👌. No lee espesores ni cilindradas (no es necesario (?))
# Devuelve esto ERROR:
##Artículo - Ref	Aplicación	Precio
		
# Aros: Hidráulico Linea "X" / nan / N		0
# Aros: Hidráulico Linea "X" / nan / /		0
# Aros: Hidráulico Linea "X" / nan / A		0
# Chevrolet / nan / N		0
# Chevrolet / nan / /		0
# Chevrolet / nan / A		0


import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_AROS_MH
from utils.requiredColumns import get_required_columns
from utils.mahleRefAros import ref_mahle_aros

def case_mahle_aros_mh(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_AROS_MH)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({'Artículo - Ref': '', "Aplicación": row["Artículo"], 'Precio': '' })
            else:
                ref = str(row["Ref."]) #Lo hace una cadena de string (test)
                medidas = ref_mahle_aros(row["Ref."])
                
                for medida in medidas:
                    datos.append({'Artículo - Ref': f"{row['Artículo']} / {ref} / {medida}", 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_aros_mh')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')