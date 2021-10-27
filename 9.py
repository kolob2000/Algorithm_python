a, b, c = map(int, input('Введите три числа через пробел - ').split())

if b < a < c or b > a > c:
    print(a)
elif a > b > c or a < b < c:
    print(b)
elif a > c > b or a < c < b:
    print(c)
