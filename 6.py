import random as r

digit = int(r.random() * 100)
count = 10
while True:
    if count == 0:
        break
    match int(input(f'Угадайте число от 0 до 100. У вас {count} попыток - ')):
        case a if a == digit:
            print('Правильно')
            exit(0)
        case a if a > digit:
            print('ваше число больше загаданного')
            count -= 1
        case a if a < digit:
            print('ваше число меньше загаданного')
            count -= 1
print(f'Не угадали!. Загаданное число - {digit}')