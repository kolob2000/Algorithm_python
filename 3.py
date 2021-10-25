import random

random_digits = [random.randint(1, 100) for _ in range(100)]

# честный  метод алгоритмом
minn = maxx = random_digits[0]
min_index = 0
max_index = 0

for index, digit in enumerate(random_digits, 0):
    if digit > maxx:
        maxx = digit
        max_index = index
    if digit < minn:
        minn = digit
        min_index = index

random_digits[min_index], random_digits[max_index] = random_digits[max_index], random_digits[min_index]

# читерский метод, результаты методов могут отличаться, обмен большего и меньшего будет верным, но индексы могут отличаться
# если несколько одинаковых элементов

random_digits[random_digits.index(min(random_digits))], random_digits[random_digits.index(max(random_digits))] = max(
    random_digits), min(random_digits)
