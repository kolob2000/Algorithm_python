digit = int(input('Введите трехзначное число - '))

sum = digit % 10
multiple = digit % 10
digit = digit // 10
sum += digit % 10
multiple *= digit % 10
digit = digit // 10
sum += digit % 10
multiple *= digit % 10
print(f'Сумма = {sum}')
print(f'Произведение = {multiple}')

