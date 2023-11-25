import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


def ayuda():
    ventana_ayuda = tk.Tk()
    ventana_ayuda.title("Ayuda al Usuario")
    ventana_ayuda.resizable(False, False)

    # Obtener las dimensiones de la pantalla
    ancho_pantalla = ventana_ayuda.winfo_screenwidth()
    alto_pantalla = ventana_ayuda.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla - 600) // 2  # Ancho deseado de la ventana
    y = (alto_pantalla - 400) // 2   # Alto deseado de la ventana

    ventana_ayuda.geometry("600x400+{}+{}".format(x, y))

    fuente_personalizada = ("Times New Roman", 14)


    mensaje_ayuda = "¡Bienvenido a la Calculadora Numérica!\n\n" \
                "1. Ingrese la ecuación en el cuadro de texto.\n" \
                "2. Ingrese los valores para a, b y el error.\n" \
                "3. Seleccione el método numérico.\n" \
                "4. Haga clic en 'Emular Cálculo' para ver resultados y gráfica.\n\n" \
                "RECORDAR \n\n" \
                "A. La funcion SENO se debe poner como 'sin(x)' \n" \
                "B. La funcion EULER se debe poner como 'exp(x)' \n" \
                "C. La funcion RAIZ se debe poner como 'sqrt(x)' \n\n" \
                "Creado por:\n" \
                "- Samuel Celis Lizcano\n" \
                "- Juan Pablo Marquez\n" \
                "- Yoberson Hernandez\n" \
                "- Juan Camilo Gomez Hernandez"

    # Crear un widget de etiqueta para mostrar el mensaje de ayuda
    etiqueta_ayuda = tk.Label(ventana_ayuda, text=mensaje_ayuda, justify=tk.LEFT, font=fuente_personalizada)
    etiqueta_ayuda.pack()
    ventana_ayuda.mainloop()



