'''
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
1. [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
2. [0] -> [[],[0]]
'''


class Solution:
    '''Time: O(n*2^n)'''

    def subsets(self, nums):
        res, subset = [], []
        nums.sort()

        self.dfs(nums, 0, subset, res)

        return res

    def dfs(self, nums, index, subset, res):
        res.append(subset)

        for i in range(index, len(nums)):
            self.dfs(nums, i+1, subset+[nums[i]], res)


class Solution2:
    '''https://www.youtube.com/watch?v=REOH22Xwdkk&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=4'''

    def subsets(self, nums):
        res, subset = [], []
        self.dfs(nums, subset, res, 0)

        return res

    def dfs(self, nums, subset, res, i):
        if i >= len(nums):
            res.append(subset[:])
            return

        # Include i
        self.dfs(nums, subset + [nums[i]], res, i + 1)

        # Exclude i
        self.dfs(nums, subset, res, i + 1)
