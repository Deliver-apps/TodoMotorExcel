import pandas as pd
from datetime import datetime
import os
import numpy as np

import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from tkinter import filedialog

#functions
#nubo
from functions.Nubo.nuboGuiaValvula import case_nubo_guia_valvula
from functions.Nubo.nuboAsientoValvula import case_nubo_asiento_valvula
#mahle PC
from functions.MahlePC.mahleSubconjuntosPC import case_mahle_subconjuntos_pc
from functions.MahlePC.mahleArosPC import case_mahle_aros_pc
#mahle MH
from functions.MahleMH.mahleConjuntosMH import case_mahle_conjuntos_mh
from functions.MahleMH.mahleSubconjuntosMH import case_mahle_subconjuntos_mh
from functions.MahleMH.mahleCojinetesMH import case_mahle_cojinetes_mh
from functions.MahleMH.mahleCamisaMH import case_mahle_camisa_mh
from functions.MahleMH.mahleArosMH import case_mahle_aros_mh
from functions.MahleMH.mahleArosRectifMH import case_mahle_aros_rectif_mh
from functions.MahleMH.mahleArosTH import case_mahle_aros_th
from functions.MahleMH.mahleOrings import case_mahle_oring
#mahle CL
from functions.MahleCL.mahleConjuntosCL import case_mahle_conjuntos_cl
from functions.MahleCL.mahleSubconjuntosCL import case_mahle_subconjuntos_cl
from functions.MahleCL.mahleCamisaCL import case_mahle_camisa_cl
from functions.MahleCL.mahleArosCL import case_mahle_aros_cl
from functions.MahleCL.mahleCojinetesCL import case_mahle_cojinetes_cl

#utils
from utils.excelHandler import leer_archivo_excel, guardar_df_en_excel
from constants.empresas import MAHLE_COJINETES_CL, MAHLE_AROS_CL, MAHLE_CAMISA_CL, MAHLE_SUBCONJUNTOS_CL, MAHLE_CONJUNTOS_CL, MAHLE_ORING, MAHLE_AROS_TH, MAHLE_AROS_RECTIF_MH, MAHLE_AROS_MH, MAHLE_CONJUNTOS_MH, MAHLE_CAMISA_MH, MAHLE_COJINETES_MH, MAHLE_SUBCONJUNTOS_MH, MAHLE_AROS_PC, MAHLE_SUBCONJUNTOS_PC, NUBO_GUIA_VALVULA, NUBO_ASIENTO_VALVULA
from utils.requiredColumns import get_required_columns

class SelectorApp:
    def __init__(self, root):
        self.root = root
        root.title('Selector de Archivos y Opciones')

        # Opciones para el Combobox o OptionMenu
        self.opciones = ['-----MAHLE CL-----', MAHLE_COJINETES_CL, MAHLE_AROS_CL, MAHLE_CAMISA_CL, MAHLE_SUBCONJUNTOS_CL,MAHLE_CONJUNTOS_CL,'-----MAHLE MH-----', MAHLE_ORING, MAHLE_AROS_TH, MAHLE_AROS_RECTIF_MH, MAHLE_AROS_MH, MAHLE_CONJUNTOS_MH, MAHLE_CAMISA_MH, MAHLE_COJINETES_MH, MAHLE_SUBCONJUNTOS_MH,'-----MAHLE PC-----', MAHLE_AROS_PC, MAHLE_SUBCONJUNTOS_PC,'-----NUBO-----', NUBO_GUIA_VALVULA, NUBO_ASIENTO_VALVULA]
        
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
        #NUBO
        if self.opcion_seleccionada.get() == NUBO_GUIA_VALVULA:
            case_nubo_guia_valvula(archivo_excel, messagebox)
        elif self.opcion_seleccionada.get() == NUBO_ASIENTO_VALVULA:
            case_nubo_asiento_valvula(archivo_excel, messagebox)
        
        #MAHLE PC
        elif self.opcion_seleccionada.get() == MAHLE_SUBCONJUNTOS_PC:
            case_mahle_subconjuntos_pc(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_AROS_PC:
            case_mahle_aros_pc(archivo_excel, messagebox)
        
        #MAHLE MH
        elif self.opcion_seleccionada.get() == MAHLE_CONJUNTOS_MH:
            case_mahle_conjuntos_mh(archivo_excel, messagebox)      
        elif self.opcion_seleccionada.get() == MAHLE_SUBCONJUNTOS_MH:
            case_mahle_subconjuntos_mh(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_COJINETES_MH:
            case_mahle_cojinetes_mh(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_CAMISA_MH:
            case_mahle_camisa_mh(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_AROS_MH:
            case_mahle_aros_mh(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_AROS_RECTIF_MH:
            case_mahle_aros_rectif_mh(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_AROS_TH:
            case_mahle_aros_th(archivo_excel, messagebox)    
        elif self.opcion_seleccionada.get() == MAHLE_ORING:
            case_mahle_oring(archivo_excel, messagebox)    
        
        #MAHLE CL
        elif self.opcion_seleccionada.get() == MAHLE_CONJUNTOS_CL:
            case_mahle_conjuntos_cl(archivo_excel, messagebox) 
        elif self.opcion_seleccionada.get() == MAHLE_SUBCONJUNTOS_CL:
            case_mahle_subconjuntos_cl(archivo_excel, messagebox) 
        elif self.opcion_seleccionada.get() == MAHLE_CAMISA_CL:
            case_mahle_camisa_cl(archivo_excel, messagebox) 
        elif self.opcion_seleccionada.get() == MAHLE_COJINETES_CL:
            case_mahle_cojinetes_cl(archivo_excel, messagebox) 
        elif self.opcion_seleccionada.get() == MAHLE_AROS_CL:
            case_mahle_aros_cl(archivo_excel, messagebox) 
   
        self.root.destroy()

        if not archivo_excel:
            messagebox.warning("Warning", "Debes seleccionar un archivo Excel")
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

        if opcion.startswith('-----'):
            messagebox.showwarning("Seleccion Invalida", 'Selecciona una opcion que sea valida')
            return

        columnas = get_required_columns(opcion)
        messagebox.showinfo("Info", f"El archivo Excel debe contener las columnas: {columnas}")

# Crear la ventana principal
root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
app = SelectorApp(root)
root.mainloop()