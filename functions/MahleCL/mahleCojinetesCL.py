#Este tiene las Medidas: dentro de Aplicación. el reeplace no cambia  piez-1027-S: .... 

import pandas as pd
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_COJINETES_CL
from utils.requiredColumns import get_required_columns
import re

def case_mahle_cojinetes_cl(archivo_excel, messagebox):
        columnas = get_required_columns(MAHLE_COJINETES_CL)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({ 'Artículo - Medidas': row["Artículo"], 'Precio': '' })
            else:
                medidas = str(row['Aplicación']).split(',')
        
                for medida in medidas:
                    medida = medida.strip()
                    articulo = f"{row['Artículo']} {medida}"
                    # Saca las palabras no needed, hardcodeado mostly.
                    articulo = articulo.replace("Medidas:", " ").replace("Reemplaza", " ").replace(".", " ").replace("1985--->1987", " ").replace("( el G21879)", " ").replace("- 4 cil", " ").replace("- 6 cil", " ").replace("Después de 01/2000", " ").replace("EO: 5257363", " ").replace("(EO 3802210)", " ").replace("(OE piez: Ford BH6T/6211/AA/; Cummins 5348887)", " ").replace("(OE piez-1027-S: Ford BH3T/6633/AA/; Cummins 4996250)", " ").replace("Perforación central parón", " ").replace('Perforación º 30" parón', " ").replace("4 y 6 cil", " ").replace("(OE piez-1027-S: Ford BH3T/6633/AA/; Cummins 4996250)", " ").replace("(OE piez-1028-S: Ford BH3T/6337/AA/; Cummins 4946031)", " ").replace("(OE piez-1027-I: Ford BH3T/6633/BA/; Cummins 4946030)", " ").replace("(OE piez-1027-S: Ford BH3T/6633/AA/; Cummins 4996250) (OE piez-1028-S: Ford BH3T/6337/AA/; Cummins 4946031)(OE piez-1027-I: Ford BH3T/6633/BA/; Cummins 4946030)", " ").replace(" (OE piez: Ford BH6T/6211/AA/; Cummins 5348887)(OE: piez: Ford BH6T/6211/BA/; Cummins 5340182)", "")
                    #No hardcodeado regex para eliminar el a [codigo random]
                    articulo = re.sub('a [A-Za-z0-9]*', '', articulo)
                    articulo = re.sub('\(OE ', '', articulo)
                    datos.append({
                         'Artículo - Medidas': articulo, 
                         'Precio': round(row['Precio'], 2)
                         })        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_cojinetes_cl')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')



