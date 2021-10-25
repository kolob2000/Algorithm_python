import random

digits = [random.randint(1, 100) for i in range(20)]
list_index = []
for index, digit in enumerate(digits, 0):
    if not digit % 2:
        list_index.append(index)

print(f'Indexes: {list_index}')
print(f'Array: {digits}')
