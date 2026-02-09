# Two Sum

# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# 
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# 
# Return the answer with the smaller index first.

from typing import List

class Solution():
    def twoSum(self, nums: List[int] , target: int) -> List[int] :

        n = len(nums)
        
        seen = {}

        for i in range(n):

            complement = target - nums[i]

            print(complement)

            if complement in seen : 

                return [seen[complement] , i]

            seen[nums[i]] = i

            print(seen)

        return []
    

if __name__ == "__main__":
    sol =Solution()
    nums=[4,5,6]
    target=10
    res = sol.twoSum(nums , target)
    print(res)