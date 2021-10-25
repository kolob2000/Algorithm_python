import random

array = [random.randint(1, 50) for _ in range(20)]
most_min = array[0]
next_min = array[1]
count = 0
# не знаю, может избыточно, но постарался реализовать на голом питоне
for i in array:
    if i == most_min:
        count += 1
    if i < most_min:
        most_min = i
        count = 1
    if array[0] > array[1]:
        next_min = array[0]  # на всякий случай если минимальным будет array[1] единственным элементом

if count > 1:
    next_min = most_min
else:
    for i in array:
        if most_min < i < next_min:
            next_min = i

print(sorted(array), most_min, next_min)

