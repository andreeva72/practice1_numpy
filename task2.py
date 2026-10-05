import numpy as np

A = np.array([210, 245, 300, 180, 260, 290, 150, 330, 220, 275, 240, 310, 190, 265, 285])

matrix = np.reshape(A, (3,5))
print("матрица: ")
print(matrix)

print("размерность матрицы: ", matrix.shape)
print("общее кол-во эл-тов: ", matrix.size)

sum_stroka = matrix.sum(axis=1)
sum_stolbik = matrix.sum(axis=0)
print("сумма по строкам: ", sum_stroka)
print("сумма по столбцам: ", sum_stolbik)

matrix_transponir = matrix.T
print("транспонированная матрица: ", matrix_transponir)

sr_znach = np.mean(matrix)
stand_otklon = np.std(matrix)
dispersia = np.var(matrix)
print("среднее значение всех эл-тов матрицы: ", sr_znach)
print("стандартное отклонение: ", stand_otklon)
print("дисперсия: ", dispersia)
Q1, Q2, Q3 = np.percentile(A, [25, 50, 75])
print("первый квартиль: ", Q1)
print("второй квартиль: ", Q2)
print("третий квартиль: ", Q3)