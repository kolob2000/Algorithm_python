import random
# ############# Первый вариант
matrix = []
for _ in range(4):
    tmp = []
    summ = 0
    for i in range(5):
        if i == 4:
            tmp.append(summ)
        else:
            j = random.randint(1, 10)
            tmp.append(j)
            summ += j
    matrix.append(tmp)
print('Первый вариант:')
for i in matrix:
    print(i)
################### Второй вариант
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
for i in matrix:
    summ = 0
    for j in i:
        summ += j
    i.append(summ)

print('\n Второй вариант:')
for i in matrix:
    print(i)

############### Тритий вариант
matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
for i in matrix:
    i.append(sum(i))
print('\n Третий вариант:')
for i in matrix:
    print(i)
