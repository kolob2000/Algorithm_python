import random

array = [random.randint(0, 10) for _ in range(10)]
minn = array[0]
maxx = array[0]
summ = 0
for i in array:
    if i < minn:
        minn = i
    if i > maxx:
        maxx = i
    summ += i
summ -= (maxx * array.count(maxx) + minn * array.count(minn))
print(array, maxx, minn, ' array, max & min elements')
print(summ, '- sum without max and min')
print(sum(array), 'common sum')
