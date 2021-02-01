# -*- coding: utf-8 -*-

from tkinter import END, messagebox
from tkinter.filedialog import askopenfilename

import fitz

def buscarArchivo(entrada_de_texto, tipo_de_archivo):
    entrada_de_texto.delete(0, 'end')
    nombre_archivo =askopenfilename(
        filetypes=((
            "{} files".format(tipo_de_archivo),
            "*.{}".format(tipo_de_archivo)),
            ("All files","*.*")
        ))
    entrada_de_texto.insert(END, nombre_archivo)

def firmarDocumentos(pdf, firma):
    try:
        rectangulo_firma = fitz.Rect(450,20,550, 120)
        pdf_abierto = fitz.open(pdf)
        primera_pagina = pdf_abierto[0]
        primera_pagina.insertImage(rectangulo_firma, filename=firma)
        file_handle.save(pdf.replace(".pdf", "_firmado.pdf"))
        messagebox.showinfo("Completado", "Se ha firmado correctamente el fichero.")
    except:
         messagebox.showerror("Error", "No se ha podido firmar el fichero, compruebe la ruta.")
