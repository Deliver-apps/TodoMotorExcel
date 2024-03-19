import pandas as pd
from datetime import datetime
import os
import numpy as np

import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter import filedialog


class SelectorApp:
    def __init__(self, root):
        self.root = root
        root.title('Selector de Archivos y Opciones')

        # Opciones para el Combobox o OptionMenu
        self.opciones = ['Nubo Guia Válvula', 'Nubo Asiento Válvula', 'Mahle Conjuntos', 'Mahle Cojinetes PC']
        
        # Variable para almacenar la opción seleccionada
        self.opcion_seleccionada = tk.StringVar()

        # Etiqueta para mostrar la ruta del archivo seleccionado
        self.archivo_seleccionado = tk.StringVar(value='Selecciona una opción para definir los parametros del excel')
        self.etiqueta_archivo = tk.Label(root, textvariable=self.archivo_seleccionado)
        self.etiqueta_archivo.pack(pady=5)
        
        # Combobox para las opciones
        self.combobox = ttk.Combobox(root, textvariable=self.opcion_seleccionada, values=self.opciones, state='readonly')
        self.combobox.pack(pady=10)
        self.combobox.bind('<<ComboboxSelected>>', self.show_required_columns)

        # Botón para seleccionar archivo
        self.boton_archivo = tk.Button(root, text='Seleccionar Archivo', command=self.seleccionar_archivo)
        self.boton_archivo.pack(pady=5)
        
        # Botones Aceptar y Cancelar
        self.boton_aceptar = tk.Button(root, text='Aceptar', command=self.aceptar)
        self.boton_aceptar.pack(side=tk.RIGHT, padx=(20, 10), pady=20)
        
        self.boton_cancelar = tk.Button(root, text='Cancelar', command=self.cancelar)
        self.boton_cancelar.pack(side=tk.LEFT, padx=(10, 20), pady=20)

        # Footer
        self.footer = tk.Label(root, text="Powered by Dinasoft")
        self.footer.pack(side=tk.BOTTOM, pady=10)

    def seleccionar_archivo(self):
        # Abre el diálogo para seleccionar un archivo y actualiza la etiqueta con la ruta del archivo
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:  # Si el usuario selecciona un archivo
            self.archivo_seleccionado.set(ruta_archivo)
        else:
            self.archivo_seleccionado.set('Selecciona un archivo Excel')

    def aceptar(self):
        archivo_excel = self.archivo_seleccionado.get()
        
        if self.opcion_seleccionada.get() == 'Nubo Guia Válvula':
            self.caseNuboGuiaValvula(archivo_excel)
        elif self.opcion_seleccionada.get() == 'Nubo Asiento Válvula':
            self.caseNuboAsientoValvula(archivo_excel)
        elif self.opcion_seleccionada.get() == 'Mahle Conjuntos':
            self.caseMahleConjuntos(archivo_excel)    
        elif self.opcion_seleccionada.get() == 'Mahle Cojinetes PC':
            self.caseMahleCojinetes(archivo_excel)    

        self.root.destroy()

        if not archivo_excel:
            messagebox.showwarning("Warning", "Debes seleccionar un archivo Excel")
            return

        # Check if the selected file is an Excel file. !!!AVERIGUAR OTROS FORMATOS DE EXCEL!!!
        if not (archivo_excel.endswith('.xlsx') or archivo_excel.endswith('.xls')):
            messagebox.showwarning("Warning", "El formato del archivo no es correcto. Por favor, selecciona un archivo Excel.")
            return
        
        messagebox.showinfo("Info", "El archivo Excel ha sido añadido a tu escritorio.")
        

    def cancelar(self):
        # Acciones al presionar Cancelar
        print('Operación Cancelada')
        self.root.destroy()

    def leer_archivo_excel(self, archivo_excel, columnas):
        try:
            df = pd.read_excel(archivo_excel, usecols=columnas)
            return df
        except Exception as e:
            messagebox.showwarning("Warning", "Error al leer el archivo Excel. Asegúrate de que el archivo es un archivo Excel válido y cumpla con los formatos establecidos.")
            print(f"Error: {e}")
            return None
    
    def show_required_columns(self, event):
        opcion = self.opcion_seleccionada.get()
        columnas = self.get_required_columns(opcion)
        messagebox.showinfo("Info", f"El archivo Excel debe contener las columnas: {columnas}")

    def get_required_columns(self, opcion):
        # INSERTAR COLUMNAS POR CADA DEF
        opciones = {
            'Nubo Guia Válvula': ['Código', 'Marca', 'Precio'],
            'Nubo Asiento Válvula': ['Código', 'Marca', 'Precio'],
            'Mahle Conjuntos': ['Artículo', 'Ref.', 'Precio', "Aplicación"],
            'Mahle Cojinetes PC': ['Marca', 'Código Corto', 'Aplicación', 'Precio']
            # añadir...
        }
        return opciones.get(opcion, [])
    
    def caseNuboGuiaValvula(self, archivo_excel):
        columnas = self.get_required_columns('Nubo Guia Válvula')
        df = self.leer_archivo_excel(archivo_excel, columnas)
        
        # Los valores de 'medida' que quieres añadir al 'Código'
        medidas = ['STD' ,'003', '005', '010', '015']

        # Lista para almacenar los datos
        datos = []

        for _, row in df.iterrows():
            for medida in medidas:
                # Añadir un diccionario por cada combinación de código y medida
                datos.append({'Código': f"{row['Código']} {medida}", 'Marca': row['Marca'], 'Precio': round(row['Precio'], 2)})

        # Crear un nuevo DataFrame a partir de la lista de diccionarios
        df_repetido = pd.DataFrame(datos)

        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Comprueba si la ruta existe
        if not os.path.exists(escritorio):
        # Si no existe, usa la ruta del escritorio predeterminada
            escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Escritorio')
            if not os.path.exists(escritorio):
                escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Desktop')
        
        timestamp_actual = datetime.now().strftime("%Y%m%d%H%M%S")
        df_repetido.to_excel(f'{escritorio}/nubo_guia_valvula_{timestamp_actual}.xlsx', index=False)

        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')
        
    def caseNuboAsientoValvula(self, archivo_excel):   
        columnas = self.get_required_columns('Nubo Asiento Válvula')
        df = self.leer_archivo_excel(archivo_excel, columnas)

        # Los valores de 'medida' que quieres añadir al 'Código'
        medidas = ['STD' , '005', '010', '020']

        # Lista para almacenar los datos
        datos = []

        for _, row in df.iterrows():
            for medida in medidas:
                # Añadir un diccionario por cada combinación de código y medida
                datos.append({'Código': f"{row['Código']} {medida}", 'Marca': row['Marca'], 'Precio': round(row['Precio'], 2)})

        # Crear un nuevo DataFrame a partir de la lista de diccionarios
        df_repetido = pd.DataFrame(datos)

        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        # Comprueba si la ruta existe
        if not os.path.exists(escritorio):
        # Si no existe, usa la ruta del escritorio predeterminada
            escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Escritorio')
            if not os.path.exists(escritorio):
                escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Desktop')
        timestamp_actual = datetime.now().strftime("%Y%m%d%H%M%S")
        df_repetido.to_excel(f'{escritorio}/nubo_asiento_valvula_{timestamp_actual}.xlsx', index=False)

        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')

    def caseMahleConjuntos(self, archivo_excel):
        columnas = self.get_required_columns('Mahle Conjuntos')
        df = self.leer_archivo_excel(archivo_excel, columnas)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({'Artículo - Ref': '', "Aplicación": row["Artículo"], 'Precio': '' })
            else:
                medidas = self.refMahleConjuntos(row["Ref."])
                
                for medida in medidas:
                    # Añadir un diccionario por cada combinación de código y medida
                    datos.append({'Artículo - Ref': f"{row['Artículo']} / {row['Ref.']} / {medida}", 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        # Comprueba si la ruta existe
        if not os.path.exists(escritorio):
        # Si no existe, usa la ruta del escritorio predeterminada
            escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Escritorio')
            if not os.path.exists(escritorio):
                escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Desktop')
        timestamp_actual = datetime.now().strftime("%Y%m%d%H%M%S")
        df_repetido.to_excel(f'{escritorio}/mahle_conjuntos_{timestamp_actual}.xlsx', index=False)
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')
        
    def caseMahleCojinetes(self, archivo_excel): 
        columnas = self.get_required_columns('Mahle Cojinetes PC')
        df = self.leer_archivo_excel(archivo_excel, columnas)

        medidas = ['STD', '0,25', '0,50', '0,75', 'SPA', '(F-STD)']
        autos = []
        datos= []

        for _, row in df.iterrows():
            for medida in medidas:
                datos.append({'Código Corto': f"{row['Código Corto']} {medida}", 'Marca': row['Marca'], 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})

        df_repetido = pd.DataFrame(datos)

        escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

        # Comprueba si la ruta existe
        if not os.path.exists(escritorio):
        # Si no existe, usa la ruta del escritorio predeterminada
            escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Escritorio')
            if not os.path.exists(escritorio):
                escritorio = os.path.join(os.environ['USERPROFILE'], 'OneDrive/Desktop')
        
        timestamp_actual = datetime.now().strftime("%Y%m%d%H%M%S")
        df_repetido.to_excel(f'{escritorio}/mahle_cojinetes_{timestamp_actual}.xlsx', index=False)

        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')

    def refMahleConjuntos(self, ref):
        switch = {
            'E.O.': ['N° de equipo original.'],
            'AC': ['Altura de Compresión reducida'],
            'WS': ['con aros de vedación (with seal)'],
            'A': ['STD.'],
            'A/1': ['STD - Entrega condicionada.'],
            'B': ['STD', '0.50.'],
            'C': ['STD', 0.50, '1.00.'],
            'D': ['STD', 0.25, 0.50, 0.75, '1.00.'],
            'E': ['STD', '04', '06.'],
            'F': ['STD', 0.25, 0.50, '1.00.'],
            'F/1': ['1.25', '1.50', '2.00.'],
            'G': ['0.50.'],
            'H': ['STD',0.25,0.50,'1.00.'],
            'I': ['Ø ext. camisa: 93,7 mm.', '94,5 mm.', '95,5 mm.', '96,2 mm.'],
            'J': ['STD', '06.'],
            'K': ['0.50', '1.00.'],
            'L': ['STD', 0.50, 0.75, '1.00.'],
            'M': ['STD', '04.'],
            'N': ['STD', '010', '020'],
            'O': ['STD', 0.50, 0.75],
            'P': ['STD = 98,76 mm.', '+030' , '-030' ,'-060.'],
            'Q': ['STD', '025.'],
            'R': ['STD' , 0.25, '0.50.'],
            'S': ['STD' , 0,40 , '0,80.'],
            'T': ['STD', 0.30, '0.60'],
            'U': ['STD', '0.65'],
            1: ['Camisas con pestaña.'],
            2: ['Se proveen sin bujes de bielas y sin  anillos de camisas.'],
            3: ['Se proveen con bujes de bielas y anillos de camisas.'],
            4: ['Se proveen sin bujes de bielas y con anillos de camisas.'],
            'A.C.': ['Altura de compresión.']
        }
        
        return switch.get(ref, 'N/A')   

# Crear la ventana principal
root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
app = SelectorApp(root)
root.mainloop()
