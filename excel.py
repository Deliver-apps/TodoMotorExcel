import pandas as pd
from datetime import datetime
import os
import numpy as np

import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter import filedialog
from functions.mahleGuiaValvula import case_nubo_guia_valvula
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import NUBO_GUIA_VALVULA, NUBO_ASIENTO_VALVULA, MAHLE_CONJUNTOS, MAHLE_COJINETES_PC
from utils.mahleRef import ref_mahle_conjuntos
from utils.requiredColumns import get_required_columns

class SelectorApp:
    def __init__(self, root):
        self.root = root
        root.title('Selector de Archivos y Opciones')

        # Opciones para el Combobox o OptionMenu
        self.opciones = [NUBO_GUIA_VALVULA, NUBO_ASIENTO_VALVULA, MAHLE_CONJUNTOS, MAHLE_COJINETES_PC]
        
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
        
        if self.opcion_seleccionada.get() == NUBO_GUIA_VALVULA:
            case_nubo_guia_valvula(archivo_excel, messagebox)
        elif self.opcion_seleccionada.get() == NUBO_ASIENTO_VALVULA:
            self.case_nubo_asiento_valvula(archivo_excel)
        elif self.opcion_seleccionada.get() == MAHLE_CONJUNTOS:
            self.case_mahle_conjuntos(archivo_excel)    
        elif self.opcion_seleccionada.get() == MAHLE_COJINETES_PC:
            self.case_mahle_cojinetes(archivo_excel)    

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
    
    def show_required_columns(self, event):
        opcion = self.opcion_seleccionada.get()
        columnas = get_required_columns(opcion)
        messagebox.showinfo("Info", f"El archivo Excel debe contener las columnas: {columnas}")

        
    def case_nubo_asiento_valvula(self, archivo_excel):   
        columnas = self.get_required_columns(NUBO_ASIENTO_VALVULA)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)

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

        guardar_df_en_excel(df_repetido, 'nubo_asiento_valvula')

        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')

    def case_mahle_conjuntos(self, archivo_excel):
        columnas = self.get_required_columns(MAHLE_CONJUNTOS)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)      
        datos = []
        
        for _, row in df.iterrows():
            if pd.isna(row["Precio"]) and row["Artículo"] is not None:
                datos.append({'Artículo - Ref': '', "Aplicación": row["Artículo"], 'Precio': '' })
            else:
                medidas = ref_mahle_conjuntos(row["Ref."])
                
                for medida in medidas:
                    # Añadir un diccionario por cada combinación de código y medida
                    datos.append({'Artículo - Ref': f"{row['Artículo']} / {row['Ref.']} / {medida}", 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})        
        
        df_repetido = pd.DataFrame(datos)

        guardar_df_en_excel(df_repetido, 'mahle_conjuntos')
        
        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')
        
    def case_mahle_cojinetes(self, archivo_excel): 
        columnas = self.get_required_columns(MAHLE_COJINETES_PC)
        df = leer_archivo_excel(archivo_excel, columnas, messagebox)

        medidas = ['STD', '0,25', '0,50', '0,75', 'SPA', '(F-STD)']
        datos= []

        for _, row in df.iterrows():
            for medida in medidas:
                datos.append({'Código Corto': f"{row['Código Corto']} {medida}", 'Marca': row['Marca'], 'Aplicación': row['Aplicación'], 'Precio': round(row['Precio'], 2)})

        df_repetido = pd.DataFrame(datos)
        
        guardar_df_en_excel(df_repetido, 'mahle_cojinetes')

        print(df_repetido)
        print('Se ha guardado el archivo en el escritorio')

    
# Crear la ventana principal
root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
app = SelectorApp(root)
root.mainloop()
