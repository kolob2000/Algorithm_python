import random as r

first_int, second_int = map(int, input('Введит два целых числа диапозона через пробел - ').split())
if first_int > second_int:
    _ = first_int
    first_int = second_int
    second_int = _
first_float, second_float = map(int, input('Введит два вещественных  числа диапозона через пробел - ').split())
if first_float > second_float:
    _ = first_float
    first_float = second_float
    second_float = _

first_char, second_char = map(ord, input('введите два символа через пробел - ').lower().split())
if first_char > second_char:
    _ = first_char
    first_char = second_char
    second_char = _
print(r.randint(first_int, second_int))
print(r.uniform(first_float, second_float))
print(chr(r.randint(first_char, second_char)))
