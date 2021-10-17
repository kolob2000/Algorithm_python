import random as r

a, b = map(int, input('Введит два числа диапозона через пробел - ').split())
if a > b:
    e = a
    a = b
    b = e
c, d = map(ord, input('введите два символа через пробел - ').split())
if c > d:
    e = c
    c = d
    d = e
print(chr(r.randint(c, d)))
print(r.randint(a, b))
print(r.uniform(a, b))
