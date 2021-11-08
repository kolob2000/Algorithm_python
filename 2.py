import random


class Array:
    def __init__(self, arr: list):
        self.array = arr
        self.func_count = 0

    def __str__(self):
        return str(self.array)

    def merge_sort(self):
        def sorting(array: list):

            _len = len(array)
            if _len == 1:
                return array
            first = sorting(array[:_len // 2])
            second = sorting(array[_len // 2: _len])
            array = []
            j = 0
            i = 0
            for _ in range(len(second) + len(first) - 1):
                self.func_count += 1
                if first[i] < second[j]:
                    array.append(first[i])
                    i += 1
                    if i == len(first):
                        array.extend(second[j:])
                        break
                else:
                    array.append(second[j])
                    j += 1
                    if j == len(second):
                        array.extend(first[i:])
                        break
            return array

        self.array = sorting(self.array)
        print(f'Cycle quantity - {self.func_count}')
        return self.array


array = Array([round(random.uniform(0, 50), 2) for _ in range(20)])
print(f'Not sorted array: \n{array}')
print('\nSorted array with Merge sort:')
print(array.merge_sort())
