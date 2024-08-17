import sys
sys.path.append('c:/Users/Tomas/OneDrive/Documentos/Requisitos 2024-1/ModuloIQ-main')

import tkinter as tk
from tkinter import ttk
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo

from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.ui_main.gestion_maestros.Ver_Lista_Maestros import Ver_Lista_Maestros
from src.ui_main.gestion_maestros.Ver_Maestro import Ver_Maestro
from src.ui_main.gestion_maestros.Editar_Maestro import Editar_Maestro

from src.ui_main.gestion_sedes.Editar_Sede import Editar_Sede
from src.ui_main.gestion_sedes.Ver_Lista_Sedes import Ver_Lista_Sedes
from src.ui_main.gestion_sedes.Ver_Sede import Ver_Sede

class Menu_inicial:
    @classmethod
    def menu_inicial_Administrativo(cls, cuenta, frame):
        imprimir_titulo(frame, "Menu Inicial Administrativo")
        frame_inicial = ttk.Frame()
        frame_inicial.pack(fill=tk.BOTH, expand=1)
        label_info = ttk.Label(frame_inicial, text="Bienvenido por favor selecciona en el menú superior la acción que deseas realizar")
        label_info.pack()

        #Menu desplegable
        menu_admin = tk.Menu(frame)
        frame.config(menu=menu_admin)
    
        opcion_gestion_cuentas = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Cuentas", menu=opcion_gestion_cuentas)
        opcion_gestion_cuentas.add_command(label="Crear cuenta")
        opcion_gestion_cuentas.add_command(label="Ver cuenta")
        opcion_gestion_cuentas.add_command(label="Editar cuenta")

        opcion_gestion_maestros = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Maestros", menu=opcion_gestion_maestros)
        opcion_gestion_maestros.add_command(label="Crear Maestro", command=lambda: Crear_Maestro.crear_maestro(cuenta, frame))
        opcion_gestion_maestros.add_command(label="Ver Maestro", command=lambda: Ver_Maestro.ver_maestro(cuenta, frame))
        opcion_gestion_maestros.add_command(label="Ver Lista Maestros", command=lambda: Ver_Lista_Maestros.ver_lista_maestros(cuenta, frame))
        opcion_gestion_maestros.add_command(label="Editar Maestro", command=lambda: Editar_Maestro.editar_maestro(cuenta,frame))

        opcion_gestion_sedes = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Sedes", menu=opcion_gestion_sedes)
        opcion_gestion_sedes.add_command(label="Editar Sede", command=lambda: Editar_Sede.editar_sede(cuenta, frame))
        opcion_gestion_sedes.add_command(label="Ver Sede", command=lambda: Ver_Sede.ver_sede(cuenta, frame))
        opcion_gestion_sedes.add_command(label="Ver Lista De Sedes", command=lambda: Ver_Lista_Sedes.ver_lista_sedes(cuenta, frame))


    @classmethod
    def menu_inicial_Clinico(cls, cuenta, frame):
        imprimir_titulo(frame, "Menu Inicial Clinico")
        frame_inicial = ttk.Frame()
        frame_inicial.pack(fill=tk.BOTH, expand=1)
        label_info = ttk.Label(frame_inicial, text="Bienvenido por favor selecciona en el menú superior la acción que deseas realizar")
        label_info.pack()

        #Menu desplegable
        menu_admin = tk.Menu(frame)
        frame.config(menu=menu_admin)
        opcion_gestion_cuentas = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Cuentas", menu=opcion_gestion_cuentas)
        opcion_gestion_cuentas.add_command(label="Ver cuenta")
        opcion_gestion_maestros = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Maestros", menu=opcion_gestion_maestros)
        opcion_gestion_maestros.add_command(label="Ver Maestro")
        opcion_gestion_sedes = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Sedes", menu=opcion_gestion_sedes)
        opcion_gestion_sedes.add_command(label="Ver Sede", command=lambda: Ver_Sede.ver_sede(cuenta, frame))

