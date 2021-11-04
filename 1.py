from collections import OrderedDict
from functools import wraps
from timeit import timeit


# Как и обещал в дз4 использую collection(дз4 сдал раньше дз3)
# использую OrderedDict как очередь с приорететом для написания самописного lru cache
# с возможностью задания размера кэша
def lru_cache_decorator(max_length=128):
    def _lru_cache_decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache
            if f'{args}{kwargs}' in cache:
                cache.move_to_end(f'{args}{kwargs}')  # при выборке из кэша ячейка сдвигается в конец
                # print('беру из кэша')
                return cache[f'{args}{kwargs}']
            else:
                if len(cache) >= max_length:  # привышение размера кэша самый старый выкидываем
                    cache.popitem(last=False)
                # print('считаю')
                cache[f'{args}{kwargs}'] = func(*args, **kwargs)
                return cache[f'{args}{kwargs}']

        return wrapper

    return _lru_cache_decorator


@lru_cache_decorator()
def fibonachi_recursive(n):
    if n < 2:
        return n
    return fibonachi_recursive(n - 1) + fibonachi_recursive(n - 2)


def fibonachi_recursive_2(n):
    if n < 2:
        return n
    return fibonachi_recursive_2(n - 1) + fibonachi_recursive_2(n - 2)


def fibonachi_cycle(n):
    prev = 1
    nexxt = 1
    print(1, '   \t', nexxt)
    for _ in range(2, n + 1):
        prev, nexxt = nexxt, nexxt + prev
        print(_, '   \t', nexxt)


# /////////////////////////////////////// RECURSIVE WITHOUT LRU ////////////////////////////////////////////
print('fibonachi без lru кэш')
print(timeit('print(fibonachi_recursive_2(40))', setup='from __main__ import fibonachi_recursive_2', number=1))

# ////////////////////////////////////// RECURSIVE WITH LRU ////////////////////////////////////////////////

print('fibonachi с lru кэш')
print(timeit('print(fibonachi_recursive(40))', setup='from __main__ import fibonachi_recursive', number=1))

# ////////////////////////////////////// CYCLE FUNCTION ///////////////////////////////////////////////

print('fibonachi_cycle')
print(round(timeit('fibonachi_cycle(100)', setup='from __main__ import fibonachi_cycle', number=1), 4))

# рекурсивная функция вычисления числа фибоначи имеет очень высокую временную сложность
# каждая функция имеет два вызова функциии что соответствует 2^n,
# для числа 100 = 1267650600228229401496703205376(126 октилионов) фызовов функций, сделал попытку
# вызвать ее для числа 100, с lru_cache декоратором функция выполнилась за 3.5 секунды, без кэша ждал час,
# не дождался выключил, выполнил для числа 40 lru - 0.00017 секунды, без кэша 37.6 секунд. Реализовал ту же функцию
# при помощи циклов никаких кэшэй не используется, разница колосальная фукнкция
# выполнилась меньше чем за 0.0008 секунды для числа 100, при том что еще и принтует каждое число.
