"""Лабораторна робота №3
Студента Сірого І.М.
Номер віраінта: 122"""


import random
import numpy as np
import math


X1_MIN = -5
X2_MIN = 10
X3_MIN = 10
X1_MAX = 15
X2_MAX = 60
X3_MAX = 20
F1 = 2
F2 = 4
F3 = 8
F4 = 2
N = 4
M = 3
T_TABLE_VALUE = 2.306
F_TABLE_VALUE = 4.5


def x_maximum_average():
    x_max_average = (X1_MAX + X2_MAX + X3_MAX) / 3
    return x_max_average


def x_minimum_average():
    x_min_average = (X1_MIN + X2_MIN + X3_MIN) / 3
    return x_min_average


def y_maximum():
    y_max = 200 + x_maximum_average()
    return y_max


def y_minimum():
    y_min = 200 + x_minimum_average()
    return y_min


def print_x_encoded_matrix():
    print("Кодованє значення X")
    print("{:<5} {:<5} {:<5} {:<5}".format("№", "X1", "X2", "X3"))
    x11 = ["-1", "-1", "+1", "+1"]
    x22 = ["-1", "+1", "-1", "+1"]
    x33 = ["-1", "+1", "+1", "-1"]
    for i in range(4):
        print("{:<5} {:<5} {:<5} {:<5}".format(i + 1, x11[i], x22[i], x33[i]))


print_x_encoded_matrix()


def print_experimental_design_matrix():
    print("\nМатриця для m = 3")
    print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format("№", "X1", "X2", "X3", "Y1", "Y2", "Y3"))
    x1 = [X1_MIN, X1_MIN, X1_MAX, X1_MAX]
    x2 = [X2_MIN, X2_MAX, X2_MIN, X2_MAX]
    x3 = [X3_MIN, X3_MAX, X3_MAX, X3_MIN]

    y1 = [random.randrange(int(y_minimum()), int(y_maximum()), 1) for _ in range(4)]
    y2 = [random.randrange(int(y_minimum()), int(y_maximum()), 1) for _ in range(4)]
    y3 = [random.randrange(int(y_minimum()), int(y_maximum()), 1) for _ in range(4)]
    for element in range(4):
        print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(element + 1, x1[element], x2[element], x3[element],
                                                                 y1[element], y2[element], y3[element]))
    line1_y_average = (y1[0] + y2[0] + y3[0]) / 3
    line2_y_average = (y1[1] + y2[1] + y3[1]) / 3
    line3_y_average = (y1[2] + y2[2] + y3[2]) / 3
    line4_y_average = (y1[3] + y2[3] + y3[3]) / 3
    line_y_arr = [line1_y_average, line2_y_average, line3_y_average, line4_y_average]

    def average_line_values_of_response_function():    # Знайдемо середні значення відгуку функції за рядками

        mx1 = sum(x1) / 4
        mx2 = sum(x2) / 4
        mx3 = sum(x3) / 4

        my = (line1_y_average + line2_y_average + line3_y_average + line4_y_average) / 4
        
        # Коефіцієнти a1,a2,a3,a11,a22,a33,a12,a13,a23 є проміжними позначеннями при знаходженні коефіцієнтів рівняння регресії
        # та вводяться для того аби спростити вигляд системи рівнянь

        a1 = (x1[0] * line1_y_average + x1[1] * line2_y_average + x1[2] * line3_y_average + x1[3] * line4_y_average) / 4        
        a2 = (x2[0] * line1_y_average + x2[1] * line2_y_average + x2[2] * line3_y_average + x2[3] * line4_y_average) / 4
        a3 = (x3[0] * line1_y_average + x3[1] * line2_y_average + x3[2] * line3_y_average + x3[3] * line4_y_average) / 4

        a11 = (x1[0] * x1[0] + x1[1] * x1[1] + x1[2] * x1[2] + x1[3] * x1[3]) / 4           
        a22 = (x2[0] * x2[0] + x2[1] * x2[1] + x2[2] * x2[2] + x2[3] * x2[3]) / 4
        a33 = (x3[0] * x3[0] + x3[1] * x3[1] + x3[2] * x3[2] + x3[3] * x3[3]) / 4
        a12 = _a21 = (x1[0] * x2[0] + x1[1] * x2[1] + x1[2] * x2[2] + x1[3] * x2[3]) / 4
        a13 = _a31 = (x1[0] * x3[0] + x1[1] * x3[1] + x1[2] * x3[2] + x1[3] * x3[3]) / 4
        a23 = _a32 = (x2[0] * x3[0] + x2[1] * x3[1] + x2[2] * x3[2] + x2[3] * x3[3]) / 4

        b01 = np.array([[my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a23], [a3, a13, a23, a33]])
        b02 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
        b0 = np.linalg.det(b01) / np.linalg.det(b02)

        b11 = np.array([[1, my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a23], [mx3, a3, a23, a33]])
        b12 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
        b1 = np.linalg.det(b11) / np.linalg.det(b12)

        b21 = np.array([[1, mx1, my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a23], [mx3, a13, a3, a33]])
        b22 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
        b2 = np.linalg.det(b21) / np.linalg.det(b22)

        b31 = np.array([[1, mx1, mx2, my], [mx1, a11, a12, a1], [mx2, a12, a22, a2], [mx3, a13, a23, a3]])
        b32 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])
        b3 = np.linalg.det(b31) / np.linalg.det(b32)

        print("\nОтримане рівняння регресії:\ny = {:.2f} + {:.2f}*x1 + {:.2f}*x2 + {:.2f}*x3".format(b0, b1, b2, b3))

        print("y1 = " + str(round(b0 + b1 * x1[0] + b2 * x2[0] + b3 * x3[0], 2)) +
              " = " + str(round(line1_y_average, 2)))
        print("y2 = " + str(round(b0 + b1 * x1[1] + b2 * x2[1] + b3 * x3[1], 2)) +
              " = " + str(round(line2_y_average, 2)))
        print("y3 = " + str(round(b0 + b1 * x1[2] + b2 * x2[2] + b3 * x3[2], 2)) +
              " = " + str(round(line3_y_average, 2)))
        print("y4 = " + str(round(b0 + b1 * x1[3] + b2 * x2[3] + b3 * x3[3], 2)) +
              " = " + str(round(line4_y_average, 2)))
        print("Значення співпадають")
        return [b0, b1, b2, b3]
    b = average_line_values_of_response_function()
    return y1, y2, y3, line_y_arr, x1, x2, x3, b


