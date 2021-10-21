digits = input('Введите натуральные числа через пробел - ').strip().split()
max = 0
print(digits)

for i in digits:
    summ = 0
    for j in i:
        summ += int(j)
    if summ > max:
        max = summ
        digit = i

print(digit)
