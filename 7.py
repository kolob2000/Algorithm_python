n = int(input('Введите любое натурльное число - '))
left = 0
for i in range(1, n + 1):
    left += i
right = int(n * (n + 1) / 2)

print(f'Для множества натуральных чисел длиной N выполняется равенство 1+2+...+n = n(n+1)/2')
print(f'Для 1+2+...+n = {left}')
print(f'n(n+1)/2 = {right}')
