arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squere = lambda x: x**2
cube = lambda x: x**3

print([squere(x) for x in arr])
print([cube(x) for x in arr])