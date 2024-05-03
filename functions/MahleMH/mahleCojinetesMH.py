#Este tiene las Medidas: dentro de Aplicación.

import pandas as pd
import re
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_COJINETES_MH
from utils.requiredColumns import get_required_columns


def case_mahle_cojinetes_mh(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_COJINETES_MH)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Aplicación"] is not None:
                datos.append({ 'Artículo': row["Artículo"], 'Precio': '' })
            else:
                medidas = str(row['Aplicación']).split(',')
        
                for medida in medidas:
                    medida = medida.strip()
                    articulo = f"{row['Artículo']} {medida}"
                    # Saca las palabras no needed, hardcoded
                    articulo = articulo.replace("Medidas:", "").replace("Reemplaza", "").replace(".", "").replace("Motor mecánico (T y TCA)", "").replace("Motor electrónico (T", "").replace("TCA y TCE)", "").replace("Origen Alemania", "").replace("Cojinete axial en + 0", "").replace("(SPUTTER)", "")
                    articulo = re.sub('a [A-Za-z0-9]*', '', articulo)
                    datos.append({
                         'Artículo': articulo, 
                         'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_cojinetes_mh')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')