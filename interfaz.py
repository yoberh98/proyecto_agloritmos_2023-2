import tkinter as tk
from tkinter import ttk
import numpy as np
from sympy import symbols, sympify, diff
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import funciones as fn
import pandas as pd


def emular_calculo():
    graficar()
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
        iteraciones, resultados = fn.metodo_newtom_raphson(
            ecuacion, a, b, error)

    historial.append({
        'ecuacion': ecuacion,
        'puntos': [(a), (b)],
        'error': error,
        'metodo': selec,
        'resultados': resultados
    })

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


def plot_ecuacion(ecuacion, x_vals, puntos=None, der_ecuacion=None, rango_x=(-10, 10), paso=0.1):
    y_vals = [ecuacion.subs('x', val) for val in x_vals]

    plt.cla()
    plt.plot(x_vals, y_vals)

    if puntos:
        x_puntos, y_puntos = zip(*puntos)
        plt.scatter(x_puntos, y_puntos, color='red')

    if der_ecuacion:
        y_vals = [der_ecuacion.subs('x', val) for val in x_vals]
        plt.plot(x_vals, y_vals)

    plt.title("Gráfica de la Ecuación con Puntos Dados")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axhline(0, color='black', linewidth='1')
    plt.axvline(0, color='black', linewidth='1')

    canvas.draw()


def graficar():
    ecuacion_str = ecuacion_entry.get()
    x = symbols("x")
    ecuacion = sympify(ecuacion_str)
    selec = metodo_combobox.get()

    punto1 = float(a_entry.get())
    punto2 = float(b_entry.get())
    rango1 = punto1 - 5
    rango2 = punto2 + 5

    puntos = [(punto1, 0), (punto2, 0)]

    rango_x = np.arange(rango1, rango2, 0.1)

    if selec == "Newton-Raphson":
        der_ecuacion = diff(ecuacion, x)
        plot_ecuacion(ecuacion, rango_x, puntos, der_ecuacion)
    else:
        plot_ecuacion(ecuacion, rango_x, puntos)


def borrar_historial():
    historial.clear()
    with open('historial.txt', 'w') as file:
        pass  # Simplemente abrir y cerrar el archivo para borrar su contenido
    historial_text_widget.delete("1.0", tk.END)
    historial_window.withdraw()


def mostrar_historial_emergente():
    historial_window.deiconify()
    for entry in historial:
        historial_text_widget.insert(
            tk.END, f"Ecuación: {entry['ecuacion']}\n")
        historial_text_widget.insert(tk.END, f"Puntos: {entry['puntos']}\n")
        historial_text_widget.insert(tk.END, f"Error: {entry['error']}\n")
        historial_text_widget.insert(tk.END, f"Método: {entry['metodo']}\n")
        historial_text_widget.insert(
            tk.END, "\n".join(entry['resultados']) + "\n\n")


def llenar_tabla():
    for row_id in tabla.get_children():
        tabla.delete(row_id)
    res_bi = []
    ite_bi = []
    res_se = []
    ite_se = []
    res_fal_pos = []
    ite_fal_pos = []
    res_Net_Rap = []
    ite_Net_Rap = []
    ecuacion = ecuacion_entry.get()
    a = float(a_entry.get())
    b = float(b_entry.get())
    error = float(error_entry.get())
    ite_bi, res_bi = fn.metodo_biseccion(
        ecuacion, a, b, error)

    ite_se, res_se = fn.metodo_secante(
        ecuacion, a, b, error)

    ite_fal_pos, res_fal_pos = fn.metodo_falsa_posicion(
        ecuacion, a, b, error)

    ite_Net_Rap, res_Net_Rap = fn.metodo_newtom_raphson(
        ecuacion, a, b, error)

    res_bi_str = ", ".join(map(str, res_bi))
    res_se_str = ", ".join(map(str, res_se))
    res_fal_pos_str = ", ".join(map(str, res_fal_pos))
    res_Net_Rap_str = ", ".join(map(str, res_Net_Rap))

    tabla.insert("", "end", values=[
        ecuacion, res_bi_str, res_se_str, res_fal_pos_str, res_Net_Rap_str])


def cerrar_tabla():
    tabla.delete()
    ventana_comparacion.withdraw()


