import numpy as np

data_coffee = np.array([
    245, 310, 180, 260, 290, 3500, 220, 275, 240, 310,
    190, 265, 285, 210, 245, 300, 180, 4000, 290, 150,
    330, 220, 275, 240, 310, 190, 265, 285, 210, 245,
    300, 180, 260, 290, 150, 330, 220, 275, 240, 310,
    190, 265, 285, 210, 176, 300, 180, 260, 290, 150,
    330, 220, 275, 240, 310, 190, 265, 285, 210, 245
])

sr_znach = np.mean(data_coffee)
print("среднее значение: ", sr_znach)

mediana = np.median(data_coffee)
print("медиана: ", mediana)

stand_otklon = np.std(data_coffee)
print("стандартное отклонение: ", stand_otklon)

dispersia = np.var(data_coffee)
print("дисперсия: ", dispersia)

max = np.max(data_coffee)
print("максимальное значение: ", max)

min = np.min(data_coffee)
print("минимальное значение: ", min)

razmah = max - min
print("размах: ", razmah)

p25, p50, p75, p90, p99 = np.percentile(data_coffee, [25, 50, 75, 90, 99])
print("25 перцентиль: ", p25)
print("50 перцентиль: ", p50)
print("75 перцентиль: ", p75)
print("90 перцентиль: ", p90)
print("99 перцентиль: ", p99)

Q1, Q3 = np.percentile(data_coffee, [25, 75])
print("первый квартиль: ", Q1)
print("третий квартиль: ", Q3)

IQR = Q3 - Q1
print("межквартильный размах: ", IQR)

niz_gran = Q1 - 1.5 * IQR
verh_gran = Q3 + 1.5 * IQR

vybros = data_coffee[(data_coffee < niz_gran) | (data_coffee > verh_gran)]
print("выбросы: ", vybros)

total_vyruchka = data_coffee.sum()
print("общая выручка за 60 дней работы кофейни: ", total_vyruchka)