year = int(input(' Введите, пожалуйста, год - '))

if not year % 400:
    print('Ваш год високосный!')
elif not year % 4 and year % 100:
    print('Ваш год високосный!')
else:
    print('Ваш год невисокосный!')
