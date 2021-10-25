import random

matrix = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]

array_mins = []

for i in range(len(matrix)):
    min_el = matrix[i][0]
    for j in range(len(matrix[i])):
        if matrix[j][i] < min_el:
            min_el = matrix[j][i]
    array_mins.append(min_el)
max_el = array_mins[0]
for i in array_mins:
    if max_el < i:
        max_el = i
print('Исходная матрица:')
for row in matrix:
    for el in row:
        print(el, end='\t')
    print()

print(f'Список минимальных элементов каждого столбца:\n{array_mins}')
print(f'Максимальный элемент среди минимальных:\n{max_el}')
