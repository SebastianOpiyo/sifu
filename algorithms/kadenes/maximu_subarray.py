'''
53. Maximum Subarray
Link: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.

Examples
1. [1] -> 1
2. [2, 3, -6, 4, 2, -8, 3] -> 6
   Explanation: the maximum subarray is [4, 2], its sum is 6
3. [2, 3, -1, 4, -10, 2, 5] -> 8
   Explanation: the maximum subarray is [2, 3, -1, 4], its sum is 8
4. [-3, -1, -2] -> -1
   Explanation: the maximum subarray is [-1], its sum is -1
'''


def max_sub_array(nums: list[int]) -> int:
    curr_sum = max_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)

    return max_sum


def max_sub_array_v2(A):
    max_ending_here = max_so_far = A[0]

    for num in A[1:]:
        max_ending_here = max(max_ending_here + num, num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_sub_array([2, 3, -1, 4, -10, 2, 5]) == 8
assert max_sub_array_v2([-3, -1, -2]) == -1
assert max_sub_array_v2([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
