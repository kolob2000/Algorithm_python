import random

array = list(random.sample([_ for _ in range(100)], 15))
print('------------------- Initial data --------------------')
# print(f'Origin array - {array}')
# print(f'Sorted array - {sorted(array)}')
print(f'Median by sorting - {sorted(array)[len(array) // 2]}')
############################################################
# алгоритм разработанный по определению медианы - минимальная сумма растояний...
# самый сложный алгоритм всегда O(2^n) не меньше
min_sum = sum(array)
median = 1
cycle_counter = 0
for i in array:
    sum = 0
    for j in array:
        cycle_counter += 1
        if i < j:
            sum += j - i
        else:
            sum += i - j

    # print(i, ' - ', sum)
    if min_sum > sum:
        min_sum = sum
        median = i
print('----------------- A-priority algorithm --------------')
print(f'Median - {median}')
print('Cycle quantity - ', cycle_counter)
# ############################################################################
# # Алгоритм на основе линейного поиска
# Тоже сложный алгоритм O(2^n), но если медиана поподется сразу будет O(n)
median = 0
cycle_count = 0
for i in range(len(array)):
    less_count = 0
    great_count = 0
    for j in range(len(array)):
        cycle_count += 1
        if array[i] > array[j]:
            great_count += 1
        if array[i] < array[j]:
            less_count += 1
    if great_count == len(array) // 2 or len(array) // 2 == less_count:
        median = i
        break
print('------------ Like liner search Algorithm ------------')
print(f'Median - {array[median]}')
print('Cycle quantity - ', cycle_count)
# быстрее сделать сортировку слиянием и получить медиану


################################################################################
# Алгоритм БЫСТРОГО ВЫБОРА - очень быстрый аглоритм - долго его писал... Саму суть сразу понял, а вот как счетчики организовать
# понял не сразу, три раза переписывал, на бумажке считал))
cycle = 1


def quick_select(array: list, count_left=0, count_right=0, length_sides=0):
    if length_sides == 0:
        length_sides = len(array) // 2
    pivot = 0
    left_part = []
    right_part = []
    global cycle
    cycle += 1
    for i in array:
        if array[pivot] > i:
            left_part.append(i)
        elif array[pivot] < i:
            right_part.append(i)

    if count_left + len(left_part) == length_sides or count_right + len(right_part) == length_sides:
        return array[pivot]
    elif len(left_part) + count_left + 1 == length_sides:
        median = right_part[0]
        for i in right_part:
            if i < median:
                median = i
            return median
    elif len(right_part) + count_right + 1 == length_sides:
        median = left_part[0]
        for i in left_part:
            if i > median:
                median = i
            return median
    elif len(left_part) + count_left < length_sides:
        count_left += len(left_part)
        right_part.append(array[pivot])
        return quick_select(right_part, count_left, count_right, length_sides)
    else:
        count_right += len(right_part)
        left_part.append(array[pivot])
        return quick_select(left_part, count_left, count_right, length_sides)


print('-------------- Quick Select Algorithm ----------------')
print('Median - ', quick_select(array))
print(f'Cycle quantity - {cycle}')
