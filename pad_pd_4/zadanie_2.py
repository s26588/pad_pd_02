import numpy as np

data2 = np.genfromtxt('./Zadanie_2.csv', delimiter=';')

## a)
w,v = np.linalg.eig(data2)
print("Wartości własne")
print(w)
print("Wektory własne")
print(v)

## b)
print("Odwrotność macierzy")
print(np.linalg.inv(data2))