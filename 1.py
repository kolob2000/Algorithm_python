while True:
    users_input = input('Введите два числа и знак операции через пробел либо 0 для завершения - ').split()
    match users_input:
        case a, b, '+' as c if str.isdigit(a) and str.isdigit(b):
            print(int(a) + int(b))
        case a, b, '-' as c if str.isdigit(a) and str.isdigit(b):
            print(int(a) - int(b))
        case a, b, '*' as c if str.isdigit(a) and str.isdigit(b):
            print(int(a) * int(b))
        case a, b, '/' as c if str.isdigit(a) and str.isdigit(b):
            print(int(a) / int(b))
        case '0', :
            print('Досвидания!')
            exit(0)
        case _:
            print('Неверный ввод!')
