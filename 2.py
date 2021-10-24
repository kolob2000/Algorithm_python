import random

numbers = [random.randint(1, 100) for i in range(20)]
list_index = []
for i, j in enumerate(numbers, 0):
    if not j % 2:
        list_index.append(i)

print(f'Indexes: {list_index}')
print(f'Array: {numbers}')