values = print_experimental_design_matrix()


def dispersion():
    print("\nДисперсія по рядкам")
    dispersion1 = ((values[0][0] - values[3][0]) ** 2 + (values[1][0] - values[3][1]) ** 2 +
                   (values[2][0] - values[3][2]) ** 2) / 3
    dispersion2 = ((values[0][1] - values[3][0]) ** 2 + (values[1][1] - values[3][1]) ** 2 +
                   (values[2][1] - values[3][2]) ** 2) / 3
    dispersion3 = ((values[0][2] - values[3][0]) ** 2 + (values[1][2] - values[3][1]) ** 2 +
                   (values[2][2] - values[3][2]) ** 2) / 3
    dispersion4 = ((values[0][3] - values[3][0]) ** 2 + (values[1][3] - values[3][1]) ** 2 +
                   (values[2][3] - values[3][2]) ** 2) / 3
    print("d1 =", round(dispersion1, 2), "\nd2 =", round(dispersion2, 2), "\nd3 =", round(dispersion3, 2),
          "\nd4 =", round(dispersion4, 2))
    dispersions = [dispersion1, dispersion2, dispersion3, dispersion4]
    return dispersions


dispersion = dispersion()


def g_distribution():
    print("\nКритерій Кохрена")
    gp = max(dispersion) / sum(dispersion)
    print("Gp = " + str(gp))
    if gp <= 0.7679:
        print("Дисперсія однорідна")
    else:
        print("Дисперсія неоднорідна")


g_distribution()


def t_distribution():
    print("\nКритерій Ст'юдента")
    dispersion_square_b = sum(dispersion) / 4
    dispersion_square_beta = dispersion_square_b / N * M
    dispersion_beta = math.sqrt(dispersion_square_beta)
    beta0 = (values[3][0] * 1 + values[3][1] * 1 + values[3][2] * 1 + values[3][3] * 1) / 4
    beta1 = (values[3][0] * (-1) + values[3][1] * (-1) + values[3][2] * 1 + values[3][3] * 1) / 4
    beta2 = (values[3][0] * (-1) + values[3][1] * 1 + values[3][2] * (-1) + values[3][3] * 1) / 4
    beta3 = (values[3][0] * (-1) + values[3][1] * 1 + values[3][2] * 1 + values[3][3] * (-1)) / 4
    beta_arr = [beta0, beta1, beta2, beta3]
    print('| '.join('Beta{} = {:.2f} '.format(n + 1, k) for n, k in enumerate(beta_arr)))

    t0 = beta0 / dispersion_beta
    t1 = beta1 / dispersion_beta
    t2 = beta2 / dispersion_beta
    t3 = beta3 / dispersion_beta

    if t0 < T_TABLE_VALUE:
        print("t0 < t-табличне, коефіцієнт b0 незначимий")
        values[7][0] = 0
    if t1 < T_TABLE_VALUE:
        print("t1 < t-табличне, коефіцієнт b1 незначимий")
        values[7][1] = 0
    if t2 < T_TABLE_VALUE:
        print("t2 < t-табличне, коефіцієнт b2 незначимий")
        values[7][2] = 0
    if t3 < T_TABLE_VALUE:
        print("t3 < t-табличне, коефіцієнт b3 незначимий")
        values[7][3] = 0
    y1 = values[7][0] + values[7][1] * X1_MIN + values[7][2] * X2_MIN + values[7][3] * X3_MIN
    y2 = values[7][0] + values[7][1] * X1_MIN + values[7][2] * X2_MAX + values[7][3] * X3_MAX
    y3 = values[7][0] + values[7][1] * X1_MAX + values[7][2] * X2_MIN + values[7][3] * X3_MAX
    y4 = values[7][0] + values[7][1] * X1_MAX + values[7][2] * X2_MAX + values[7][3] * X3_MIN
    print("\ny1 = {:.2f}\ny2 = {:.2f}\ny3 = {:.2f}\ny4 = {:.2f}".format(y1, y2, y3, y4))
    return [y1, y2, y3, y4, dispersion_square_beta]


equations = t_distribution()


def f_distribution():
    print("\nКритерій Фішера")
    d = 2
    print(d, " значимих коефіцієнта")
    s_square_ad = ((equations[0] - values[0][0]) ** 2 + (equations[1] - values[1][1]) ** 2 +
                   (equations[2] - values[2][2]) ** 2 + (equations[3] - values[3][3]) ** 2) * (M / F4)
    fp = s_square_ad / equations[4]
    print("Fp = ", round(fp, 2))

    if fp > F_TABLE_VALUE:
        print("Fp =", round(fp, 2), "> Ft", F_TABLE_VALUE, "Рівняння неадекватно оригіналу")
    else:
        print("Fp =", round(fp, 2), "< Ft", F_TABLE_VALUE, "Рівняння адекватно оригіналу")


f_distribution()
