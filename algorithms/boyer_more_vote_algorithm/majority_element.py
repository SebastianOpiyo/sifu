'''
169. Majority Element
https://leetcode.com/problems/majority-element/

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Examples
1. [3,2,3] -> 3
2. [2,2,1,1,1,2,2] -> 2
'''


class Solution:
    def majority_element(self, nums: list[int]) -> int:
        '''
        Boyer Moore Majority Voting algorithm
        The Boyer-Moore majority vote algorithm is an algorithm for finding the majority of a
        sequence of elements using linear time and constant space.
        '''

        counter = 1
        majority = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == majority:
                counter += 1
            else:
                counter -= 1

            if counter == 0:
                majority = nums[i]
                counter = 1

        return majority

    def majority_element2(self, nums: list[int]) -> int:
        counter = {}
        majority = len(nums) // 2

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for k, v in counter.items():
            if v > majority:
                return k


soln = Solution()
assert soln.majority_element([3, 2, 3]) == 3
assert soln.majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
