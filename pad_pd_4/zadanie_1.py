import numpy as np

data1 = np.genfromtxt('./Zadanie_1.csv', delimiter=';', skip_header=1)

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