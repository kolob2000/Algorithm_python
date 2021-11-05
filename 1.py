import random


class Array:
    def __init__(self, array: list):
        self.array = array

    def __str__(self):
        return str(self.array)

    def bubble_sort(self):
        count = 0
        count_iter = 0
        for _ in range(len(self.array) - 1):
            for j in range(len(self.array) - 1, count, -1):
                if self.array[j - 1] > self.array[j]:
                    self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                count_iter += 1
            count += 1
        print('Количество итераций - ', count_iter)


array = Array([random.randint(1, 100) for _ in range(20)])
print(array)
array.bubble_sort()
print(array)
