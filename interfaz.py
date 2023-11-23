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

    canvas.draw()


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


ventana = tk.Tk()
ventana.title("Calculadora Numérica")
ventana.resizable(False, False)

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
    ventana, text="Emular Cálculo", command=emular_calculo)
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

# Frame para las iteraciones
iteraciones_frame = ttk.LabelFrame(ventana, text="Iteraciones")
iteraciones_frame.grid(row=4, column=0, columnspan=6, padx=10,
                       pady=10, sticky="w")  # Movido debajo de los inputs

# Widget Text para mostrar iteraciones
iteraciones_text_widget = tk.Text(
    iteraciones_frame, wrap="none", height=10, width=60)
iteraciones_text_widget.pack(expand=True, fill='both')

# Frame para los resultados
resultados_frame = ttk.LabelFrame(ventana, text="Resultados")
resultados_frame.grid(row=5, column=0, columnspan=6, padx=10,
                      pady=10, sticky="w")  # Movido debajo de los inputs

# Widget Text para mostrar resultados
resultados_text_widget = tk.Text(
    resultados_frame, wrap="none", height=10, width=60)
resultados_text_widget.pack(expand=True, fill='both')

ventana.mainloop()
