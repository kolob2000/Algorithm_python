year = int(input(' Введите, пожалуйста, год - '))

if not year % 400:
    print('Ваш год высокосный!')
elif not year % 4 and year % 100:
    print('Ваш год високосный ')
else:
    print('Ваш год не високосный ')
