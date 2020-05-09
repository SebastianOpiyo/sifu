"""
How Many Numbers Are Smaller Than the Current Number
Given the array nums, for each nums[i] find out 
how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number 
of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
"""

def smallerNumbersThanCurrent(nums):
    '''Time complexity: O(nlogn)'''
    sorted_nums = sorted(nums)
    mappings = {}
    
    for k, v in enumerate(sorted_nums):
        if v not in mappings:
            mappings[v] = k
    return [mappings[x] for x in nums]


nums = [8, 1, 2, 2, 3] 
assert smallerNumbersThanCurrent(nums) == [4,0,1,1,3]