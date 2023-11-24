import tkinter as tk
from tkinter import ttk
import numpy as np
from sympy import symbols, sympify, diff
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import funciones as fn


def plot_ecuacion(ecuacion, x_vals, puntos=None, ecu_der=None):
    plt.title("Grafica de la ecuacion con puntos Dados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth='1')
    plt.axvline(0, color='black', linewidth='1')
    plt.plot(x_vals, [fn.evaluar_ecuacion(ecuacion, x) for x in x_vals], label='Ecuación')

    canvas.draw()
    ecuacion_label.config(text=f"Ecuación actual: {ecuacion}")


def emular_calculo():
    ecuacion = ecuacion_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    error = float(error_entry.get())
    selec = metodo_combobox.get()

    if selec == "Biseccion":
        iteraciones, resultados = fn.metodo_biseccion(ecuacion, a, b, error)

    if selec == "Secante":
        iteraciones, resultados = fn.metodo_secante(ecuacion, a, b, error)

    if selec == "Falsa Posicion":
        iteraciones, resultados = fn.metodo_falsa_posicion(
            ecuacion, a, b, error)

    if selec == "Newton-Raphson":
        iteraciones, resultados = fn.metodo_new(
            ecuacion, a, b, error)

    iteraciones_text_widget.delete("1.0", tk.END)
    iteraciones_text_widget.insert(tk.END, "\n".join(iteraciones))
    resultados_text_widget.delete("1.0", tk.END)
    resultados_text_widget.insert(tk.END, "\n".join(resultados))

def mostrar_ayuda():
    mensaje_ayuda = "¡Bienvenido a la Calculadora Numérica!\n\n" \
                    "1. Ingrese la ecuación en el cuadro de texto.\n" \
                    "2. Ingrese los valores para a, b y el error.\n" \
                    "3. Seleccione el método numérico.\n" \
                    "4. Haga clic en 'Emular Cálculo' para ver resultados y gráfica.\n\n" \
                    "Botón de Ayuda presionado."
    tk.messagebox.showinfo("Ayuda", mensaje_ayuda)

def mostrar_creditos():
    mensaje_creditos = "Creado por:\n" \
                       "- Samuel Celis Lizcano\n" \
                       "- Juan Pablo Marquez\n" \
                       "- Yoberson Hernandez\n" \
                       "- Juan Camilo Gomez Hernandez"
    tk.messagebox.showinfo("Créditos", mensaje_creditos)

def actualizar_titulo():
    titulo_label.config(text=ecuacion_entry.get())

ventana = tk.Tk()
ventana.title("Calculadora Numérica")
ventana.resizable(False, False)

# Agregar un título centrado
#Agregar un título centrado y desplazado a la derecha
titulo_label = ttk.Label(ventana, text="Ecuacion a digitar", font=("Helvetica", 16, "bold"))
titulo_label.grid(row=0, column=0, columnspan=8, pady=(10, 0), padx=(450, 0)) 

# Configuración de estilos de ttk
style = ttk.Style()
style.configure('TButton', padding=5, font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))

# Configuración de la interfaz
tk.Label(ventana, text="Ecuación:").grid(row=0, column=0, sticky="w")
ecuacion_entry = tk.Entry(ventana)
ecuacion_entry.grid(row=0, column=1, columnspan=3, sticky="w")

tk.Label(ventana, text="Punto izquierdo (a):").grid(
    row=1, column=0, sticky="e")
a_entry = tk.Entry(ventana, width=10)
a_entry.grid(row=1, column=1)

tk.Label(ventana, text="Punto derecho (b):").grid(row=1, column=2, sticky="e")
b_entry = tk.Entry(ventana, width=10)
b_entry.grid(row=1, column=3)

tk.Label(ventana, text="Error estimado:").grid(row=1, column=4, sticky="e")
error_entry = tk.Entry(ventana, width=10)
error_entry.grid(row=1, column=5)

tk.Label(ventana, text="Método numérico:").grid(row=2, column=0, sticky="w")
metodo_var = tk.StringVar()
metodo_var.set("Biseccion")
metodo_combobox = ttk.Combobox(ventana, textvariable=metodo_var, values=[
                               "Biseccion", "Secante", "Falsa Posicion", "Newton-Raphson"], state="readonly")
metodo_combobox.grid(row=2, column=1, columnspan=2, sticky="w")

calcular_button = tk.Button(
    ventana, text="Emular Cálculo", command=lambda: [emular_calculo(), actualizar_titulo()])
calcular_button.grid(row=2, column=3, columnspan=3)

# Configuración de la columna para mostrar la gráfica, iteraciones y resultados
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
widget_canvas = canvas.get_tk_widget()
widget_canvas.grid(row=3, column=6, rowspan=3, sticky="w")

toolbar_frame = tk.Frame(ventana)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()

toolbar_frame.grid(row=6, column=6, columnspan=2, sticky="we")

# Botón de ayuda
emoji = "\u2753"
ayuda_button = tk.Button(ventana, text=f"Ayuda {emoji}", command=mostrar_ayuda, bg="blue", fg="white")
ayuda_button.grid(row=0, column=7, sticky="ne", padx=10, pady=10)

# Botón de créditos con fondo gris oscuro
creditos_button = tk.Button(ventana, text="Créditos", command=mostrar_creditos, bg="#444", fg="white")
creditos_button.grid(row=0, column=6, sticky="ne", padx=10, pady=10)

# Frame para las iteraciones
iteraciones_frame = ttk.LabelFrame(ventana, text="Iteraciones")
iteraciones_frame.grid(row=4, column=0, columnspan=6, padx=10,
                       pady=10, sticky="w")  # Movido debajo de los inputs

# Widget Text para mostrar iteraciones
iteraciones_text_widget = tk.Text(
    iteraciones_frame, wrap="none", height=10, width=60)
iteraciones_text_widget.pack(side="left",expand=True, fill='both')

# Barra de desplazamiento vertical para el cuadro de texto de iteraciones
scrollbar = ttk.Scrollbar(iteraciones_frame, orient="vertical", command=iteraciones_text_widget.yview)
scrollbar.pack(side="right", fill="y")

# Frame para los resultados
resultados_frame = ttk.LabelFrame(ventana, text="Resultados")
resultados_frame.grid(row=5, column=0, columnspan=6, padx=10,
                      pady=10, sticky="w")  # Movido debajo de los inputs

# Widget Text para mostrar resultados
resultados_text_widget = tk.Text(
    resultados_frame, wrap="none", height=10, width=60)
resultados_text_widget.pack(expand=True, fill='both')

ventana.mainloop()
