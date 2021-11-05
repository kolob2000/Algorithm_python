import random
import sys


# Сильно обширные выводы сделать сложно посколько все три алгоритма решают различные задачи
# скорее необходимо сравнивать различные алгоритмы решающие те же задачи например алгоритмы сортировки.
# Но некоторые вещи всё же заметны если в переменную сохраняется просто число к примеру a = 1 то переменная занимает 24
# байта, а если же тоже самое значение передается из итерируемого объекта на приемер а = array[i], то а уже занимает
# 28 байт. Также обратил внимание что в алгоритмах в которых последовательность хранится в массиве займет больше места,
# чем к примеру в динамически созданых переменных, поэтому при возможности лучше использовать генераторы вместо
# списковых включений, если это возможно.

def two_min_element():
    array = [random.randint(1, 50) for _ in range(20)]
    most_min = array[0]
    next_min = array[1]
    count = 0
    # не знаю, может избыточно, но постарался реализовать на голом питоне
    for i in array:
        if i == most_min:
            count += 1
        if i < most_min:
            most_min = i
            count = 1
        if array[0] > array[1]:
            next_min = array[0]  # на всякий случай если минимальным будет array[1] единственным элементом

    if count > 1:
        next_min = most_min
    else:
        for i in array:
            if most_min < i < next_min:
                next_min = i
    print(f'count\t        {sys.getsizeof(count)}  bytes'
          f'\nmost_min\t    {sys.getsizeof(most_min)}  bytes\n'
          f'next_min\t    {sys.getsizeof(next_min)}  bytes\n'
          f'array\t        {sys.getsizeof(array)} bytes')

    print(sorted(array), most_min, next_min)


def most_digit_sum():
    digits = input('Введите натуральные числа через пробел - ').strip().split()
    max = 0
    summ = 0  # избыточная переменная - объявленна толко для отоброжения ее в анализе
    print(digits)
    print(f'max\t        {sys.getsizeof(max)}  bytes'
          f'\nsumm\t    {sys.getsizeof(summ)}  bytes\n'
          f'digits\t    {sys.getsizeof(digits)}  bytes')

    for i in digits:
        summ = 0
        for j in i:
            summ += int(j)
        if summ > max:
            max = summ
            digit = i

    print(digit)


def chr_ord_table():
    count = 0
    for i in range(32, 128):
        if count == 0:
            print(f'count\t    {sys.getsizeof(count)}  bytes'
                  f'\ni\t        {sys.getsizeof(i)}  bytes\n')
        if count % 10 != 0 or count == 0:
            print(f'{i}  {chr(i)}      ', end=' \t')
        else:
            print('\n')
            print(f'{i}  {chr(i)}       ', end=' \t')
        count += 1


if __name__ == '__main__':
    print('1. Два минимальных элемента - ')
    two_min_element()
    print('\n2. Число с наибольшей суммой разрядов -')
    most_digit_sum()
    print('\n3. Таблица код - символ -')
    chr_ord_table()
