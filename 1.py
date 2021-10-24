quantity = 0
list_numbers = []

for i in range(2, 100):
    count = 0
    for j in range(2, 9):
        if i % j == 0:
            count += 1
        else:
            break
    if count == 8:
        quantity += 1
        list_numbers.append(i)
if quantity != 0:
    print(f'{quantity} чисел кратны числам от 2 до 9.', f'\n Это числа: {list_numbers}')
else:
    print('Таких чисел нет.')