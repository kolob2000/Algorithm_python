digit, number = input('Введите последовательность чисел и искомое число через пробел - ').split()

count = 0
for i in digit:
    if number == i:
        count += 1
print(f'Цифра {number} повторятся {count} раз.')
