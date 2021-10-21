digit = int(input('Введите число - '))
odd = 0
even = 0
while digit:
    match digit:
        case digit if digit != 0 and digit % 2 == 0:
            even += 1
            digit = digit // 10
        case digit if digit != 0 and digit % 2 != 0:
            odd += 1
            digit = digit // 10

print(f'Четных: {even}, Нечетных: {odd}')