def crear_tabla():
    # Definicion de las columnas
    tabla["columns"] = ("Ecuacion", "Biseccion", "Secante",
                        "Falsa Posicion", "Newthon Rapson")

    # Configuracion de las columnas de la tabla
    tabla.column("#0", width=0, stretch=tk.NO)
    tabla.column("Ecuacion", anchor=tk.CENTER, width=200)   
    tabla.column("Biseccion", anchor=tk.CENTER, width=200)
    tabla.column("Falsa Posicion", anchor=tk.CENTER, width=200)
    tabla.column("Newthon Rapson", anchor=tk.CENTER, width=200)

    # Encabezados de las columnas
    tabla.heading("Ecuacion", text="Ecuacion", anchor=tk.CENTER)
    tabla.heading("Biseccion", text="Biseccion", anchor=tk.CENTER)
    tabla.heading("Secante", text="Secante", anchor=tk.CENTER)
    tabla.heading("Falsa Posicion", text="Falsa Posicion", anchor=tk.CENTER)
    tabla.heading("Newthon Rapson", text="Newthon Rapson", anchor=tk.CENTER)

    # Mostrar la Tabla
    tabla.pack()


def mostrar_comparacion():
    ventana_comparacion.deiconify()
    # Creacion de la tabla
    crear_tabla()
    # Insercion de Datos y obtener la informacion digitada para ser procesada en los metodos
    llenar_tabla()


def cargar_historial():
    try:
        with open('historial.txt', 'r') as file:
            # Leer el contenido del archivo y cargar el historial
            historial.clear()  # Limpiar el historial actual
            entry = {}
            for line in file:
                if line.startswith("Ecuación:"):
                    entry['ecuacion'] = line.split(":")[1].strip()
                elif line.startswith("Puntos:"):
                    entry['puntos'] = eval(line.split(":")[1].strip())
                elif line.startswith("Error:"):
                    entry['error'] = float(line.split(":")[1].strip())
                elif line.startswith("Método:"):
                    entry['metodo'] = line.split(":")[1].strip()
                elif line == "\n":
                    # Fin de la entrada, agregar al historial
                    if 'iteraciones' in entry and 'resultados' in entry:
                        historial.append(entry)
                    entry = {}
                else:
                    # Iteraciones o resultados
                    if 'iteraciones' not in entry:
                        entry['iteraciones'] = []
                    if 'resultados' not in entry:
                        entry['resultados'] = []
                    entry['iteraciones' if line.startswith(
                        'Iteración') else 'resultados'].append(line.strip())
    except FileNotFoundError:
        # El archivo no existe, no hay historial para cargar
        pass


def guardar_historial():
    with open('historial.txt', 'w') as file:
        for entry in historial:
            file.write(f"Ecuación: {entry['ecuacion']}\n")
            file.write(f"Puntos: {entry['puntos']}\n")
            file.write(f"Error: {entry['error']}\n")
            file.write(f"Método: {entry['metodo']}\n")
            file.write("\n".join(entry['resultados']) + "\n\n")


def cerrar_aplicacion():
    guardar_historial()
    ventana.destroy()


def cerrar_historial():
    historial_text_widget.delete("1.0", tk.END)
    historial_window.withdraw()


ventana = tk.Tk()
ventana.title("Calculadora Numérica")
ventana.resizable(False, False)
historial = []

# print(tk.TkVersion)

fuente_personalizada = ("Arial", 12)

# Definicion de los elementos del Historial
historial_window = tk.Toplevel(ventana)
historial_window.title("Historial de Cálculos")
historial_window.withdraw()
historial_window.protocol("WM_DELETE_WINDOW", cerrar_historial)
borrar_button = tk.Button(
    historial_window, text="Borrar Historial", command=borrar_historial)
borrar_button.pack(side="top", anchor="nw", pady=10, padx=10)

historial_text_widget = tk.Text(
    historial_window, wrap="none", height=20, width=80)
scrollbar = tk.Scrollbar(historial_window, command=historial_text_widget.yview)
historial_text_widget.configure(yscrollcommand=scrollbar.set)

# Creacion de la ventana de comparacion de metodos

