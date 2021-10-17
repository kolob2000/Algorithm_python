import random as r

a, b = map(int, input('Введит два целых числа диапозона через пробел - ').split())
if a > b:
    e = a
    a = b
    b = e
f, g = map(int, input('Введит два вещественных  числа диапозона через пробел - ').split())
if a > b:
    e = f
    f = g
    g = e

c, d = map(ord, input('введите два символа через пробел - ').lower().split())
if c > d:
    e = c
    c = d
    d = e
print(r.randint(a, b))
print(r.uniform(f, g))
print(chr(r.randint(c, d)))
