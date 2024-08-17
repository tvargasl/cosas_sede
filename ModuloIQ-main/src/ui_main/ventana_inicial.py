import sys
sys.path.append('c:/Users/Tomas/OneDrive/Documentos/Requisitos 2024-1/ModuloIQ-main')


import tkinter as tk
from src.ui_main.Inicio_sesion import Inicio_sesion

ventana = tk.Tk()
ventana.title("MedPlus - Sistema de gestion hospitalaria")
ventana.geometry("1280x720")

Inicio_sesion.inicio_sesion(ventana)

ventana.mainloop()