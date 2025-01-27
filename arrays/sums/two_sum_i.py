'''
1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def two_sum(A, target):
    '''Time: O(n^2), Space: O(1)'''

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                return True

    return False


def two_sum_v1(A, target):
    '''Time: O(nlogn), Space: O(1)'''

    A.sort()
    left, right = 0, len(A) - 1

    while left < right:
        curr_sum = A[left] + A[right]

        if curr_sum == target:
            return True
        elif curr_sum > target:
            right -= 1
        else:
            left += 1

    return False


def two_sum_v2(nums: list, target: int) -> list:
    '''Time: 0(n), Space: 0(n)'''

    seen = {}

    for key, value in enumerate(nums):
        rem = target - value

        if rem in seen:
            return [key, seen[rem]]

        seen[value] = key


assert sorted(two_sum([2, 7, 11, 15], 9)) == sorted([0, 1])
assert sorted(two_sum([2, 6, 11, 7, 15], 9)) == sorted([0, 3])