ventana_comparacion = tk.Toplevel(ventana)
ventana_comparacion.title("Comparacion entre metodos")
ventana_comparacion.resizable(False, False)
# Obtener las dimensiones de la pantalla
# ancho_pantalla = ventana_comparacion.winfo_screenwidth()
# alto_pantalla = ventana_comparacion.winfo_screenheight()
# # Calcular las coordenadas para centrar la ventana
# x = (ancho_pantalla - 1200) // 2  # Ancho deseado de la ventana
# y = (alto_pantalla - 250) // 2   # Alto deseado de la ventana

# ventana_comparacion.geometry("1200x250+{}+{}".format(x, y))
ventana_comparacion.withdraw()
ventana_comparacion.protocol("WM_DELETE_WINDOW", cerrar_tabla)

# Creacion de la tabla
tabla = ttk.Treeview(ventana_comparacion)

# Empacar el widget Text y la barra de desplazamiento vertical
historial_text_widget.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
cargar_historial()

# Configuración de la interfaz
tk.Label(ventana, text="Ecuación:", font=fuente_personalizada).grid(
    row=0, column=0, sticky="w")
ecuacion_entry = tk.Entry(ventana)
ecuacion_entry.grid(row=0, column=1, columnspan=3, sticky="w")

tk.Label(ventana, text="Punto izquierdo (a):",
         font=fuente_personalizada).grid(row=1, column=0, sticky="e")
a_entry = tk.Entry(ventana, width=10)
a_entry.grid(row=1, column=1)

tk.Label(ventana, text="Punto derecho (b):",
         font=fuente_personalizada).grid(row=1, column=2, sticky="e")
b_entry = tk.Entry(ventana, width=10)
b_entry.grid(row=1, column=3)

tk.Label(ventana, text="Error estimado:", font=fuente_personalizada).grid(
    row=1, column=4, sticky="e")
error_entry = tk.Entry(ventana, width=10)
error_entry.grid(row=1, column=5)

tk.Label(ventana, text="Método numérico:", font=fuente_personalizada).grid(
    row=2, column=0, sticky="w")
metodo_var = tk.StringVar()
metodo_var.set("Biseccion")
metodo_combobox = ttk.Combobox(
    ventana,
    textvariable=metodo_var,
    values=["Biseccion", "Secante", "Falsa Posicion", "Newton-Raphson"],
    state="readonly", font=fuente_personalizada
)
metodo_combobox.grid(row=2, column=1, columnspan=2, sticky="w")

calcular_button = tk.Button(
    ventana, text="Emular Cálculo", command=emular_calculo)
calcular_button.grid(row=2, column=3, columnspan=3)

# Configuración de la columna para mostrar la gráfica, iteraciones y resultados
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
widget_canvas = canvas.get_tk_widget()
widget_canvas.grid(row=3, column=6, rowspan=3, sticky="w")

# Crear una barra de herramientas de navegación de matplotlib
toolbar_frame = tk.Frame(ventana)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()

# Posicionar la barra de herramientas en la interfaz
toolbar_frame.grid(row=6, column=6, columnspan=2, sticky="we")

# Frame para las iteraciones
iteraciones_frame = ttk.LabelFrame(ventana, text="Iteraciones")
iteraciones_frame.grid(
    row=4, column=0, columnspan=6, padx=10, pady=10, sticky="w"
)  # Movido debajo de los inputs

# Widget Text para mostrar iteraciones
iteraciones_text_widget = tk.Text(
    iteraciones_frame, wrap="none", height=10, width=70)
iteraciones_text_widget.pack(expand=True, fill="both")

# Frame para los resultados
resultados_frame = ttk.LabelFrame(ventana, text="Resultados")
resultados_frame.grid(
    row=5, column=0, columnspan=6, padx=10, pady=10, sticky="w"
)  # Movido debajo de los inputs

# Widget Text para mostrar resultados
resultados_text_widget = tk.Text(
    resultados_frame, wrap="none", height=10, width=70)
resultados_text_widget.pack(expand=True, fill="both")

historial_button = tk.Button(
    ventana, text="Mostrar Historial", command=mostrar_historial_emergente)
historial_button.grid(row=6, column=0, columnspan=2)

comparacion_button = tk.Button(
    ventana, text="Comparar Metodos", command=mostrar_comparacion)
comparacion_button.grid(row=6, column=3, columnspan=2)

ventana.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)

ventana.mainloop()
