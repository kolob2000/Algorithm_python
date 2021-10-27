a, b, c = map(int, input('Введите длину трех отрезков через пробел - ').split())

if a + b <= c or b + c <= a or a + c <= b:
    print('Треугольник не существует!')
else:
    if a == b and b == c:
        print('Треугольнк равносторонний')
    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        print('Прямоугольник равнобедренный')
    else:
        print('Треугольник разносторнний')
