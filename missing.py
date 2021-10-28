class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        min_el = nums[0]
        next_el = 1
        my_dict = {}
        my_dict.setdefault(nums[0])
        while next_el < len(nums):
            if min_el < 0:
                min_el = nums[next_el]
            elif min_el > nums[next_el] > 0:
                min_el = nums[next_el]
            my_dict.setdefault(nums[next_el])
            next_el += 1
        if 0 > min_el or min_el > 1:
            return 1
        for i in nums:
            if min_el + 1 in my_dict:
                min_el += 1
            else:
                return min_el + 1
