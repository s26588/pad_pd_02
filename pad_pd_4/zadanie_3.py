import numpy as np

matrix_a = np.genfromtxt('./Zadanie_3_macierz_A.csv', delimiter=',')
matrix_b = np.genfromtxt('./Zadanie_3_macierz_B.csv', delimiter=',')

matrix = np.zeros([matrix_a.shape[0], matrix_b.shape[0]])

numerator = lambda a,b: np.multiply(a, b).sum()
denominator = lambda a,b: np.sqrt(np.multiply(a, a).sum() * np.multiply(b, b).sum())

for i in range(matrix.shape[0]):
  for j in range(matrix.shape[1]):
      a = matrix_a[i]
      b = matrix_b[j]
      matrix[i,j] = numerator(a,b) / denominator(a,b)

print(matrix)