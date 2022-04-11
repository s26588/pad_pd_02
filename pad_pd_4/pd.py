import numpy as np

### Zadanie 1
data1 = np.genfromtxt('Zadanie domowe/Zadanie_1.csv', delimiter=';', skip_header=1)

## a)
print(f"Liczba komórek {data1.size}")

## b)
print(f"Liczba wierszy {data1.shape[0]}")
print(f"Liczba kolumn {data1.shape[1]}")

## c)
print(f"Średnia {np.mean(data1)}")
print(f"Mediana {np.median(data1)}")
print(f"Wariancja {np.var(data1)}")

## d)
print(f"Średnia bez braków {np.nanmean(data1)}")
print(f"Mediana bez braków {np.nanmedian(data1)}")
print(f"Wariancja bez braków {np.nanvar(data1)}")

print()

### Zadanie 2
data2 = np.genfromtxt('Zadanie domowe/Zadanie_2.csv', delimiter=';')

## a)
w,v = np.linalg.eig(data2)
print("Wartości własne")
print(w)
print("Wektory własne")
print(v)

## b)
print("Odwrotność macierzy")
print(np.linalg.inv(data2))


### Zadanie 3
matrix_a = np.genfromtxt('Zadanie domowe/Zadanie_3_macierz_A.csv', delimiter=',')
matrix_b = np.genfromtxt('Zadanie domowe/Zadanie_3_macierz_B.csv', delimiter=',')

# print([matrix_a.shape[0], matrix_b.shape[0]])
matrix = np.zeros([matrix_a.shape[0], matrix_b.shape[0]])

numerator = lambda a,b: np.multiply(a, b).sum()
denominator = lambda a,b: np.sqrt(np.multiply(a, a).sum() * np.multiply(b, b).sum())

for i in range(matrix.shape[0]):
  for j in range(matrix.shape[1]):
      a = matrix_a[i]
      b = matrix_b[j]
      matrix[i,j] = numerator(a,b) / denominator(a,b)

print(matrix)