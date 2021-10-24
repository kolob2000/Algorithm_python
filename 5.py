import random

array = [random.randint(-100, 100) for _ in range(100)]


element = min(array)  # или можно было также найти обычным алгоритмом, как в предыдущих задачах и элемент и индекс
index = array.index(min(array))  # без встроенных функций голым питоном
for j, i in enumerate(array, 0):  # и также считать индекс обычным счетчиком инкрементируя
    if element < i < 0:
        element = i
        index = j

print(sorted(array))
print(f'Index:{index} \n Element: {element} ')
