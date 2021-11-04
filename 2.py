from timeit import timeit


def erastrothenes_algorithm(number, printing=True):
    row_numbers = [i for i in range(0, number + 1)]
    for i in row_numbers:
        if i < 2 or i == 0:
            continue
        elif i == number:
            break
        for j in row_numbers[i + 1:]:
            if j == 0:
                continue
            elif j % i == 0:
                row_numbers[j] = 0
    if printing:
        print("Eratosthenes' algorithm - ")
        for i in row_numbers[2:]:
            if i != 0:
                print(i, end=' ')
        print()


def get_primer_by_division(number, printing=True):
    prime_numers = []
    for i in range(2, number + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            prime_numers.append(i)
    if printing:
        print('Simple division method - ')
        for i in prime_numers:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    number = int(input('Enter integer number -  '))
    erastrothenes_algorithm(number)
    print(timeit('erastrothenes_algorithm(number, printing=False)', setup='from __main__ import erastrothenes_algorithm, number',
                 number=100))

    get_primer_by_division(number)
    print(
        timeit('get_primer_by_division(number, printing=False)', setup='from __main__ import get_primer_by_division, number', number=100))



