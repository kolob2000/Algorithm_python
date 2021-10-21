n = int(input('введите длину проекции - '))
summ = 0
temp = 2
for _ in range(n):
    if _ % 2 == 0:
        summ += temp / 2
    else:
        summ += -(temp / 2)
    temp = temp / 2
print(summ)
