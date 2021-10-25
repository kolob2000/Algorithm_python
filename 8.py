import random

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
for i in matrix:
    print(i)
