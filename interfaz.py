import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar(ecuacion, x_vals, y_vals):
    plt.clf()
    plt.plot(x_vals, y_vals, label=ecuacion)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    canvas.draw()

def metodo_biseccion(ecuacion, a, b, error):
    iteraciones = []
    resultados = []

    fa = eval(ecuacion.replace('x', str(a)))
    fb = eval(ecuacion.replace('x', str(b)))

    if fa * fb > 0:
        resultados.append("No hay cambio de signo en el intervalo.")
        return iteraciones, resultados

    iteracion = 0
    while (b - a) / 2 > error:
        c = (a + b) / 2
        fc = eval(ecuacion.replace('x', str(c)))

        iteraciones.append(f"Iteración {iteracion}: [{a}, {b}], c = {c:.5f}, f(c) = {fc:.5f}")

        if abs(fc) < error:
            resultados.append(f"Error: {error:.5f}\nNúmero de iteraciones: {iteracion}\nRaíz encontrada: {c:.5f}")
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iteracion += 1

    # Añadir la última iteración y resultados si la condición de error se cumple
    iteraciones.append(f"Iteración {iteracion}: [{a}, {b}], c = {c:.5f}, f(c) = {fc:.5f}")
    resultados.append(f"Error: {error:.5f}\nNúmero de iteraciones: {iteracion}\nRaíz encontrada: {c:.5f}")

    return iteraciones, resultados

def emular_calculo():
    ecuacion = ecuacion_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    error = float(error_entry.get())
    metodo_combobox.set("Bisección")

    iteraciones, resultados = metodo_biseccion(ecuacion, a, b, error)

    iteraciones_text_widget.delete("1.0", tk.END)
    iteraciones_text_widget.insert(tk.END, "\n".join(iteraciones))
    resultados_text_widget.delete("1.0", tk.END)
    resultados_text_widget.insert(tk.END, "\n".join(resultados))
    
    emular_iteraciones()
    emular_resultados()

def emular_iteraciones():
    iteraciones_frame.update_idletasks()

def emular_resultados():
    resultados_frame.update_idletasks()

ventana = tk.Tk()
ventana.title("Calculadora Numérica")

# Configuración de la interfaz
tk.Label(ventana, text="Ecuación:").grid(row=0, column=0, sticky="e")
ecuacion_entry = tk.Entry(ventana)
ecuacion_entry.grid(row=0, column=1, columnspan=3)

tk.Label(ventana, text="Punto izquierdo (a):").grid(row=1, column=0, sticky="e")
a_entry = tk.Entry(ventana, width=10)
a_entry.grid(row=1, column=1)

tk.Label(ventana, text="Punto derecho (b):").grid(row=1, column=2, sticky="e")
b_entry = tk.Entry(ventana, width=10)
b_entry.grid(row=1, column=3)

tk.Label(ventana, text="Error estimado:").grid(row=1, column=4, sticky="e")
error_entry = tk.Entry(ventana, width=10)
error_entry.grid(row=1, column=5)

tk.Label(ventana, text="Método numérico:").grid(row=2, column=0, sticky="e")
metodo_var = tk.StringVar()
metodo_combobox = ttk.Combobox(ventana, textvariable=metodo_var, values=["Bisección", "Secante", "Falsa Posición", "Newton-Raphson"])
metodo_combobox.grid(row=2, column=1, columnspan=2)

calcular_button = tk.Button(ventana, text="Emular Cálculo", command=emular_calculo)
calcular_button.grid(row=2, column=3, columnspan=3)

# Configuración de la columna para mostrar la gráfica, iteraciones y resultados
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
widget_canvas = canvas.get_tk_widget()
widget_canvas.grid(row=3, column=6, rowspan=3, sticky="e")

# Frame para las iteraciones
iteraciones_frame = ttk.LabelFrame(ventana, text="Iteraciones")
iteraciones_frame.grid(row=4, column=0, columnspan=6, padx=10, pady=10, sticky="w")  # Movido debajo de los inputs

# Widget Text para mostrar iteraciones
iteraciones_text_widget = tk.Text(iteraciones_frame, wrap="none", height=10, width=50)
iteraciones_text_widget.pack(expand=True, fill='both')

# Frame para los resultados
resultados_frame = ttk.LabelFrame(ventana, text="Resultados")
resultados_frame.grid(row=5, column=0, columnspan=6, padx=10, pady=10, sticky="w")  # Movido debajo de los inputs

# Widget Text para mostrar resultados
resultados_text_widget = tk.Text(resultados_frame, wrap="none", height=10, width=50)
resultados_text_widget.pack(expand=True, fill='both')

ventana.mainloop()
