digits = input('Введите натуральные числа через пробел - ').split()
max = 0
summ = 0
print(digits)

for i in digits:
    for j in i:
        summ += int(j)
    print(summ)
    if summ > max:
        max = summ
        digit = i

print(digit)
