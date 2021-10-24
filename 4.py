import random

array = [random.randint(1, 100) for _ in range(100)]
count = 0
element = 0
for i in array:
    if array.count(i) > count:
        count = array.count(i)
        element = i

print(element)
print(sorted(array))

# Второй вариант
count = 0
element = 0
for i in array:
    tmp = 0
    for j in array:
        if i == j:
            tmp += 1
    if tmp > count:
        element = i
        count = tmp

print(element)
