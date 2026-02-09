# Contains Duplicate


# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


from typing import List


class Solution:
    def hasDuplicate(self , nums : List[int]) -> bool :
        n = len(nums)
        nums.sort()
        for i in range(1 , n):
            if nums[i] == nums[i-1]:
                return True
            
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,1]
    res = sol.hasDuplicate(nums)
    print("Array contains duplicate item ? >>", res)


