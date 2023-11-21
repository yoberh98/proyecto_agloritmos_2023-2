from sympy import symbols, sympify, diff
import numpy as np


def metodo_biseccion(ecuacion_str, a, b, error):
    iteraciones = []
    resultados = []

    x = symbols('x')
    ecuacion = sympify(ecuacion_str)

    fa = ecuacion.subs(x, a)
    fb = ecuacion.subs(x, b)

    if fa * fb > 0:
        resultados.append("No hay cambio de signo en el intervalo.")
        return iteraciones, resultados

    iteracion = 0
    while (b - a) / 2 > error:
        iteracion += 1
        c = (a + b) / 2
        # fc = eval(ecuacion.replace('x', str(c)))
        fc = ecuacion.subs(x, c)

        iteraciones.append(
            f"Iteración {iteracion}: [{a}, {b}], c = {c:.5f}, f(c) = {fc:.5f}")

        if fc == 0:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    # Añadir la última iteración y resultados si la condición de error se cumple

    resultados.append(
        f"Error: {error:.5f}\nNúmero de iteraciones: {iteracion}\nRaíz encontrada: {c:.5f}")

    return iteraciones, resultados


def f_x2(x1, x0, fx1, fx0):
    x2 = x1 - (fx1*(x1-x0))/(fx1-fx0)
    return x2


def f_errores(x1, x2, fx2):
    e1 = abs(x2-x1)/abs(x2)
    e2 = abs(fx2)
    return e1, e2


def metodo_secante(ecuacion, a, b, error):
    iteraciones = []
    resultados = []

    x = symbols('x')
    ecuacion = sympify(ecuacion)

    miEr = 1
    contador = 1
    ite = 2

    while miEr == 1:
        fx0 = ecuacion.subs(x, a)
        fx1 = ecuacion.subs(x, b)
        x2 = f_x2(b, a, fx1, fx0)
        fx2 = ecuacion.subs(x, x2)

        iteraciones.append(
            f"Iteración {ite}: [{a}, {b}], xi = {x2:.5f}, f(xi) = {fx2:.5f}")

        if contador > 1:
            [e1, e2] = f_errores(b, x2, fx2)
            if (e1 <= error or e2 <= error):
                miEr = 2
                break
        else:
            contador += 1

        a = b
        b = x2
        ite += 1

    resultados.append(
        f"Error: {error:.5f}\nNúmero de iteraciones: {ite}\nRaíz encontrada: {x2:.5f}")

    # resultados.append("Seleccionaste secante")

    return iteraciones, resultados


def f_xi(a, b, fa, fb):
    xi = (a*fb-b*fa)/(fb-fa)
    return xi


def metodo_falsa_posicion(ecuacion, a, b, error):
    iteraciones = []
    resultados = []

    x = symbols('x')
    ecuacion = sympify(ecuacion)

    miErr = 1
    itera = 0
    xiAnt = 0

    while miErr > error:
        fa = ecuacion.subs(x, a)
        fb = ecuacion.subs(x, b)

        xi = f_xi(a, b, fa, fb)
        fxi = ecuacion.subs(x, xi)

        if (fa*fxi) < 0:
            b = xi
        else:
            a = xi

        if itera > 0:
            miErr = xi - xiAnt

        xiAnt = xi
        itera += 1

        iteraciones.append(
            f"Iteración {itera}: [{a}, {b}], xi = {xi:.5f}, f(xi) = {fxi:.5f}")

    resultados.append(
        f"Error: {error:.5f}\nNúmero de iteraciones: {itera}\nRaíz encontrada: {xi:.5f}")

    # resultados.append("Seleccionaste Falsa Posicion")

    return iteraciones, resultados


def f_xin(x1, fx1, fdx1):
    xi = x1 - (fx1/fdx1)
    return xi


def f_err(x2, x1):
    e = abs((x2-x1)/x2)
    return e


def metodo_new(ecuacion, a, b, error):
    iteraciones = []
    resultados = []

    x = symbols('x')
    ecuacion = sympify(ecuacion)
    ecu_deri = diff(ecuacion)

    x1 = a
    er = 1
    i = 0

    while er > error:
        fx1 = ecuacion.subs(x, x1)
        fdx1 = ecu_deri.subs(x, x1)
        x2 = f_xin(x1, fx1, fdx1)
        er = f_err(x2, x1)
        x1 = x2
        i += 1
        iteraciones.append(
            f"Iteración {i}: [{a}, {b}], x2 = {x2:.5f}")

    resultados.append(
        f"Error: {error:.5f}\nNúmero de iteraciones: {i}\nRaíz encontrada: {x2:.5f}")

    # resultados.append("Seleccionaste Newton_Rapson")

    return iteraciones, resultados
