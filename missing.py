# from timeit import timeit
#
# print(object.mro())
#
#
# class Solution:
#     def firstMissingPositive(self, nums: list[int]) -> int:
#         min_el = nums[0]
#         next_el = 1
#         my_dict = {}
#         my_dict.setdefault(nums[0])
#         while next_el < len(nums):
#             if min_el < 0:
#                 min_el = nums[next_el]
#             elif min_el > nums[next_el] > 0:
#                 min_el = nums[next_el]
#             my_dict.setdefault(nums[next_el])
#             next_el += 1
#         if 0 > min_el or min_el > 1:
#             return 1
#         for i in nums:
#             if min_el + 1 in my_dict:
#                 min_el += 1
#             else:
#                 return min_el + 1
#
#
# print(timeit('a = [621, 622, 623, 624, 625];a[1]'))
# print(timeit("b = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5};b['a']"))
from functools import wraps


def cache_decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal cache
        if func.__name__ in cache:
            if f'{args}{kwargs}' in cache[func.__name__]:
                value = cache[func.__name__][f'{args}{kwargs}']
            else:
                value = func(args, kwargs)
                cache[func.__name__].append({})
